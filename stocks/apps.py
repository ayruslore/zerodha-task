from django.apps import AppConfig
#from apscheduler.schedulers.background import BackgroundScheduler

class StocksConfig(AppConfig):
    name = 'stocks'

    '''
    def ready(self):
        from . import views
        scheduler = BackgroundScheduler()
        scheduler.add_job(views.data_downloader, 'interval', seconds=5)
        scheduler.start()
    '''