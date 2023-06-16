# 리스트

import datetime

value = datetime.datetime.now()
lists = [1, 2, 3, 4, [5, 6, 7], True, 'Hello', value] # 들어갈 수 있는 데이터의 제약 없음

print(lists) # => [1, 2, 3, 4, [5, 6, 7], True, 'Hello', datetime.datetime(2023, 6, 16, 15, 0, 49, 787939)]
print(lists[-2]) # => Hello

# 2차원배열
print(lists[4][1]) # => 6
print(lists[-2][-1]) # => o # 문자열도 배열

print(lists[:4]) # => [1, 2, 3, 4]
# [찾고싶은 시작인덱스:마지막인덱스+1]

# 리스트 연산
a = [1, 2, 3]
b = [4, 6, 8]
print(a + b) # => [1, 2, 3, 4, 6, 8]
print(a * 2) # => [1, 2, 3, 1, 2, 3]

a[2] = False # 2번 인덱스에 False를 할당
print(a) # => [1, 2, False]

del b[2] # 2번 인덱스 지우기
print(b) # => [4, 6]

# 리스트 함수 (중요)
c = [3, 6, 9]
c.append(12) # 리스트 마지막에 추가
print(c) # => [3, 6, 9, 12]

d = [6, 4, 9, 3, 2, 1]
d.sort() # 오름차순 정렬 (문자열도 정렬가능)
print(d) # => [1, 2, 3, 4, 6, 9]

e = [3, 4, 6, 2, 5]
e.reverse() # 역정렬X, 현재 순서 뒤집기
print(e) # => [5, 2, 6, 4, 3]

#역정렬 (내림차순정렬)
e.sort(reverse=True) 
print(e) # => [6, 5, 4, 3, 2]

e.insert(2, 5.5) # 2번 인덱스에 5.5 입력
print(e) # => [6, 5, 5.5, 4, 3, 2]

print(e.index(5.5)) # => 2 # 값의 위치 찾기

e.append(6)
print(e) # => [6, 5, 5.5, 4, 3, 2, 6]
e.remove(6) # 값을 지움 (하나만)
print(e) # => [5, 5.5, 4, 3, 2, 6]
e.remove(6) # 값을 지움 (하나만)
print(e) # => [5, 5.5, 4, 3, 2]


