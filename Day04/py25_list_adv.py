# 리스트 고급사용
# 1 ~ 1000 사이의 3의 배수

# 방법 1)
list_3rd = []
for n in range(1, 1000+1):
    if n % 3 == 0:
        list_3rd.append(n)
# print(list_3rd)

# 방법 2)
list_3rd_2 = [n for n in range(3, 1000+1, 3)]
# print(list_3rd_2)

# 방법 3)
list_3rd.clear()
for n in range(3, 1000+1, 3):
    list_3rd.append(n)
# print(list_3rd)

# 방법 4)
# print([3 * x for x in range(1, 333+1)])
# 설명용
# print([2 * x for x in range(1, 10+1)]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# 방법 5)
# print([x for x in range(1, 1000+1) if x % 3 == 0]) # for문 if문 전부 처리


# zip 과 유사
# 예시 1)
print([(x, y) for x in ['광어', '고등어', '참치'] for y in ['1마리', '2마리', '3마리']])
# [('광어', '1마리'), ('광어', '2마리'), ('광어', '3마리'), ('고등어', '1마리'), ('고등어', '2마리'), ('고등어', '3마리'), ('참치', '1마리'), ('참치', '2마리'), ('참치', '3마리')] 

l1 = []
for x in ['광어', '고등어', '참치']:
    for y in ['1마리', '2마리', '3마리']:
        l1.append((x, y))
# print(l1) # 위랑 같은 결과


# 예시 2)
print([x for x in range(10+1) if x < 5 if x % 2 == 0]) # [0, 2, 4]

l2 = []
for x in range(10+1):
    if x < 5:
        if x % 2 == 0:
            l2.append(x)
print(l2) # 위랑 같은 결과


# 예시 3)
print(tuple([x * 2 for x in range(1,6)])) # (2, 4, 6, 8, 10)
print(tuple((x * 2 for x in range(1,6)))) # (2, 4, 6, 8, 10)
