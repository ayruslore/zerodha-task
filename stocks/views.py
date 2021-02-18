from django.shortcuts import render
from django.http import HttpResponse
import datetime, os, zipfile, redis, csv

RedisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

def download_and_extract(today):
    equity_bhavcopy = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ'
    equity_bhavcopy_zip_url = equity_bhavcopy + today[:2] + today[3:5] + today[8:] + '_CSV.ZIP'
    zip_file_name = equity_bhavcopy_zip_url.split('/')[-1]
    os.system('wget ' + equity_bhavcopy_zip_url)
    zipfile.ZipFile(zip_file_name).extractall()
    os.remove(zip_file_name)

def parse_and_save_in_redis(today):
    csv_file_name = 'EQ' + today[:2] + today[3:5] + today[8:] + '.CSV'
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                row[1] = row[1].strip()
                with RedisClient.pipeline() as pipe:
                    pipe.multi()
                    pipe.hset(row[1], 'code', row[0])
                    pipe.hset(row[1], 'open', row[4])
                    pipe.hset(row[1], 'high', row[5])
                    pipe.hset(row[1], 'low', row[6])
                    pipe.hset(row[1], 'close', row[7])
                    pipe.execute()
            line_count += 1
    os.remove(csv_file_name)

def search_stock_name(name):
    answer = RedisClient.hgetall(name)
    if answer != {}:
        result = {'code':answer[b'code'].decode('ascii'), 'open':answer[b'open'].decode('ascii'),
                'high':answer[b'high'].decode('ascii'), 'low':answer[b'low'].decode('ascii'),
                'name':name, 'close':answer[b'close'].decode('ascii')}
        return result
    else:
        return {}

def index(request):
    return render(request, 'index.html', context = {})

def download(request):
    today_date = datetime.date.today().strftime("%d-%m-%Y")
    download_and_extract(today_date)
    parse_and_save_in_redis(today_date)
    return HttpResponse('Downloading Done!!\n')

def search(request, stock):
    context = search_stock_name(stock)
    return render(request, 'index.html', context=context)