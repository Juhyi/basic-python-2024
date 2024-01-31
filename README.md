# Python 기초 2024
부경대 2024 IoT 개발자과정 기초 프로그래밍 언어 - 파이썬

## 1일차
- 개발환경 구축
  - 코딩폰트 - 나눔고딕코딩
  - Notepad++ 설치
  - Python 설치
  - Visual Studio Code 설치
  - Git 설치
    - TortoisGit 설치
    - Github 가입
    - Github Desktop 설치

- Python 기초
  - Ptrhon 개발자는 귀도 반 로썸 
  - 콘솔 출력
  - 주석      
  - 변수
  - 자료형
  - 연산자

```Python
#이 부분은 주석입니다.
var01 = 10 # 정수, 실수, 불, 문자열 모두 가능
print(var01)
print(type(var01))

print( 5 + 4 / 2) # 7.0
print( 5 == 4 )  # False
```

## 2일차
- Python 기초
  - 흐름제어
    - if : 참/거짓으로 조건 분기 (다른 언어 swich)
    - for : 반복문 기본 (다른언어 foreach)
    - while : 반복문 변형 (다른언어 do ~ while)
  - 복합자료형 + 연산자(연산 함수)
    - list, tuple, dictionary
  - 출력 포맷
  - 구구단 + 디버깅

  ```Python
  # debugging
  # F5(디버그 시작), F10(한줄씩 실행), F11(함수안으로 진입), F9(중단점 토글)
  # Shift + F5 (디버깅 종료)
  print('구구단 시작!')
  for x in range(2, 9+1):   # 2부터 9까지 반복
      print(f'{x}단----->')
      for y in range(1,10): # 1부터 9까지 반복
          print(f'{x} X {y} = {x*y:2d}',end = '   ')  # end =  엔터대신 공백으로 변경
      print(' ') #안쪽 for문이 끝나면 마지막 엔터를 하나 추가
    ```

## 3일차
- Python 기초
  - 입력 방법
  - 별찍기
  - 함수
  - 객체지향

