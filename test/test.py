import openpyxl


workbook = openpyxl.load_workbook('./V2.xlsx')
worksheet = workbook.active
concatenated_values = []
for cell in worksheet['C'][1:]:
    concatenated_values.append(cell.value)
result = (','.join(str(value) for value in concatenated_values)).split(',')
int_numbers = [int(num) for num in result]
max_number = max(int_numbers) 
print(max_number)