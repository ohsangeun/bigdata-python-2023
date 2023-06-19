# 딕셔너리

iron_man = {'name' : 'Tony Stark',
            'address' : 'New york',
            'armer' : 'Repluse Arm'} # json 형식과 유사
print(iron_man) # {'name': 'Tony Stark', 'address': 'New york', 'armer': 'Repluse Arm'}

print(iron_man.get('name')) # Tony Stark
print(iron_man['name']) # Tony Stark

# (주의) key 중복시 값 덮어씌워짐
d1 = {1 : 'a', 1 : 'b'}
print(d1) # {1: 'b'}

# Value 중복 허용
d2 = {1 : 'test', 2 : 'test'}
print(d2) # {1: 'test', 2: 'test'}

# 딕셔너리 함수
print(iron_man.keys()) # dict_keys(['name', 'address', 'armer'])

for item in iron_man.keys() :
    print(item)
'''
(결과)
name
address
armer
'''

# values(), items() => 잘 안씀
print(iron_man.values()) # dict_values(['Tony Stark', 'New york', 'Repluse Arm'])
print(iron_man.items()) # dict_items([('name', 'Tony Stark'), ('address', 'New york'), ('armer', 'Repluse Arm')])
print(iron_man) # {'name': 'Tony Stark', 'address': 'New york', 'armer': 'Repluse Arm'}