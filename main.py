import openpyxl

#path_winext: str = r"192.168.8.69\Users\foo.xlsx"
path_winext: str = r"Training.xlsx"
fileXLSX = openpyxl.load_workbook(path_winext)

sheet = fileXLSX["Tabellenblatt1"]

print(sheet['C8'].value)
sheet['A1'].value = 500
print(sheet['A1'].value)