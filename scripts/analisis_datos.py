
# Importar librerías
import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo CSV
df = pd.read_csv("datos/ventas.csv")

# Calcular total de ventas
ventas_totales = (df["cantidad"] * df["precio"]).sum()

# Mostrar resultado
print("Ventas totales:", ventas_totales)

# Agrupar ventas por producto
ventas_por_producto = df.groupby("producto")["cantidad"].sum()

# Generar gráfico
ventas_por_producto.plot(kind="bar")

# Guardar gráfico
plt.savefig("resultados/grafico_ventas.png")

# Guardar resumen
with open("resultados/resumen.txt", "w") as archivo:
    archivo.write(f"Ventas totales: {ventas_totales}")
