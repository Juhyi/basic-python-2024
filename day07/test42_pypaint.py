# date : 2024-02-06
# file : test42_pypaint.py
# desc : 그림판

import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import *
from PyQt5.QtGui import QMouseEvent
from PyQt5.QtWidgets import QWidget,QApplication
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget

class winApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initUI() 
        self.initSignal()


    def initUI(self):       # 화면 초기화
        uic.loadUi('./day07/pyPaint.ui', self)
        self.setWindowIcon(QIcon('./image/iot.png'))
        self.setWindowTitle('Drawing Painting')
        # 캔버스 초기화
        self.brushColor = Qt.black
        self.canvas = QPixmap(self.lb_canvas.width(), self.lb_canvas.height())
        self.canvas.fill(QColor('White'))
        self.lb_canvas.setPixmap(self.canvas)

        self.btn_black.setStyleSheet('background:black;')
        self.btn_red.setStyleSheet('background:red;')
        self.btn_blue.setStyleSheet('background:blue;')


        self.show()
        self.setCenter()

    def initSignal(self):   # 동작 초기화
        self.btn_black.clicked.connect(self.btnBlackClicked)
        self.btn_blue.clicked.connect(self.btnBlueClicked)
        self.btn_red.clicked.connect(self.btnRedClicked)
        self.btn_clear.clicked.connect(self.btnClearClicked)
        # 이미지로드 및 저장버튼 추가
        self.btn_load.clicked.connect(self.btnLoadClicked)
        self.btn_save.clicked.connect(self.btnSaveClicked)


    def btnLoadClicked(self):
        image = QFileDialog.getOpenFileName(None, '이미지로드', '', 'Image file(*.jpg;*.png)')
        imagePath = image[0]
        # print(imagePath)
        pixmap = QPixmap(imagePath).scaledToWidth(381) # 파일 경로에 있는 이미지를 읽어서 pixmap 객체에 담기
        self.lb_canvas.setPixmap(pixmap)
        self.lb_canvas.adjustSize() #이미지를 라벨크기에 맞추기
    
        
    def btnSaveClicked(self):
        filePath,_ =QFileDialog.getSaveFileName(self,'이미지 저장', '', 'Image file(*.jpg;*.png)')
        if filePath == '': return
        pixmap = self.lb_canvas.pixmap()
        pixmap.save(filePath)

    def buttonClicked(self):    # black, ree, blue를 다 통일한 함수
        btn_val = self.sender().objectName()
        print(btn_val)
        if btn_val == 'btn_black':  # 검은버튼 클릭
            self.brushColor = Qt.black
        elif btn_val == 'btn_red':  # 빨간버튼 클릭
            self.brushColor = Qt.red
        elif btn_val == 'btn_blue': # 파란버튼 클릭
            self.brushColor = Qt.blue
        elif btn_val == 'btn_clear' :  #클리어
            self.canvas.fill(QColor('white'))
            self.lb_canvas.setPixmap
            

        

    def btnBlackClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_black
        print(btn_val)
        self.brushColor= Qt.black

    def btnBlueClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_blue
        print(btn_val)
        self.brushColor= Qt.blue


    def btnRedClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_red
        print(btn_val)    
        self.brushColor= Qt.red

    def btnClearClicked(self):
        btn_val = self.sender().objectName() # self.sender() btn_red
        print(btn_val)    # btn_clear
        self.canvas.fill(QColor('White'))
        self.lb_canvas.setPixmap(self.canvas)

    def mouseMoveEvent(self, e) -> None:
        print(e.x(), e.y())
        brush = QPainter(self.lb_canvas.pixmap())   # 
        brush.setPen(QPen(self.brushColor, 5, Qt.SolidLine, Qt.RoundCap))
        brush.drawPoint(e.x(), e.y())
        brush.end()
        self.update()   # 화면 업데이트

    def setCenter(self): #윈도우 앱을 화면에 정중앙에 위치  
        gm = self.frameGeometry() #윈도우 앱 자신 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터의 정중앙 값
        gm.moveCenter(cp)
        self.move(gm.topLeft())
    
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    inst = winApp()
    sys.exit(app.exec_())