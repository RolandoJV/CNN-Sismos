# Dataset del proyecto CNN-Sismos
Generado por `test.py` el 2026-10-12 21:29. Carpeta analizada: `D:\Programacion\Proyectos\CNN-Sismos\Dataset-20261012T210016Z-1-001\Dataset`. Archivos: 8.

## Inventario de archivos
| Archivo | Tamano |
|---|---|
| allhitexp.csv | 18.0 KB |
| categoria_sismos.csv | 2.3 KB |
| CW.QMBU.00.HHE.D.2025.122 | 10.5 MB |
| nohitexp.csv | 15.8 MB |
| sismos.csv | 314 B |
| sismos_en_tiempo_real.csv | 277 B |
| wilber-stations.txt | 14.8 KB |
| winequality-red.csv | 82.2 KB |

## allhitexp.csv
- **Que es:** Ejemplos 'con golpe' (sismo), etiqueta 1 en la ultima columna
- **Formato:** texto (valores separados por espacios en blanco, sin encabezado (matriz numerica))
- **Dimensiones:** 329 filas x 9 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 3
- **Rango por columna:** `col0` [-174 a 174], `col1` [-63 a 63], `col2` [0 a 22.19], `col3` [0 a 378.29], `col4` [0 a 2.169], `col5` [0 a 0.0943], `col6` [0 a 32.22], `col7` [0 a 4.99], `col8` [1 a 1]
- **Etiqueta (ultima columna, `col8`):** `1` -> 329 (100.0 %)
- **Primeras 3 filas de 329:**
| col0 | col1 | col2 | col3 | col4 | col5 | col6 | col7 | col8 |
|---|---|---|---|---|---|---|---|---|
| -174 | -15 | 9.99 | 8.12 | 0.0000 | 0.0000 | 0.36 | 0.22 | 1 |
| 174 | -21 | 9.14 | 9.11 | 0.1496 | 0.0000 | 0.54 | 0.68 | 1 |
| 138 | 21 | 0.44 | 0.00 | 0.0000 | 0.0000 | 0.39 | 0.48 | 1 |

## categoria_sismos.csv
- **Que es:** Exportacion CSV de la traza miniSEED (muestra parcial de la senal)
- **Formato:** texto (separador `,`, con encabezado)
- **Dimensiones:** 29 filas x 10 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 0
- **Primeras 3 filas de 29:**
| timestamp | amplitude | network | station | location | channel | starttime | sampling_rate | delta | npts |
|---|---|---|---|---|---|---|---|---|---|
| 1746144000.78 | 141 | CW | QMBU | 0 | HHE | 2025-05-02T00:00:00.780000Z | 100.0 | 0.01 | 7792650 |
| 1746144000.79 | 125 | CW | QMBU | 0 | HHE | 2025-05-02T00:00:00.780000Z | 100.0 | 0.01 | 7792650 |
| 1746144000.8 | 105 | CW | QMBU | 0 | HHE | 2025-05-02T00:00:00.780000Z | 100.0 | 0.01 | 7792650 |

## CW.QMBU.00.HHE.D.2025.122 -- traza sismica en miniSEED 2.x
- **Que es:** forma de onda continua de la estacion **QMBU** (red `CW`, canal `HHE`, ubicacion `00`). El nombre codifica `RED.ESTACION.UBICACION.CANAL.D.ANO.DIA`.
- **Primer registro:** 2025-05-02 00:00:00.7800 UTC | **Muestras/registro:** 412 | **Tasa:** 100 Hz
- **Compresion:** STEIM1 (blockette 1000)
- **Tamano:** 10,966,016 bytes = 21,418 registros de 512 bytes
- **Muestras totales (estimado, registros completos):** 8,824,216 (~24.5 h)
- **Nota:** la senal completa se lee con `obspy.read()`, no con pandas (miniSEED es un formato binario de sismologia).

## nohitexp.csv
- **Que es:** Ejemplos 'sin golpe' (ruido), etiqueta 0 en la ultima columna
- **Formato:** texto (valores separados por espacios en blanco, sin encabezado (matriz numerica))
- **Dimensiones:** 295,771 filas x 9 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 237,919
- **Rango por columna:** `col0` [-174 a 174], `col1` [-87 a 87], `col2` [0 a 27.24], `col3` [0 a 597.53], `col4` [0 a 2.1679], `col5` [0 a 0.1036], `col6` [0 a 39.4], `col7` [0 a 4.98], `col8` [0 a 0]
- **Etiqueta (ultima columna, `col8`):** `0` -> 295,771 (100.0 %)
- **Primeras 3 filas de 295,771:**
| col0 | col1 | col2 | col3 | col4 | col5 | col6 | col7 | col8 |
|---|---|---|---|---|---|---|---|---|
| -174 | 87 | 0.00 | 0.00 | 0.0000 | 0.0000 | 0.00 | 0.00 | 0 |
| -162 | 87 | 0.00 | 0.00 | 0.0000 | 0.0000 | 0.00 | 0.00 | 0 |
| -150 | 87 | 0.00 | 0.00 | 0.0000 | 0.0000 | 0.00 | 0.00 | 0 |

