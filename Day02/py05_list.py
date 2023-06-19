# 리스트

a = [1,2,3]

print(a) # => [1, 2, 3]

# 자료구조 stack 에 있는 pop 기능 구현
print(a.pop()) # => 3 # 리스트의 맨 마지막 요소 꺼내기
print(a) # => [1, 2] # 꺼낸 요소는 사라짐

a.append(10) # 리스트 마지막에 집어넣기
print(a) # => [1, 2, 10]

print(a.count(2)) # => 1 # 리스트 안에 값이 몇 개 있는지 세기

# 리스트 확장
a.extend([5, 3, 2])
print(a) # => [1, 2, 10, 5, 3, 2]

print(a.count(2)) # => 2