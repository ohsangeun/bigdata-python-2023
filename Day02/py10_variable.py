# 변수

a = 1
b = 'python'
c = [1, 2, 3]

print(id(a)) # 140737286365992 # 컴퓨터에 저장된 메모리 주소
print(id(b)) # 2026697741296
print(id(c)) # 2026697741888

a = b
print(id(a)) # 2962130424816
print(id(b)) # 2962130424816
# => 같은 메모리 주소에 저장됨

a = c
print(id(a)) # 1837029873216
print(id(c)) # 1837029873216
print(a is c) # True

from copy import copy
a = copy(c)
print(id(a)) # 1837031178688
print(id(c)) # 1837029873216
print(a is c) # False

a, b = ('python', 5)
print(a, b) # python 5

[c, d] = ['python', 7] # 잘 안씀
print(c, d) # python 7
