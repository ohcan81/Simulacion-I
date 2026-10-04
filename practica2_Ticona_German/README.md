# Práctica Individual N° 2

## Análisis del tiempo de atención en cajas de un supermercado

### Descripción

Esta práctica consiste en formular y realizar un análisis preliminar de un sistema real simulado correspondiente a la atención de clientes en las cajas de un supermercado.

El objetivo es analizar el tiempo que tarda en ser atendido cada cliente en una caja, utilizando datos generados mediante Python.

### Variable principal

La variable principal de estudio es:

**Tiempo de servicio (minutos):** tiempo que tarda la atención de un cliente en la caja del supermercado.

### Datos

Se utilizan 30 observaciones correspondientes al tiempo de atención de 30 clientes.

Los datos se encuentran en:

`datos/supermercado_datos.xlsx`

### Tecnologías utilizadas

* Python
* NumPy
* Pandas
* OpenPyXL

### Estructura del proyecto

```text
Practica2_Supermercado/
│
├── datos/
│   └── supermercado_datos.xlsx
│
├── scripts/
│   └── analisis.py
│
├── reporte/
│   └── informe.txt
│
└── README.md
```

### Ejecución

Primero se generan los datos ejecutando:

```bash
python scripts/genera_datos.py
```

Posteriormente se ejecutará el script de análisis estadístico:

```bash
python scripts/analisis.py
```

### Análisis

El análisis contempla estadísticos descriptivos básicos y la detección de valores atípicos (outliers) mediante Z-Score.

Los resultados y la interpretación técnica se presentan en el archivo:

`reporte/informe.txt`
