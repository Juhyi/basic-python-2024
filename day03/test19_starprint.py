# file : test19_starprint.py
# desc : 뼐찍기 또는프라미디 ㅡ 만들기
## 1번 - 삼각형
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     # i가 1이면, range(1,2) 1번 반복
#     # i 가 2이면, range(1,3) 2번 반복
#     for j in range(1,i+1): #range() 값을 바꿔서 디버깅
#         print('*', end='') #엔터대신 empty로 변환
#     print() # 안쪽 for문이 끝나면 엔터

## 2번 - 역삼각형
# *****
# ****
# ***
# **
# *
# for i in range(1,6):
#     for j in range(1,7-i):
#         print('*', end= '')
#     print()

##3번 - 오른쪽으로 붙은 삼각형
#     *
#    **
#   ***
#  ****
# *****
for i in range (1,7):
    for j in range(6-i):
        print(' ', end='')
    for j in range(i):
        print('*', end = '')
    print()    
