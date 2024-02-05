# file : test36_pyqt.py
# desc : PyQt5 기본화면 만들기
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QFont
## GUI : Graphic User interface / CLI : Command Line interface
from PyQt5.QtWidgets import QApplication, QWidget
#print(sys.argv) # 현재 Python 파일의 경로 표시

class qtwin_exam(QWidget): #QWidget을 상속받을거야. QWidget이 가진 모든것을 사용할 수 있다
    #생성자
    def __init__(self) -> None:
        super().__init__()
        self.initUI() #화면 초기화 함수를 호출

    def initUI(self):
        self.setGeometry((1920-400)//2, (1080-300)//2, 400, 300) #x, y, widtg, height
        self.setWindowTitle('Qt5 Hello world!')
        self.text = ' '
        self.show()
    def drawText(self, event, paint):
        paint.setPen(QColor(10, 10, 10))  #dark gray / r0,g0,b0 -> black / r255, g255, b255 -> white
        paint.setFont(QFont('NanumGothic',15))
        paint.drawText((400-100)//2, 300//2, 'HELL WORLD!')
        paint.drawText(event.rect(), Qt.AlignLeft, self.text)  # AlignLeft, A;lignCenter, AlignRight

    def paintEvent(self, event) -> None:   #재정의(Override)
        paint = QPainter()
        paint.begin(self)
        self.drawText(event, paint)
        paint.end() #닫는다


loop = QApplication(sys.argv) #내 소스 위치로 App을 생성할거야
isinstance =qtwin_exam() #QWidget을 qtwin_exam 상속한 객체를 생성
loop.exec_()
