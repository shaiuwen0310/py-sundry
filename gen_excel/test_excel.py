from openpyxl import Workbook
import datetime

datetime_dt = datetime.datetime.today()
datetime_str = datetime_dt.strftime("%Y%m%d_%H%M%S")

wb = Workbook()
ws = wb.active
ws.title = "sheet name"
ws['A1'], ws['B1'], ws['C1'] = 'number1', 'number2', 'number3'

try:
    # 可用loop去插值
    ws.append(["first", "second", "third"])
finally:
    # 在finally儲存檔案
    wb.save(datetime_str + '.xlsx')
