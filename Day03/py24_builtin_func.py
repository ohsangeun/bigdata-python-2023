# 내장함수

print(abs(-4)) # 4 절대값
print(chr(97)) # a # 숫자를 캐릭터로 변경 # ascii 코드 번호
print(chr(44032)) # 가 # utf-8 코드번호
print(ord('각')) # 44033 # ascii 코드 번호로 변환
print(ord('a')) # 97 # 유니코드 숫자값으로 변환
print(chr(13)) # enter
print(min(1,2)) # 1 # 최소값
print(max(1,2)) # 2 # 최대값
print(eval('1 + 4')) # 5 # eval[uate] 실행
print(hex(234)) # 0xea # 16진수
a = 0
b = 1
print(id(a)) # 140731667899144 # a 변수의 메모리 주소
print(id(b)) # 140731665146664 # b 변수의 메모리 주소

print(int('3')) # 3 # digit number 문자열를 숫자로 변환 # 3.0 은 불가능
print(pow(2,10)) # 1024 # 제곱승 함수
print(2 ** 10) # 1024 # 제곱승 식


# map
def three_times(numberlist):
    result = []
    for n in numberlist:
        result.append(n * 3)
    return result

res = list(three_times([3, 6, 9, 12])) # 함수 파라미터로 리스트를 받아서 반복문을 돌려 처리
print(res) # [9, 18, 27, 36]


def three_times2(x):
    return x * 3

# 첫번째 파라미터: 함수, 두번째 파라미터: 리스트
# 리스트 요소를 하나씩 함수를 통해서 처리해주는 방식
print(list(map(three_times2, [3, 6, 9, 12]))) # [9, 18, 27, 36]
# map 결과가 map object기 때문에 list 또는 tuple, set 으로 형변환 필요

print(list(map(str, [3, 6, 9, 12]))) # ['3', '6', '9', '12']
print(list(map(float, [3, 6, 9, 12]))) # [3.0, 6.0, 9.0, 12.0]


# range list 활용, 순차적인 리스트를 쉽게 만들 수 있음
print(range(3, 11)) # range(3, 11)
print(list(range(3, 11))) # [3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(3, 50, 3))) # [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48] # 3의 배수만
print(sum(list(range(3, 50, 3)))) # 408 # py12_control.py 연습문제와 동일

print(round(4.6)) # 5
print(round(3.141592, 4)) # 3.1416 # 소수점 네번째 자리에서 반올림

l1 = [3, 10, 2]
# l1.sort()
# print(l1) # [2, 3, 10]
print(sorted(l1)) # [2, 3, 10]

# 변수값의 타입을 리턴
print(type(12)) # <class 'int'>
print(type('a')) # <class 'str'>
print(type(True)) # <class 'bool'>
print(type([1,2,3])) # <class 'list'>
print(type(None)) # <class 'NoneType'>