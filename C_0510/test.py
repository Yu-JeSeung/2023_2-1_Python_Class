import time
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.weather.go.kr/w/index.do"
# Chrome브라우저 및 get요청
browser = webdriver.Chrome()
browser.implicitly_wait(15) # 최대 (원하는)초 동안 대기
browser.get(url)
time.sleep(15)


temp = browser.find_element(By.CSS_SELECTOR,'#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-2.no-underline > li:nth-child(2) > span.val').text


# 데이터 수정
# replace
temp_replace = float(temp.replace("℃",""))
# split
temp_split = float(temp.split("℃")[0])
if temp_replace > temp_replace-1:
    print("오늘 날씨가 더워요")

# 스크래핑만 한 데이터
print(f"현재온도: {temp}")
# replace or split 으로 조작한 데이터
print(f"조작한데이터: {temp_replace}")
