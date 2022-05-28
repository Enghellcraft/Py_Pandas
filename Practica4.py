import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 5))

def excel_to_dataframe(path_archivo):
    data = pd.read_excel(path_archivo, index_col=0)
    return data
def calcularPrecios():
    precios = pd.DataFrame(df, columns=["PRECIO"])
    print(precios.describe())
def agrupacionPorStock():
    stock = df.groupby('TIPO')['STOCK'].sum().plot(kind='barh',legend='Reverse')
    print(stock)
    
df = excel_to_dataframe("autos.xlsx")
print(df)
agrupacionPorStock()
calcularPrecios()

plt.xlabel('Stock')
plt.title('Concesionaria',weight='bold',size=10)
plt.show()


