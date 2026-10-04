import pandas as pd

# 1. CARGAR LOS DATOS

archivo = "datos/supermercado_datos.xlsx"

df = pd.read_excel(archivo, sheet_name="Datos")

# Obtener la columna que vamos a analizar

tiempos = df["tiempo_servicio_min"]

# CALCULAR ESTADÍSTICOS DESCRIPTIVOS

cantidad = len(tiempos)
media = tiempos.mean()
mediana = tiempos.median()
desviacion = tiempos.std()
minimo = tiempos.min()
maximo = tiempos.max()

# 3. CALCULAR Z-SCORE

z_score = (tiempos - media) / desviacion

df["z_score"] = z_score

# DETECTAR OUTLIERS

outliers = df[abs(df["z_score"]) > 3]

# MOSTRAR RESULTADOS

print(" ANÁLISIS DEL TIEMPO DE SERVICIO")

print(f"\nCantidad de datos: {cantidad}")
print(f"Media: {media:.2f} minutos")
print(f"Mediana: {mediana:.2f} minutos")
print(f"Desviación estándar: {desviacion:.2f} minutos")
print(f"Valor mínimo: {minimo:.2f} minutos")
print(f"Valor máximo: {maximo:.2f} minutos")


print(" VALORES ATÍPICOS - Z-SCORE")

print(f"\nCantidad de outliers: {len(outliers)}")

if len(outliers) > 0:
    print("\nOutliers encontrados:")
    print(outliers[["id_cliente", "tiempo_servicio_min", "z_score"]])
else:
    print("\nNo se encontraron valores atípicos.")