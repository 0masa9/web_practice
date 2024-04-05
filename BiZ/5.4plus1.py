import requests
from bs4 import BeautifulSoup

load_url = "https://mypage.shirucafe.com/user/meetups?_url=%2Fuser%2Fmeetups&lang=ja&day_of_week=&store_id=35&month=-1&page=1"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

topic = soup.find(class_ = "article-feed")

for element in topic.find_all("a"):
    url = element.get("href")
    detail_url = requests.get(url)
    
    soup = BeautifulSoup(detail_url.content, "html.parser")

    datetime_class = soup.find(class_ = "datetimeplace_detail")
    datetime = datetime_class.find("p")
    formatted_string_datetime = datetime.text.replace("\n", "").replace(" ", "")
    print(formatted_string_datetime)

    company = soup.find(class_ = "meetup-detail-sponsor-name")
    print(company.text,"\n")   








