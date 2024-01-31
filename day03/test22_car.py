# file : test22_car.py
# desc : Car 클래스 만들기
from typing import Any


class Car:
    wheel_num= 4
    color = 'white'
    __palte_number = ''
    company = ''
    gear_type = ''

    #전진, 후진, 좌회전, 우회전
    def moveForward(self):
        print(f'{self.__palte_number}이 전진합니다.')

    def moveBackward(self):
        print(f'{self.__palte_number}이 후진합니다.')

    def moveLeft(self):
        print(f'{self.__palte_number}이 좌회전합니다.')

    def moveRight(self):
        print(f'{self.__palte_number}이 우회전합니다.')

    def __init__(self, __palte_number, company, color, gear_type) -> None:
        self.__palte_number = __palte_number
        self.company = company
        self.color = color
        self.gear_type = gear_type

    def __str__(self) -> str:   #print(객체) 출력되는 부분
        return f'제 차는 {self.__palte_number}입니다. {self.color}입니다.'
    
    def getPlateNumber(self): #외부에서는 접근할 수 없도록 막는 조치
        return self.__palte_number
    
    # def setPlateNumber(self ):

sarah = Car('54라 9538', '현대자동차', '흰색', '자동')
# 객체를 생성하는 곳과 객체를 사용하는 곳이 다를 수 있습니다.
print(sarah)
print(f'차 번호는 {sarah.getPlateNumber()}')
print(f'차 색상은 {sarah.color}')
sarah.moveForward()

sarah.__palte_number = '98하 7789' #악의적인 의도를 가지고 변경
print(sarah)


sarah.__palte_number = '99하 9999'  # 초보의 실수
print(sarah)
sarah.setPlateNumber

# csuv = Car('경남 88 1922', '기야자동차', '회색', '자동')
# print(f'차번호는 {csuv.palte_number}')