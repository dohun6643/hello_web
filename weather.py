from bs4 import BeautifulSoup
import requests

url = 'http://api.openweathermap.org/data/2.5/weather?q=London&appid=7596736f93e668ed3a0074ee3f0c7836'
res = requests.get(url=url).json()

data = res["weather"]
print(data)


