import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime

fig= plt.figure()
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
fig.set_size_inches(18,9)

datos = pd.read_csv('comercio_interno.csv', encoding='latin-1')

df = pd.DataFrame(datos)
#Muestro Columnas y filas
print(f"Muestro Columnas y Filas:\n {df.axes}")
#Muestro Cantidad de datos
print(f"Muestro Cantidad de Datos: \n{df.size}")
#Muestro Tipos de datos:
print(f"Muestro Tipos de Datos: \n{df.dtypes}")
#Muestro las Primeras 10 filas:
print(f"Muestro las 10 Primeras filas:\n {df.head(10)}")
#Muestro las Ultimas 10 filas:
print(f"Muestro las 10 Ultimas filas:\n {df.tail(10)}")
#Columna alcance_nombre ordenada alfabeticamente:
print(f"Columna alcance_nombre ordenada alfabeticamente: \n {df.sort_values('alcance_nombre')}")
alcance_nombre = pd.DataFrame(df,columns =['alcance_nombre'])
print(alcance_nombre.sort_values('alcance_nombre'))
#Actividad_producto_nombre que generó más valor:
max = df['valor'].max()
print(f"Actividad_producto_nombre que generó más valor:\n {df.loc[df['valor']==max,'actividad_producto_nombre']}")
#Sume por alcance_nombre los valores de los años 2009 al 2019:

#Muestre un gráfico de la actividad_producto_nombre agrupados en relación al valor 
df1 = df
df1.groupby('actividad_producto_nombre')['valor'].sum().plot(kind='pie',legend='Reverse',title='Montos por Actividades',autopct='%0.2f %%',fontsize=6,labels=None,pctdistance=1.10, ax=ax1) 

#Muestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019
df2 = df
df2 = df2.drop(df2[df2['alcance_nombre'] == 'Argentina'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'GRAN BUENOS AIRES'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'INDETERMINADA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'PARTIDOS DEL GBA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'RESTO DE BUENOS AIRES'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'BUENOS AIRES'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'CATAMARCA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'CORDOBA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'CORRIENTES'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'CHACO'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'CHUBUT'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'ENTRE RIOS'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'FORMOSA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'JUJUY'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'LA PAMPA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'LA RIOJA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'NEUQUEN'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'MISIONES'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'RIO NEGRO'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'SALTA'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'SAN JUAN'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'SAN LUIS'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'SANTA FE'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'SANTIAGO DEL ESTERO'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'TUCUMAN'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'SANTA CRUZ'].index)
df2 = df.drop(df2[df2['alcance_nombre'] == 'TIERRA DEL FUEGO'].index)
df2['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'], format='%d/%m/%Y')
df2['año'], df['mes'] = df2['indice_tiempo'].dt.year, df2['indice_tiempo'].dt.month
df2 = df2.drop(df2[df2['año'] < 2015].index)
df2.groupby('actividad_producto_nombre')['valor'].sum().plot(kind='pie',legend='Reverse',title='Montos por Actividades en Mendoza desde 2015',autopct='%0.2f %%',fontsize=6,labels=None,pctdistance=1.10, ax=ax2) 


df = df.drop(df[df['alcance_nombre'] == 'Argentina'].index)
df = df.drop(df[df['alcance_nombre'] == 'GRAN BUENOS AIRES'].index)
df = df.drop(df[df['alcance_nombre'] == 'INDETERMINADA'].index)
df = df.drop(df[df['alcance_nombre'] == 'PARTIDOS DEL GBA'].index)
df = df.drop(df[df['alcance_nombre'] == 'RESTO DE BUENOS AIRES'].index)
df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'], format='%d/%m/%Y')
df['año'], df['mes'] = df['indice_tiempo'].dt.year, df['indice_tiempo'].dt.month
df = df.drop(df[df['año'] < 2015].index)
del df['sector_id']
df.to_csv('comercio-interno-2.csv')
df.groupby('alcance_nombre')['valor'].sum().plot(kind='pie',legend='Reverse',title='Comercio interno por\nProvincias y CABA\nde 2015 a 2019',autopct='%0.2f %%',fontsize=6,labels=None,pctdistance=1.10,ax=ax3) 


plt.show()

