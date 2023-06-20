# 연습문제 (179P)

# Q2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return print(result / len(args))

avg_numbers(1, 2)
avg_numbers(1, 2, 3, 4, 5)


# Q6
user_input = input('저장할 내용을 입력하세요 > ')
f = open('test.txt', 'a', encoding='utf-8')
f.write(user_input)
f.write('\n')
f.close()