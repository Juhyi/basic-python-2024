# date : 2024-01-30
# desc : 홀수/짝수 구분

number = int(input('정수입력 > '))  # 입력받은 후 정수로 변경

if number % 5 ==0:  # 5의 배수
    print('5의 배수.')
else:               # 5의 배수가 아닌 나머지
    print('나머지 수.')