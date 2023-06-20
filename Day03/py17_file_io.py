# 파일 입출력

# 절대경로 지정시 사용가능
import os
curr_path = os.getcwd # 현재 파이썬 경로 (많이 사용)
print(curr_path) # C:\Source\bigdata-python-2023> 

# 파일 생성하기
# filename = 'sample.txt'
filename = './Day03/sample.txt' # 상대경로 지정
# filename = 'C:\\Source\\bigdata-python-2023\\Day03\\test.txt' # 절대경로 지정
# filename = 'C:/Source/bigdata-python-2023/Day03/test2.txt' # 절대경로 # 리눅스/유닉스와 동일하게 사용가능
f = open(filename , mode='wt', encoding='utf-8') # 텍스트 파일 생성 (ascii 코드로 기본 생성)

f.write('인생은 짧습니다. 파이썬을 쓰세용 \n')
f.write('인생은 짧습니다. 파이썬을 쓰세용') # 마지막 문장에는 \n을 안쓰는 게 좋음

f.close() # 무조건 닫아줘야함
# DB, Network, File 전부 open 하면 무조건 close 해주기
print(f'{filename}이(가) 생성되었습니다')


# 파일 읽기
fr = open(filename, mode='r', encoding='utf-8') # 읽기
while True: # 무한루프
    line = fr.readline() # 한줄씩 읽기
    if not line: break # 읽을 줄이 없으면 빠져나가기
    print(line, end='')

fr.close() # 무조건 파일 닫기
'''
인생은 짧습니다. 파이썬을 쓰세용
인생은 짧습니다. 파이썬을 쓰세용
'''