#python 顯示變數的方式
# %
'''
# % + s 表示顯示時後面要插入的數值型態
%s=str
%d=int(10進位Decimal）
%x=16進位
%o=8進位
%f=float (Python最初顯示方式）
'''
from itertools import count
from time import process_time_ns

a = 'Hello %s' # % + s 表示顯示時後面要插入的數值型態 s=str d=int(10進位Decimal） f=float (Python最初顯示方式）
b = 'Hello %d'
c = 'Hello %f'
d = 'Hello %x'

print(a % 'John')
print(b % 123)
print(c % 123.4)
print(d % 17)


e = '靠右對齊 Hello %+10s' # % + s 表示顯示時後面要插入的數值型態 s=str d=int(10進位Decimal） f=float (Python最初顯示方式）
f = 'Hello %d'
g = 'Hello %.3f'
h = 'Hello %x'

print(e % 'John')
#print(b % 123)
print(g % 123.456789)
#print(d % 17)

#字串插補法
# f '顯示文字'+{變數}
my_name = 999
print(f"Hello {my_name:*^10}")


#Practic
msg = "1.百分比_顯示_Hello %s ! 今日天氣溫度 %.2f"


print(msg %('John',23))

# format()
msg_1='Hello {:*^10s} ! 今日溫度 {:.1f}'
msg_2=('11的8進位{:o}, 及6進位{:x}')
print(msg_1.format('John',23))
print(msg_2.format(11,11))

msg_3 = '2.format方式 Hello {name:=^10s} ! 今日天氣溫度 {deg:.2f}'
print(msg_3.format(name ='John',deg=23))


# f-string
name = 'John'
deg =23
email = "adfg@gmail.com"
print(f'3.f-string方式 Hello {name:=^10s} ! 今日天氣溫度 {deg:.2f}')

# \ 跳脫字元 用途
#a = 'Hello "John"'
#a = "Hello 'John'"

#\n 換行 \t tab 空格定位

print(f'Hello\t{name:=^10s}!\ne-mail:\t{email}')
# 遇到需要顯示路徑的情況_有兩種解決方法
g = r"C:\user\name\python"

print(r"C:\user\name\python")
print("C:\\user\\name\\python")


#String index 字串索引值
s = 'helloworld!!'
#抓出第四個位置的字元(從0開始)
print(s[5])
#[起始位置:結束位置:間隔數字] 只能順向搜尋,無法反向搜尋
print(s[1:5]) # 顯示第二到第四個字元
print(s[::2])# 間隔兩個顯示
print(s[-5:])# 從倒數第五個字元開始顯示
print(s[:-1])# 起始未設定,# 倒數最後一個不顯示
print(s[-5:-1]) # 由字串後取得子字串，起始值終止值都要是負數，而起始值要比終止值小

# 定義字串變數
s = 'hello world'
print(f'String Method 舉例說明以下方法:{s}')
# len() - 取得字串長度
print('1. len() - 取得字串長度',len(s))  # 輸出: 5

# count() - 計算特定字元在字串中出現的次數
print('2. count() - 計算特定字元在字串中出現的次數',s.count("l"))  # 輸出: 2

# index() - 找出特定字元的索引位置（從0開始計算）找不到回報錯誤
print('3. index() - 找出特定字元的索引位置（從0開始計算）找不到回報錯誤',s.index("o"))  # 輸出: 4
# find() 找不到回傳-1
print('4. find() 找不到回傳-1',s.find("o"))

# isdigit() - 檢查字串是否只包含數字
print('5. isdigit() - 檢查字串是否只包含數字',s.isdigit())  # 輸出: False，因為 "hello" 不是數字

# isalpha() - 檢查字串是否只包含字母（不包含空格、數字或符號）
print('6. isalpha() - 檢查字串是否只包含字母（不包含空格、數字或符號）',s.isalpha())  # 輸出: True，因為 "hello" 只包含字母

# endswith() - 檢查字串是否以指定的字元結尾
print('7. endswith() - 檢查字串是否以指定的字元結尾',s.endswith("o"))  # 輸出: True，"hello" 以 "o" 結尾

# startswith() - 檢查字串是否以指定的字元開頭
print('8. startswith() - 檢查字串是否以指定的字元開頭',s.startswith("h"))  # 輸出: True，"hello" 以 "h" 開頭

# upper() - 將字串轉換成大寫
print(f'9. {s}經過upper()方法:\t',s.upper())  # 輸出: HELLO

# lower() - 將字串轉換成小寫
print(f'10. {s}經過lower()方法:\t',s.lower())  # 輸出: hello

#captialize() 句子第一個字大小
section= 'Captialize()方法'
print(f'{section:=^20s}')
print(f'{s}經過Capitalize()方法:\t',s.capitalize())
#title() 首字大寫
section= 'title()方法'
print(f'{section:=^20s}')
print(f'{s}經過title()方法:\t',s.title())

# replace() - 替換字串中的指定字元
section= 'replace()方法'
print(f'{section:=^20s}')
print(f'{s} 將過replace()方法將h改成g:\t',s.replace("h", "g"))  # 輸出: gello，將 "h" 替換為 "g"

#split()
section= 'Split()方法'
print(f'{section:=^20s}')

q =s.split('o')
print(type(s))
print(q)
print(type(q))
#strip() 刪除字串內不要的元素 EX:空格
section= 'strip()方法'
print(f'{section:=^20s}')
s3 = '    hell    '
print(s3.strip())
print(s3.lstrip())
print(s3.rsplit())