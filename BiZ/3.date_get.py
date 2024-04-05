import requests
from bs4 import BeautifulSoup

load_url = "https://mypage.shirucafe.com/user/meetups/detail/48647?page=1"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")


topic = soup.find(class_ = "datetimeplace_detail")
topic2 = topic.find("p")

S = topic2.text
formatted_string = S.replace("\n", "").replace(" ", "")
print(formatted_string)
     