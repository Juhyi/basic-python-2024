# file : test23_module.py
# desc : 모듈 사용

# import math

# PI = 3.141592
# radius = 5
# print(f'원의 크기는 {radius * radius * PI}')
# # print(math.pi)
# print(f'정확한 원의 크기는 {radius * radius *math.pi}')

# print(f'cos(0) = {math.cos(0)}')
# print(2 ** 10)
# print(math.pow(2, 10))
# print(math.ceil(3.1)) #올림
# print(math.floor(3.1)) #내림
# print(round(3.5)) # 반올림(너무 사용하닌깐 math에 없음. 기본함수)

# import math as m    # 별명짓기
# print(m.sin(0))

# from math import pi, pow  #조심해서 사용해야함

# print(pi)
# print(pow(2, 10))

# 5번 문제

def get_url(web_name):
    
    websites = {
        "google": "www.google.com",
        "naver":"www.naver.com",
        "daum":"www.instagram.net"
    }

    return websites.get(web_name)


web_name = input("영문 이름을 입력하세요 >  ")
    
    
url = get_url(web_name)
    
if url:
    print("웹사이트 주소는:", url) 
else:
    print("입력한 영문 이름에 해당하는 웹사이트가 없습니다.") 
   
   



    