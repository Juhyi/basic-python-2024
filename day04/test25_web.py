# file : test25_wed.py
# desc : urllib 모듈 사용법

#from urllib.request import  # request 모듈안의 모든 내용 다 사용할 
# from urllib.request import Request, urlopen  # Request 클래스와 urllib만 쓰겠다

# req = Request('https://www.naver.com/') # 네이버 웹주소(url)
# res = urlopen(req) #url주소로 웹사이트 열어달라고 요청

# print(f'응답 코드는 : {res.status}') #url로 요청된 웹사이트 응답 확인
# print(res.read())

# #urllib.request보다 성능이 조금 더 나은 모듈
# import requests

# res2 = requests.get('https://www.naver.com/')
# print(res2.status_code)
# print(res2.text)

# def get_url():
#     url = requests.get('https://www.naver.com/')

# url = get_url('google') 
# print(url) # www.google.com



        
# print(str.upper())

# def solution(s):
#     answer = ''
#     words = s.split(' ')
    
#     for word in words:
#         for i, s in enumerate(word):
#             if i % 2 == 0:
#                 answer += s.upper()
#             else :
#                 answer += s.lower()
                
#         answer += ' '
    
#     return answer[:-1]
        

str = input('영어 문자열을 입력하세요 > ')

def solution(str):    
    answer = ''
    arr = str.split(' ')
    print(f'문장의 단어 갯수는 {len(arr)}개 입니다')
    
    for i in range(0, len(arr)):
            if(i%2==0):
                answer += arr[i].upper()
            else:
                answer += arr[i].lower()
            answer += ' '
    answer = answer[:-1]
    return answer
print(solution(str))