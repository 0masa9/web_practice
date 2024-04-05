import requests
from bs4 import BeautifulSoup

load_url = "https://mypage.shirucafe.com/user/meetups?_url=%2Fuser%2Fmeetups&lang=ja&day_of_week=&store_id=35&month=-1&page=1"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

topic = soup.find(class_ = "article-feed")

for element in topic.find_all("a"):
    url = element.get("href")
    html = requests.get(url)
    print(url)
     