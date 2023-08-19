import threading
import time
import requests
from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

def scrape_and_store_data():
    while True:
        url = 'https://www.nseindia.com/api/equity-stockIndices?index=NIFTY%2050'
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.117 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            print(data)
            cache.set('nifty_data', data, 300)
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")

        time.sleep(300)

data_thread = threading.Thread(target=scrape_and_store_data)
data_thread.daemon = True 
data_thread.start()  

def nifty_data(request):
    company_data = cache.get('nifty_data')

    if company_data:
        context = {'company_data': company_data['data']}
    else:
        context = {}

    return render(request, 'scraper/cards.html', context)