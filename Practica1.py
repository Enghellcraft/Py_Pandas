import pandas as pd

año = 2015
ventas = []
for i in range(5):
    venta = int(input(f"Ingrese la venta del año {año}: "))
    ventas.append(venta)
    año = año + 1
data = { "Ventas" : ventas, "Sin Descuento" : ventas}
df = pd.DataFrame (data, index = [2015, 2016, 2017, 2018, 2019], columns = ["Ventas", "Sin Descuento"])
df ["Con Descuento"] = df["Sin Descuento"] * 0.9
print(df)