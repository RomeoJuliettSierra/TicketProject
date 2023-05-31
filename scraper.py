# Author: Joel Ruuben Seene
# Project idea: scraper for https://elron.pilet.ee/et/otsing/<start>/<destination>/<date: YYYY-MM-DD>

import requests
import datetime
from bs4 import BeautifulSoup

headers = {
    # User User-Agent header to bypass spider/scraper protection, just in case
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'
}

start = input("Input starting stop: ")
destination = input("Input destination: ")
date = input("Input date (leave empty for today's date: ")

if date == '':
    date = str(datetime.date.today())


url = 'https://elron.pilet.ee/et/otsing/' + start + '/' + destination + '/' + date + '/'
