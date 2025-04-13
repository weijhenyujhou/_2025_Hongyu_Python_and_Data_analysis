import requests
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

title = ['行程名稱','價格']
ws.append(title)