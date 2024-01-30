# file : test12_dictionary.py
# desc : 복합 자료형 dietionary

##사전형 - key와 value쌍을 나열해 놓은 자료형
# {key : value, key : value, key : value, ... }
dict_movie = { 'name' : '어벤져스 엔드게임', 'type' : '히어로 무비',
                'year' : 2019, 'director' : ['안소니 루소', '조 루소'], 'productor' : 'diadia', 
                'cast' : ['아이언맨', '타노스', '헐크', '토르', '닥터스트레인지'] }   # key값은 '문자열' 
# 조회
print(dict_movie['name'])
print(dict_movie['year'])
#추가, 수정
dict_movie['year'] = 2020
print(dict_movie)

dict_movie['productor'] = '케빈 파이기'
print(dict_movie)
# key에 대한 값을 찾을때
if 'productor' in dict_movie:
    print(dict_movie['productor'])
else:
    print('제작자 없음')

musician = dict_movie.get('musician')  #get(key) : key가 존재하면 value 을 출력하지만 존재하지면 None // 오류(예외) 발생 X
print(musician)  
#print(dict_movie['musician])  // 오류(예외) 발생
print('반복문 출력==============================================================')
# 반복문으로 출력
for key in dict_movie:
    print(key,':', dict_movie[key])

print('반복문 출력 2==============================================================')
for key, value in dict_movie.items():
    print(key, ':', value)








