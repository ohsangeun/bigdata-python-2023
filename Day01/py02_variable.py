# 변수
import sys

number = 1000000000 # 사이즈 제한 없음
value = sys.maxsize # 파이썬 시스템에서 제공하는 최고 숫자

print(number) # => 1000000000
print(value) # => 9223372036854775807
print(value + 1) # => 9223372036854775808
# => 최고숫자보다 더 큰 수도 담을 수 있음.. overflow 가 없다..!

value2 = 0o12 # 8진수
print(value2) # => 10

value2 = 0xFF # 16진수
print(value2) # => 255

value2 = '문자로 변경 가능'
print(value2) # => 문자로 변경 가능

value2 = False
print(value2 == True) # => False
print(value2 == False) # => True

# 사칙연산, 수학식
print(20 / 3) # => 6.666666666666667 => 소수점 나누기
print(20 // 3) # => 6 => 정수로 나누기
print(2 ** 10) # => 1024 => 승수 (2의 10승)
print(10 % 3) # => 1 => 나머지