# 튜플
# 리스트와 유사하지만 추가, 수정, 삭제가 불가능 (immutable)

l1 = [1,2,3] # 리스트
t1 = (1,2,3) # 튜플, 소괄호() 생략 가능
print(t1) # => (1, 2, 3)

l1.append(4) # 리스트 => 추가 가능
# t1.appent(4) # (예외발생) 튜플은 추가가 불가능
# del t1[0] # (예외발생) 튜플은 삭제 불가

print(t1[2]) # => 3
print(t1[:2]) # => (1, 2)

t2 = (5,6,7)
t3 = t1 + t2 # 튜플을 가공해 새로운 튜플을 만들 수 있음
print(t3) # => (1, 2, 3, 5, 6, 7)

# 값을 여러개 반환받기 (java, c#, python 모두 사용 가능)
def calc(x, y):
    # 사칙연산 모두 다 처리
    add = x + y
    minus = x - y
    mult = x * y
    div = x / y
    
    return (add, minus, mult, div)

res1, res2, res3, res4 = calc(5,8)
print(res1, res2, res3, res4) # => 13 -3 40 0.625