# 표준 라이브러리

from datetime import date, datetime

first_date = date(2022, 12, 25)
curr_date = date.today()
print(curr_date - first_date) # 178 days, 0:00:00

# 현재 시간
curr_dt = datetime.now()
print(curr_dt) # 2023-06-21 10:44:13.948211
print(curr_dt.strftime('%Y-%m-%d')) # 2023-06-21

# 현재 요일
print(curr_dt.weekday()) # 0부터 월요일 (수요일은 2)
print(curr_dt.isoweekday()) # 1부터 월요일 (수요일은 3)

# import time
# for x in range(10):
#     print(x)
#     time.sleep(0.1) # second # C#, C++, java => ms


import math
print(math.pi) # 3.141592653589793

import os
# print(os.environ) # 컴퓨터.. 정보?
# print(os.environ['PATH']) # 컴퓨터.. 정보?
# print(os.getcwd) # 실행중인 워크스페이스 위치
# print(os.system('dir'))

# json
import json
with open('./Day04/data.json', mode='r', encoding='utf-8') as f:
    data = json.load(f) # load => str, loads => byteArray

print(data) # {'이름': '김마루', '생일': '0621', '나이': 5, '여자': True, 'option': [{'test': 1}]}


# urllib
from urllib.request import urlopen

res = urlopen('https://www.naver.com')
print(res.status) # 200
# print(res.read().decode('utf-8')) # index.html 가져옴 => 웹 크롤링에 사용

# 크롬브라우저로 naver.com 띄우기
import webbrowser
print(webbrowser.get())
url = 'http://www.naver.com'
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
webbrowser.get(chrome_path).open(url)
# 프로그램을 종료하면 웹브라우저도 같이 종료