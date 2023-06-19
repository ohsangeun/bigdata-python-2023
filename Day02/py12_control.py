# 제어문
# 들여쓰기로 제어문, 함수, 클래스의 구역에 들어있는지 판별    

money = True
if (money == True):
    print('택시를 탑니다')
elif (money == False): # java else if()
    print('걸어갑니다')
else:
    print('XX')
print('여기 내립니다')

print(3 in [1, 2, 4, 5, 6, 7]) # False # 리스트 안에 3이 있는가
print(6 in [1, 2, 4, 5, 6, 7]) # True

# while (money == True):
    # print('무한루프')

for i in range(0, 10):
    print(i)

'''
0
1
2
3
4
5
6
7
8
9
'''

l1 = [1, 3, 5, 7, 9]
for i in l1:
    print(i)

'''
1
3
5
7
9
'''

print('홀수만 찍기')
for j in range(1, 10, 2):
    print(j)

'''
1
3
5
7
9
'''

print('구구단')
for x in range(2, 10): # 2단 ~ 9단
    for y in range(1, 10): # 1 ~ 9
        print(f'{x} X {y} = {x * y:2d}', end=' ') # 2d => 2줄 만들기 # end=' ' => 한 줄 띄우기 대신 공백으로 대체
    print('')

# 연습문제
result = 0
i = 1
while i <= 1000:
    if i % 3 == 0:
        result += i
        # print(i, end=" ")
    i += 1
print(result) # 166833

for i in range(1, 6):
    print('*' * i)
'''
*
**
***
****
*****
'''