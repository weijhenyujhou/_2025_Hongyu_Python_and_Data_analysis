# pip install pyqt6
import sys
from PyQt6 import QtWidgets

def oztoml():
    try:
        x = float(input1.text())
        result = round(x * 29.75, 2)
        showlabel.setText(f"結果：{result} ml")
    except ValueError:
        showlabel.setText("❌ 請輸入有效數值！")

def mltooz():
    try:
        x = float(input1.text())
        result = round(x / 29.75, 2)
        showlabel.setText(f"結果：{result} Oz")
    except ValueError:
        showlabel.setText("❌ 請輸入有效數值！")

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.setWindowTitle("Oz ↔ ml 單位轉換器")
widget.resize(400, 300)

# 版面配置
grid = QtWidgets.QGridLayout(widget)

# 標籤 & 輸入欄位
label1 = QtWidgets.QLabel("請輸入數值：")
input1 = QtWidgets.QLineEdit()

# 顯示結果的 Label
showlabel = QtWidgets.QLabel("👉 結果將顯示在這裡")

# 兩個按鈕
button_oztoml = QtWidgets.QPushButton("Oz ➔ ml")
button_oztoml.clicked.connect(oztoml)

button_mltooz = QtWidgets.QPushButton("ml ➔ Oz")
button_mltooz.clicked.connect(mltooz)

# 元件擺放到 Grid Layout
grid.addWidget(label1, 0, 0)
grid.addWidget(input1, 0, 1)
grid.addWidget(button_oztoml, 1, 0)
grid.addWidget(button_mltooz, 1, 1)
grid.addWidget(showlabel, 2, 0, 1, 2)  # 跨兩欄置中

widget.show()
sys.exit(app.exec())