import pandas as pd
import matplotlib.pyplot as plt

def csv_to_dataframe(path_archivo):
    data = pd.read_excel(path_archivo, index_col=0)
    print(data)
    data_frame = data.parse("autos")
    return data_frame

df = csv_to_dataframe("autos.xlsx")
print(df)

df.groupby('TIPO')['STOCK'].sum().plot(kind='barh',
legend='Reverse')
plt.xlabel('Stock')
plt.title('Concesionaria',
weight='bold',
size=10)
plt.show()
