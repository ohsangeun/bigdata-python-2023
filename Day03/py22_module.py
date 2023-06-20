# 모듈 사용

import datetime as dt # as 로 이름 줄이기
curr_date = dt.datetime.now()
print(curr_date) # 현재시간

# from datetime import datetime # 사용할 클래스만 가져오기
from datetime import datetime as dt1 # 이름 줄이기
curr_date = dt1.now()
print(curr_date) # 현재시간

# 함수만 가져오기
from os import getcwd
print(getcwd())