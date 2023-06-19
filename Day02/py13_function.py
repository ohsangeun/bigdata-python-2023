# 함수
'''
java 에서 함수의 형태
private int getMethods(int x, Object y){
    return result;
}
'''
# 함수선언 def 함수명(파라미터) [-> any] :

# def add(x, y):
#     result = x + y
#     return result

def add(x, y) -> any: # -> any => 리턴값을 any(뭐든지 가능)로 설정
    result = x + y
    return result

print(add(3, 5)) # 8
print(add('Hello ', 'World')) # Hello World # 리턴값이 any 기 때문에 문자열도 사용가능

def minus(x, y):
    return  x - y
print(minus(3, 5)) # -2

# 리턴값이 없는 함수
def plus(x, y) -> None: # 리턴값 없음(void) # -> None => 생략가능
    print(x + y)

plus(3, 5.4) # 8.4

print(None) # == NULL


# 다중 파라미터
'''
static void main(string[] args)
'''
def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add_many(1,2,3)) # 6
print(add_many(3,6,9,12,15,18,21)) # 84


# 키워드 매개변수 : 결과가 딕셔너리
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1) # {'a': 1}
print_kwargs(name = 'Hugo', age = 45) # {'name': 'Hugo', 'age': 45}


def print_kwargs(**kwargs):
    return kwargs

print(print_kwargs(a = 1)['a']) # 1
print(print_kwargs(name = 'Hugo', age = 45).get('name')) # Hugo


# 하나의 리턴값만 받을 때
def mult(x, y):
    return x * y

def div(x, y):
    return x / y

a = 10
b = 7
print(add(a, b))
print(minus(a, b))
print(mult(a, b))
print(div(a, b))

# 리턴값을 튜플로 처리하면 여러개를 리턴 받을 수 있음
def all_calc(x, y):
    return(x+y, x-y, x*y, x/y)

(res_add, res_min, res_mul, res_div) = all_calc(601, 45)


# 함수 기본값
def introduce_myself(name, age, man = True) -> None:
    print(f'나의 이름은 {name} 입니다')
    print(f'나이는 {age} 세 입니다')
    if man:
        print(f'나는 남자입니다')
    else:
        print(f'나는 여자입니다')

introduce_myself('유고', 45)
'''
나의 이름은 유고 입니다
나이는 45 세 입니다
나는 남자입니다
'''
introduce_myself('유고', 45, False)
'''
나의 이름은 유고 입니다
나이는 45 세 입니다
나는 여자입니다
'''

# 파라미터 순서 상관없이 입력 가능
introduce_myself(man=False, name='애슐리', age=24)
'''
나의 이름은 애슐리 입니다
나이는 24 세 입니다
나는 여자입니다
'''

# ---------------------------------------------------------------------------------

# 함수내의 변수는 지역변수
val = 1 # 전역변수
def valtest(val): # 지역변수
    val += 1
valtest(val)
print(val) # 1

# 함수내의 변수를 함수 밖으로 꺼내는 법
def valtest1(val): # 지역변수
    val += 1
    return val
res = valtest1(val)
print(val) # 1
print(res) # 2

# 또는... global
def valtest2():
    global val # 전역변수 val 을 함수내에서 잠시 갖다쓴다는 선언
    val += 10
valtest2()
print(val) # 11

# 되도록 지역변수, 전역변수 이름을 다르게 하자

# ---------------------------------------------------------------------------------

# lambda
'''
javascript jQuery 에서
$(document).ready = () => {}
>> = () => {} => << 이부분이 lambda 함수
'''
def adds(a, b):
    return a + b
# 위의 식을 lambda식으로 쓰면 아래와 같다
adds = lambda a, b: a + b

print(adds(6,7)) # 13

# ---------------------------------------------------------------------------------

# 내장함수

# abs() : 절대값
print(abs(-3)) # 3

# all(x)는 반복 가능한 데이터 x를 입력값으로 받으며 이 x의 요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴한다.
# 반복 가능한 데이터란 for 문에서 사용할 수 있는 자료형을 의미한다. 리스트, 튜플, 문자열, 딕셔너리, 집합 등이 있다.
print(all([1,2,3])) # True
print(all([1,2,0])) # False
print(all([1,5,2])) # True
print(all([])) # True
