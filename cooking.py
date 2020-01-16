import requests
from bs4 import BeautifulSoup
import sys
from time import sleep
 
query = "カレー"
url = "https://cookpad.com/" #クックパッド
res = requests.get(url)
status = res.status_code