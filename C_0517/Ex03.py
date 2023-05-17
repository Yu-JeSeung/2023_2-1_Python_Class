# 사이트 자료를 csv파일로 만들기
import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="")
writer = csv.writer(f)

title = "순위 연속  누적  종목명 현재가 전일비  등락률    거래량 시가  고가  저가".split("\t")
writer.writerow(title)

for page in range(1,3):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
        
    data_rows  = soup.find("table", attrs={"class": "type_2"}).find_all("tr")

    for row in data_rows:
        i = 1
        columns = row.find_all("td")
        if len(columns) <= 1:
                continue
        data = [column.get_text().strip() for column in columns]
        writer.writerow(data)
