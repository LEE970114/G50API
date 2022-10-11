from openpyxl import load_workbook
import os
path = os.path.abspath('..')
excel_name = os.path.join(path,'data/g50test_data.xlsx')
class Open_Excel:
    def read_data(self,excel_path,sheet_name):
        Wb= load_workbook(excel_path)
        sh = Wb[sheet_name]
        data=list(sh.values)
        keys=data[0]
        all_data=[]
        for row in data[1:]:
            row_dict=dict(zip(keys,row))
            all_data.append(row_dict)
        Wb.close()
        return all_data
if __name__=="__main__":
    cases=Open_Excel(excel_name,"app_login").read_data()
    print(cases)








