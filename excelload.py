from openpyxl import Workbook
from openpyxl import load_workbook
from openpyxl.compat import range

wb = load_workbook(filename = 'CA-171222-PACO.xlsx')

mysheet = wb['Packing List']

print("Invoice 날짜를 입력하세요. ex)180110")
date = input()

mysheet['k4'] = 'CA-'+ date +'-PACO'
mysheet['o4'] = '=TEXT("' +'20' + date[:2] + '-' + date[2:4] + '-' + date[-2:] + '", "MMM D, YYYY")'

print("Vessel 명을 입력하세요. ex)SKY ORION 1717S")
vessel = input()
mysheet['e20'] = vessel

print("ETD를 입력하세요. ex)180115")
etd = input()
mysheet['e19'] = '=TEXT("' +'20' + etd[:2] + '-' + etd[2:4] + '-' + etd[-2:] + '", "MMM D, YYYY")'

print("ETA를 입력하세요. ex)180115")
eta = input()
mysheet['n19'] = '=TEXT("' +'20' + eta[:2] + '-' + eta[2:4] + '-' + eta[-2:] + '", "MMM D, YYYY")'



wb.save("CA-" + date + "-PACO.xlsx")
