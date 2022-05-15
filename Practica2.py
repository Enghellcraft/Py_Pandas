import pandas as pd

alumnos_notas = {"Seth": 0,"Thot": 0, "Maat": 0, "Hathor": 0, "Bastet": 0 }

for i in alumnos_notas:
    alumnos_notas[i] = int(input(f"Ingrese la nota del alumno {i}: "))

data = alumnos_notas
print(data)
df = pd.DataFrame(list(data.items()),index=[1, 2, 3, 4, 5], columns=["Alumnos","Notas"])

print(df)
print(f"La nota maxima es: \n{df.max()}")
print(f"La nota minima es: \n{df.min()}")
notas = df["Notas"]
print(f"El promedio de las notas es: {notas.median()}")
print(f"La desviacion standard de las notas es: {notas.std()}")
