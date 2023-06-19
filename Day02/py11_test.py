# 112p
# Q1
gildong = {'국어' : 80, '영어' : 75, '수학' : 55}
print(sum(gildong.values())/len(gildong))

# A1
sum = 0
for item in gildong.values() :
    sum += item
print(f'홍길동의 평균점수는 {sum/3} 입니다')

# Q2
print((13 % 2) == 0) # 짝수면 True

# Q3
pin = '881120-1068234'
yyyymmdd = pin.split('-')[0]
num = pin.split('-')[1]
print(yyyymmdd)
print(num)

# Q5
a = 'a:b:c:d'
b = a.replace(':', '#')
print(b)

# Q6
a = [1,3,5,4,2]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

# Q11
a = [1,1,1,2,2,3,3,3,4,4,5]
print(set(a))
b = list(set(a))
print(b)

# Q12
a = b = [1, 2, 3]
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 4, 3]