## sismos.csv
- **Que es:** Catalogo de sismos 2023 (fecha, hora, epicentro, magnitud, estacion)
- **Formato:** texto (separador `,`, con encabezado)
- **Dimensiones:** 6 filas x 7 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 0
- **Contenido completo (6 filas):**
| fecha | hora | latitud | longitud | profundidad | magnitud | estacion |
|---|---|---|---|---|---|---|
| 2023-01-15 | 03:12:45 | 19.75 | -75.17 | 10 | 3.8 | SAN |
| 2023-03-10 | 12:05:20 | 20.12 | -74.56 | 15 | 4.1 | GTB |
| 2023-05-02 | 18:20:03 | 19.8 | -76.0 | 12 | 3.5 | QMBU |
| 2023-06-25 | 21:10:15 | 20.45 | -75.9 | 8 | 4.2 | SCU |
| 2023-08-30 | 07:55:30 | 21.1 | -77.3 | 18 | 4.0 | STG |
| 2023-10-11 | 14:33:12 | 20.0 | -76.5 | 5 | 3.9 | BAY |

## sismos_en_tiempo_real.csv
- **Que es:** Mediciones recientes por estacion (amax, mean)
- **Formato:** texto (separador `,`, con encabezado)
- **Dimensiones:** 4 filas x 6 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 0
- **Contenido completo (4 filas):**
| Estación | Canal | amax | mean | Fecha | Hora |
|---|---|---|---|---|---|
| GTBY | CU 00 BHZ | 8.9671e-07 | 2.37871e-12 | 2025-04-29 | 15:08:00 |
| LTUN | CW 00 HHZ | 3.90922e-03 | 4.75831e-12 | 2025-04-29 | 15:10:00 |
| LMGC | CW 00 HHZ | 2.49191e-07 | 2.54919e-12 | 2025-04-29 | 15:11:00 |
| CAMR | CW 00 HHZ | 4.44162e-06 | 4.13226e-11 | 2025-04-29 | 15:14:00 |

## wilber-stations.txt
- **Que es:** Estaciones que registraron un evento (exportado de IRIS Wilber)
- **Formato:** texto (separador `|`, con encabezado)
- **Dimensiones:** 149 filas x 9 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 0
- **Distribucion de `Net`:** `AU` -> 1, `BK` -> 1, `CI` -> 1, `CU` -> 9, `GT` -> 2, `HK` -> 1, `IC` -> 10, `II` -> 42, `IM` -> 5, `IU` -> 76, `MS` -> 1
- **Primeras 3 filas de 149:**
| Station | Source | Net | Latitude | Longitude | Distance | Azimuth | Elevation | Station Name |
|---|---|---|---|---|---|---|---|---|
| TGUH | IRISDMC | CU | 14.057 | -87.273 | 3.596494287061428 | 83.45869760502413 | 1160 | Tegucigalpa, Honduras |
| JTS | IRISDMC | II | 10.2908 | -84.9525 | 6.777330010865902 | 119.29854077788632 | 340 | Las Juntas de Abangares, Costa Rica |
| TEIG | IRISDMC | IU | 20.2263 | -88.2763 | 7.034705739934851 | 20.994077865921096 | 40 | Tepich, Yucatan, Mexico |

## winequality-red.csv
- **Que es:** Dataset UCI de vinos tintos (sin relacion con los sismos)
- **Formato:** texto (separador `;`, con encabezado)
- **Dimensiones:** 1,599 filas x 12 columnas
- **Campos vacios:** 0
- **Filas duplicadas exactas:** 240
- **Distribucion de `quality`:** `3` -> 10, `4` -> 53, `5` -> 681, `6` -> 638, `7` -> 199, `8` -> 18
- **Primeras 3 filas de 1,599:**
| fixed acidity | volatile acidity | citric acid | residual sugar | chlorides | free sulfur dioxide | total sulfur dioxide | density | pH | sulphates | alcohol | quality |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 7.4 | 0.7 | 0 | 1.9 | 0.076 | 11 | 34 | 0.9978 | 3.51 | 0.56 | 9.4 | 5 |
| 7.8 | 0.88 | 0 | 2.6 | 0.098 | 25 | 67 | 0.9968 | 3.2 | 0.68 | 9.8 | 5 |
| 7.8 | 0.76 | 0.04 | 2.3 | 0.092 | 15 | 54 | 0.997 | 3.26 | 0.65 | 9.8 | 5 |

## Panorama general del dataset
- **Par de entrenamiento hit/nohit** (8 features + etiqueta): 296,100 ejemplos, 329 con sismo (etiqueta 1) vs 295,771 de ruido (etiqueta 0) -> desbalance ~1:899 (0.11 % positivos).
- **Traza sismica cruda** en miniSEED: QMBU a 100 Hz (red sismica cubana CW).
- **Estaciones que registraron un evento:** 149 (IU=76, II=42, IC=10, CU=9, IM=5, GT=2, CI=1, BK=1, AU=1, HK=1, MS=1).
- **winequality-red.csv** es el dataset de vinos tintos de UCI; no aporta nada al proyecto de sismos (parece restante de un tutorial).
- **sismos.csv**, **sismos_en_tiempo_real.csv** y **categoria_sismos.csv** son catalogos/consultas pequenos (decenas de filas), no datos de entrenamiento.
