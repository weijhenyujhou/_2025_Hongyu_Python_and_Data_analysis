#pip install pyqt6
import sys
from PyQt6 import QtWidgets  # 匯入 PyQt6 套件

# x = float(input('請輸入轉換數值'))
# s = input('模式確認：單位轉換(Ｏ/M)')
#
# r = Ozexchange(x,s)
# r.result()


# 1. 創建一個應用程式物件 (必須的，負責管理 GUI 事件迴圈)
app = QtWidgets.QApplication(sys.argv)

# 2. 創建一個主視窗 (QWidget 是一個基本的視窗元件)
widget = QtWidgets.QWidget()

# 3. 設定視窗標題
widget.setWindowTitle("Hello Qt6")
grid = QtWidgets.QGridLayout(widget)
#先列後欄

# # 4. 設定視窗大小 (寬 400, 高 300)
# widget.resize(400, 300)

# 5. 建立一個標籤 (Label) 並將其放在主視窗中
label1 = QtWidgets.QLabel(widget)
label1.setText('輸入轉換金額')  # 設定標籤的文字內容
# label.move(30,30)


# label2 = QtWidgets.QLabel(widget)
# label2.setText('PIOUY')  # 設定標籤的文字內容
# # label.move(30,50)
#
#
# label3 = QtWidgets.QLabel(widget)
# label3.setText('Hit before')  # 設定標籤的文字內容

input1 = QtWidgets.QLineEdit(widget)
# input1.move(60,30)

text1 = QtWidgets.QTextEdit(widget)
showlabel = QtWidgets.QLabel(widget)

def oztoml():
    try:
        x = float(input1.text())
        result = str(round(x * 29.75, 2))
        showlabel.setText(f'{result}ml') #settex 只能以str顯示所以計算完需要轉換成str
    except ValueError:
        showlabel.setText("請輸入有效數值！")


def mltooz():
    try:
        x = float(input1.text())
        result = str(round(x / 29.75, 2))
        showlabel.setText(f'{result}Oz') #settex 只能以str顯示所以計算完需要轉換成str
    except ValueError:
        showlabel.setText("請輸入有效數值！")


button = QtWidgets.QPushButton("Oz to ml", widget)
button.clicked.connect(oztoml)
button2 = QtWidgets.QPushButton("ml to Oz", widget)
button2.clicked.connect(mltooz)


#順序位置（行,欄)
grid.addWidget(label1,0,0) #第一行第一列
# grid.addWidget(label2,1,0) #第二行第一列
grid.addWidget(input1,0,1)
grid.addWidget(text1,1,1)
grid.addWidget(button,2,0)
grid.addWidget(showlabel,2,1)
# grid.addWidget(label3,2,2)
grid.addWidget(button2,3,0)


# 6. 顯示主視窗
widget.show()

# 7. 啟動應用程式事件迴圈，並在程式結束時正常退出
sys.exit(app.exec())

#打包軟體