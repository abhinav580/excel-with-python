import xlrd 
  
# Give the location of the file 
loc = ("/home/abhi/Downloads/dsc.xlsx") 
x = 0  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
for i in range(1, 173):
    if sheet.cell_value(i,3)==1.0 and sheet.cell_value(i,4)==1.0 and sheet.cell_value(i,5)==1.0 and sheet.cell_value(i,6)==1.0 and sheet.cell_value(i,7)==1.0 and sheet.cell_value(i,8)==1.0:
        print(sheet.cell_value(i,1),end='\n')
        x=x+1
  
# Extracting number of rows 
print(x)
