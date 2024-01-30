# date : 2024-01-30
# desc : 복합 자료형 - list
#s1 = 80
#s2 = 90
#s3 = 100
#s4 = 50 
#s5 = 60    #학생 수만큼 변수를 생성
# 총갯수 10(n) 면 인덱스의 마지막 값은 9(n-1)
# index = 0, 2, 3, 4, 5, 6, 7, 8, 9
# index =  -7, -6 >...-3, -2, -1

std = [ 80, 90, 100, 50, 60, 55, 77, 88, 99, 100]
# list 요소 접근
print(std[9])

list_1 = [265, 3.5, '문자열', True, [1, 2, 3, 4], (3, 4), std]
print(list_1)
print(list_1[5])

list_1[6] = '바꾼값'
print(list_1)

## list 연산
print(list_1[2:3+1])   # : 뒤의 수는 출력하고 싶은 인덱스 + 1 이 필수!
## 마이너스 인덱스
print(list_1[-5:-3])  # : 뒤의 수는 출력하고 싶은 인덱스 + 1 이 필수!
## 이중 리스트
print(list_1[4][2])  #[1, 2, 3, 4] 중 3만 가져오기

list_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_2[1][2]) # 6

list_4 = [1, 2, 3]
list_5 = [7, 8, 9]
## list 연산 +, *만 사용 가능
print(list_4 + list_5) # + : list 연결
print(list_5 * 2)   # * : list 반복

##리스트 길이
print(len(list_4))

## append() : list 마지막에 하나 추가
## insert(index, val) : list의 index 이후에 val를 추가
print(list_1)
list_1.append('hello')
print(list_1)

list_1.insert(2, [1, 2, 3]) # 2번째 인덱스에 값을 추가 (원래값을  뒤로 밀림)
print(list_1)

## extend() : 기존 list 확장 , + 연산과 거의 유사// + 연산과 다르게 변수 생성 필요 X
list_4.extend(list_5)
print(list_4)
print(list_5)

## list 삭제
del list_4[3:5] # list의 인덱스의 값을 삭제
del list_4[3] 
print(list_4)
del list_4  # list 자체를 삭제
#print(list_4)

val = list_5.pop()
print(val)  # 9
print(list_5)   # [7, 8]

print(std)
val = std.pop(2)
print(val)
print(std)

# clear() : list 내용만 삭제 // del()은 완전히 삭제 -> print도 안됨
list_5.clear()
print(list_5)

# sort()
print(list_1)
#list_1.sort() # 문자열, 숫자, 불 섞여있는 리스트는 정렬안됨
std.sort() # 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not in
print(99 in std) # True
print(98 in std) # False   

# reverse(), copy(), count() ...
# *리스트 : 전개연산자 - 몰라도 될듯
list_a = [1 ,3 ,5]
list_b = [2, 4, 8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)









