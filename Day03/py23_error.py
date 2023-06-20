# 에러/예외 디버깅...

# 이거 왜 만든...? =============================================
def add(x, y):
    result = 0
    result = x + y
    return result
# 이거 왜 만든...? =============================================

def writeText(fname, text):
    try:
        f = open(fname, mode='w', encoding='utf-8')
        f.write(text)
        f.write('\n')
        f.close()
        print(f'{fname} 생성완료')
    except Exception as e:
        print(f'예외발생 {e}')
    finally: # 예외가 발생하든 안하든 무조건 실행
        print('파일생성 종료')


def divide(x, y):
    result = 0
    # 예외처리
    try:
        result = x / y
    except Exception as e:
        print(f'예외발생 {e}') # 예외발생 division by zero
    
    return result

# java 와 같은 엔트리포인트
if __name__ == '__main__':
    res = divide(7, 2)
    print(res)
    writeText(fname='', text='랄랄라') # 예외발생 [Errno 2] No such file or directory: ''