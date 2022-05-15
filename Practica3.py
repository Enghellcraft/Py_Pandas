import pandas as pd

def balance(dataframe):
    df ["Balance"] = df["Ventas"] - df["Gastos"]
    
datos = { 'Ventas':[30500, 35600, 28300, 33900], 'Gastos':[22000, 23400, 18100, 20700]}
df = pd.DataFrame(datos, index =['Enero', 'Febrero', 'Marzo', 'Abril'], columns = ["Ventas","Gastos"])
balance(df)
print(df)