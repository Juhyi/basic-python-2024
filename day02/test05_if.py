# date : 2024-01-30
# desc : 흐름제어 - if문

## 조건이 참일때와 거짓일때로 나누어서 어떤 일을 처리하는 것 - if
## if 조건:  - 참인 조건
## else: - 거짓인 조건
## 입력 input()  -> 문자
 
print('정수를 입력하세요 >')
number = int(input())   # 입력함수 input() 문자로 된 입력값을 정수로 변경 -> int(input())

if number > 0:
    print('양수입니다.')
elif number == 0:
    print('0입니다.')
elif number < 0:
    print('음수입니다.')
else:   ##거짓인 조건
    print('정의할 수 없습니다.')