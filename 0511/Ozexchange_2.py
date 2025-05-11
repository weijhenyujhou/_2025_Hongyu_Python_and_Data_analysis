import sys
from PyQt6 import QtWidgets


#  1oz = 29.573ml
#
# x = input('請輸入轉換的數字')
# s = input('單位是oz還是ml?(o/m)')
#
# if s=='o':
#     result = float(x) * 29.573
#     result = round(result,2)
#     print(f'您的換算結果為{x}oz約{result}ml')
# else:
#     result = float(x) / 29.573
#     result = round(result,2)
#     print(f'您的換算結果為{x}ml約{result}oz')
app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()
widget.setWindowTitle("Ozexchange")


#Label
label1 = QtWidgets.QLabel(widget)
label1.setText('輸入轉換金額')
label2 = QtWidgets.QLabel(widget)
label2.setText('選擇要轉換的單位')
#input

input1 = QtWidgets.QLineEdit(widget)
input2 = QtWidgets.QComboBox(widget)
input2.addItems(['o','m'])

#button
button = QtWidgets.QPushButton("exchange", widget)


#showlabel
showlabel = QtWidgets.QLabel(widget)

grid = QtWidgets.QGridLayout(widget)
grid.addWidget(label1,0,0)
grid.addWidget(input1,0,1)
grid.addWidget(label2,1,0)
grid.addWidget(input2,1,1)
grid.addWidget(button,2,1)
grid.addWidget(showlabel,3,0,1,2)

def oz():
    # s = input2.text()
    s = input2.currentText()
    x = int(input1.text())
    if s =='o':
        result = float(x) * 29.573
        result = str(round(result,2))
        print(f'您的換算結果為{x}oz約{result}ml')
        showlabel.setText(f'您的換算結果為:{x}oz約為：{result}ml')
    else:
        result = float(x) / 29.573
        result = str(round(result,2))
        print(f'您的換算結果為{x}ml約{result}oz')
        showlabel.setText(f'您的換算結果為:{x}ml約為：{result}oz')

button.clicked.connect(oz)

widget.show()

sys.exit(app.exec())