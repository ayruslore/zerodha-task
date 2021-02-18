# My Zerodha Career Task

## Python Django web app/server

### Task

1. Downloads the equity bhavcopy zip from the above page every day at 18:00 IST for the current date using cron.
1. Extracts and parses the CSV file in it.
1. Writes the records into Redis with appropriate data structures (Fields: code, name, open, high, low, close).
1. Renders a simple VueJS frontend with a search box that allows the stored entries to be searched by name and renders a table of results and you can download the results as CSV.
1. The search is performed on the backend using Redis.

### APIS
1. The home page of the website is served on https://127.0.0.1:8000/stocks/
1. The server downloads the data using http://127.0.0.1:8000/stocks/download
1. On clicking the search button, it makes an api call https://127.0.0.1:8000/stocks/search/<str:stock> to fecth the stock info.

### Usage
Go to the website https://127.0.0.1:8000/stocks/, enter the stock name in search bar and click the search button. It shows the stock details if the stock exists and allows the table to be downloaded as csv.
