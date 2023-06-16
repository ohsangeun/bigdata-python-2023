# 문자열

print('"안녕하"세요?') # => "안녕하"세요?
print("안녕하'세요?'") # => 안녕하'세요?'
print("\"안녕\"하세요?") # => "안녕"하세요?

value = '''
안뇽하세요
이거 쓰면 여러줄 쓸 수 있대요
"""  이렇게도 할 수 있대요
'''

print(value)
# 안뇽하세요
# 이거 쓰면 여러줄 쓸 수 있대요
# """  이렇게도 할 수 있대요

'''
그리고 얘로 여러줄 주석 대체 가능하대요
좋다 ~
'''

print('Hello' + ' World!') # => Hello World!
# print('Hello' * ' World!') # => 불가능
# print('Hello' + 4) # => 불가능
print('Hello' * 4) # => HelloHelloHelloHello

# 문자열의 길이 확인 (공백포함)
print(len('Life is short')) # => 13
print(len('인생은 짧아요')) # => 7

origin = 'Life is short, You need Python'
print(origin[0]) # => L
print(origin[0] + origin[16] + 
      origin[19] + origin[20] + 
      origin[0].lower() + origin[15].lower()) # => Lonely # lower() == 소문자로
print(origin[:4]) # => Life # [시작인덱스:끝인덱스 + 1] # 시작인덱스가 0일 때 생략가능
print(origin[8:13]) # => short
print(origin[8:13]) # => short
print(origin[15:]) # => You need Python # 끝인덱스가 마지막번호일 때 생략가능
print(origin[15:-7]) # => You need # 음수는 뒤에서부터 센 인덱스(-1부터 시작)

# 문자열 포매팅
# % => string formating
print('I ate %s apples' % ('three')) # => I ate three apples (문자는 %s)
print('I ate %d apples' % (3)) # => I ate 3 apples (숫자는 %d)
print('pi is %f' % 3.14159265359) # => pi is 3.141593 (숫자를 문자로 바꾸면서 문자열 포매팅)
print('pi is %10.2f' % 3.14159265359) # => pi is       3.14

# 날짜 => 문자열 포매팅
import datetime as dt
curr_dt = dt.datetime.now()
print(curr_dt) # => 2023-06-16 13:56:56.826759 현재시간 출력
print('오늘 날짜는 %s' % curr_dt) # => 오늘 날짜는 2023-06-16 13:58:34.168986
print('오늘 날짜는 %s' % curr_dt.strftime('%Y년 %m월 %d일')) # => 오늘 날짜는 2023년 06월 16일

fmt_dt = curr_dt.strftime('%Y년 %m월 %d일')

# 최신 포매팅
apple_num = 3
print(f'I ate {apple_num} apples') # => I ate 3 apples
print(f'I ate {apple_num:0.4f} apples') # => I ate 3.0000 apples
apple_num = 'three'
print(f'I ate {apple_num} apples') # => I ate three apples

print(f'오늘 날짜는 {fmt_dt}') # => 오늘 날짜는 2023년 06월 16일

# 문자열 함수
# Life is short, You need Python
print(origin.count('o')) # => 3 # count => 문자, 문자열의 개수
print(origin.find('Python')) # => 24 # find => 문자(열)의 시작 인덱스
print(origin.find('python')) # => -1
print(origin.find('w')) # => -1 (일치하는 결과가 없을 때) 

print('/'.join(origin)) # => L/i/f/e/ /i/s/ /s/h/o/r/t/,/ /Y/o/u/ /n/e/e/d/ /P/y/t/h/o/n
# '문자(열)'을 join() 에 있는 문자열이랑 하나씩 합침
print(origin.upper()) # => LIFE IS SHORT, YOU NEED PYTHON # 대문자로
print(origin.lower()) # => life is short, you need python # 소문자로
print(origin.capitalize()) # => life is short, you need python # 시작 문자만 대문자
print(origin.title()) # => Life Is Short, You Need Python # 단어의 첫번째 글자만 대문자로

#공백지우기
print('start','     Hello    ', 'end') # start      Hello     end
print('start','     Hello    '.lstrip(), 'end') # start Hello     end # 왼쪽 공백 지우기 # , 는 자동 공백 하나
print('start'+'     Hello    '.lstrip() +'end') # startHello    end
print('start','     Hello    '.rstrip(), 'end') # start      Hello end # 오른쪽 공백 지우기
print('start','     Hello    '.strip(), 'end') # start Hello end # 양쪽 공백 지우기

result = origin.split(' ') # 공백으로 자르기
print(result) # => ['Life', 'is', 'short,', 'You', 'need', 'Python']
result = origin.replace(',', '').split(' ') # , 를 지우고 공백으로 자르기
print(result) # => ['Life', 'is', 'short', 'You', 'need', 'Python']

print(result[2]) # => short