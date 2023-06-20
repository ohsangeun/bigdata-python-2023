# CSV 파일 읽기
import csv

# csvfile = '부산광역시_시내버스_이용건수.csv'
csvfile = '충청북도_푸드뱅크현황.csv'
dirname = './Day03/'

# \ufeff 가 숨어있는 경우 encoding='utf-8-sig' 사용
fr = open(f'{dirname}{csvfile}', mode='rt', encoding='utf-8-sig') # 한국어는 기본이 cp949
reader = csv.reader(fr, delimiter=',') # delimiter => 구분자

for line in reader:
    print(line)

fr.close()