import pandas as pd

datos = { 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
df = pd.DataFrame(datos, index =['Enero', 'Febrero', 'Marzo', 'Abril'], columns = ["Ventas","Gastos"])
df ["Balance"] = df["Ventas"] - df["Gastos"]
print(df)