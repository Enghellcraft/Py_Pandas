import pandas as pd


def csv_to_dataframe(path_archivo):
    data = pd.ExcelFile(path_archivo)
    print(data.sheet_names)
    data_frame = data.parse("Autos")
    return data_frame

df = csv_to_dataframe("E:\Mate3\Scrips_Python\Python_VSC\Py_Pandas\14.autos.xlsx")
print(df)