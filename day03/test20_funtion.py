# file : test20_funtion.py
# desc : 함수 만들기

def add(x, y) -> int:
    result = x + y
    return result

def minus(x, y) -> int:
    result = x - y
    return result

def multi(x, y) -> int:
    result = x * y
    return result

def divide(x, y) -> float:
    result = x / y
    return result

def say_hello() -> None:
    print('Hello')
    #return None은 생략


say_hello()

print('더하기 -> ')
a, b = map(int, input('두 정수 입력 > ').split(' '))
결과 = add(a, b)  #리턴은 함수 결과값으로 바뀐다.
print(f'{a} + {b} = {결과}')
print(f'{a} - {b} = {minus(a, b)}')
print(f'{a} * {b} = {multi(a, b)}')
print(f'{a} ÷ {b} = {divide(a, b)}')




