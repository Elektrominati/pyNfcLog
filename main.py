import openpyxl

#path_winext: str = r"192.168.8.69\Users\foo.xlsx"
workbook_path: str = r"Training.xlsx"
workbook = openpyxl.load_workbook(workbook_path)

sheet = workbook["Tabellenblatt1"]

print(sheet['C8'].value)
sheet['A1'].value = 700
print(sheet['A1'].value)
workbook.save("Training.xlsx")
