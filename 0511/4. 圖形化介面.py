#pip install pyqt6
import sys
from PyQt6 import QtWidgets  # 匯入 PyQt6 套件

# 1. 創建一個應用程式物件 (必須的，負責管理 GUI 事件迴圈)
app = QtWidgets.QApplication(sys.argv)

# 2. 創建一個主視窗 (QWidget 是一個基本的視窗元件)
widget = QtWidgets.QWidget()

# 3. 設定視窗標題
widget.setWindowTitle("Hello Qt6")
grid = QtWidgets.QGridLayout(widget)
#先列後欄

# 4. 設定視窗大小 (寬 400, 高 300)
widget.resize(400, 300)

# 5. 建立一個標籤 (Label) 並將其放在主視窗中
label1 = QtWidgets.QLabel(widget)
label1.setText('Test')  # 設定標籤的文字內容
# label.move(30,30)


label2 = QtWidgets.QLabel(widget)
label2.setText('PIOUY')  # 設定標籤的文字內容
# label.move(30,50)

input1 = QtWidgets.QLineEdit(widget)
# input1.move(60,30)

text1 = QtWidgets.QTextEdit(widget)
# text1.move(70,50)
button = QtWidgets.QPushButton("Hit me", widget)
button2 = QtWidgets.QRadioButton("Check", widget)


#順序位置（行,欄)
grid.addWidget(label1,0,0) #第一行第一列
grid.addWidget(label2,1,0) #第二行第一列
grid.addWidget(input1,0,1)
grid.addWidget(text1,1,1)
grid.addWidget(button,2,0)
grid.addWidget(button2,2,1)



# 6. 顯示主視窗
widget.show()

# 7. 啟動應用程式事件迴圈，並在程式結束時正常退出
sys.exit(app.exec())
