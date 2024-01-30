# file : test15_output.py
# desc : 콘솔 출력 포맷양식 String Format

string_1 = '{}'.format(10) # {} 위치에 함수 뒤에 들어있는 값을 치완, 원하는 양식으로 표현
print(type(string_1))

name = '이주희' #input('이름 입력 > ')
string_2 = '안녕하세요, {}입니다.'.format(name)
print(string_2)

string_3 = '{} {} {}'.format(4000,'만','빌려줘')
print(string_3)
#정수를 문자열 포맷
# = : 기호와 숫자를 분리, 0 : 공백에 0으로 채움, d : 정수 02d : 두자리 수 만들때 빈자리 0으로 채우기
string_4 = '______{:=+10d}________'.format(-100) 
print(string_4)
#실수 문자열 포맷 f (기본 소수점 6자리)
#7.2f : 전체 자리 수는 7, 소수점 뒤는 2자리 fix
val = 78.333333333
string_5 = '________{:7.2f}__________'.format(val)
print(string_5)

# python 3.6 이후에 도입. format() 함수를 사용안함
string_6 = f'_____{val:7.2f}______'
print(string_6)

string_7 = 'Hello~ world!'
print(string_7.upper()) #대문자로 변환
print(string_7.lower()) #소문자로 변환
print(string_7.lower().capitalize())

print(string_7.split(',')) #특정한 단어로 자르는 함수

string_8 = 'Hello, I am MG Sung. I am a lecturer. Good Luck for your day'
words = string_8.split(' ')
print(words)
print(f'문장의 단어 갯수는 {len(word)}개 입니다')

string_9 = 'A10'
print(string_9.isalnum()) #Frue
print(string_9.isnumeric()) # False A 얼퍼벳
string_10 = '10.5'          # 소수점은 함수를 만들어서 처리해야
print(string_10.isdecimal()) # False

print('안녕 ' in '안녕하세요') #문장안에 담겨있는지 확인