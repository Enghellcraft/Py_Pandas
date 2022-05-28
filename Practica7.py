import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

datos = pd.read_csv('Salaries.csv', encoding='latin-1')
df = pd.DataFrame(datos)
df.head()
print(df)

#Calcula el mínimo, máximo y promedio de antigüedad.
total_anios = df['yrs.since.phd'] + df['yrs.service']
describe_antiguedad = total_anios.describe()
print(f'Los datos de anios de antiguedad son:\n {describe_antiguedad}')

#Construye el código necesario para emitir un gráfico que muestre los porcentajes de cada cargo:
df.groupby('rank')['rank'].size().plot(kind='pie',legend='Reverse',title='Porcentajes por Cargo',autopct='%0.2f %%',fontsize=6,labels=None,pctdistance=1.10)


#Genera el código de agrupamiento y agregación necesario para calcular: suma, media y desviación estándar, del salario, utilizando las funciones de numpy:
describe_salario = df['salary'].describe()
print(f'Los datos de salarios son:\n {describe_salario}')

plt.show()

