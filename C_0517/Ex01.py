import requests

from bs4 import BeautifulSoup

url = "https://finance.naver.com/"

filename = "증권뉴스.csv"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

data_rows = soup.find("div", attrs={"class" :"section_strategy"}).find("ul").find_all("span")

for row in data_rows:
    columns = row.find("a")
    data = [column.get_text().strip() for column in columns]
    print(data)
