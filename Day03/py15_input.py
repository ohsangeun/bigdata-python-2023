# 입출력
import datetime

# birth_year = input('출생년도를 입력하세요 > ') # 키보드 입력 (무조건 str)
# birth_year = int(input('출생년도를 입력하세요 > ')) # 형변환
birth_year = 1996

print(f'당신의 출생년도는 {birth_year}년 입니다') # 콘솔출력

# 나이 구하기
curr_year = datetime.datetime.now().year # 현재 년도
# print(curr_year)
age = curr_year - birth_year
print(f'당신의 나이는 {age}세 입니다') # 오류 TypeError: unsupported operand type(s) for -: 'int' and 'str' => 키보드에서 입력된 값은 문자열이기 때문에 빼기 연산 불가 => 형변환 필요 (5번줄)

a = 123
a = [3, 6, 9]

print(a) # [3, 6, 9]

print('Life' + 'is' + 'short') # Lifeisshort
print('Life' 'is' 'short') # Lifeisshort
print('Life', 'is', 'short') # Life is short
print('Life', 3.14, True) # 문자열, 숫자, True False 도 출력가능


print(range(10)) # range(0, 10)
print(len(range(10))) # 10

for i in range(10):
    if i == len(range(10)) - 1:
        print(i, end='\n')
    else:
        print(i, end=', ')
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9

print('Life', 'is', 'short', sep='&') # Life&is&short # 별로안씀

# format string
pi = 3.14159265359
print(f'PI = {pi:.4f}') # PI = 3.1416 
print(f'PI = {pi:10.2f}') # PI =       3.14
