# Etapa 2 — Resultados: clasificacion hit/nohit con validacion cruzada

Generado por `entrenar_mlp.py` el 2026-10-12 22:12.

## Datos (depuracion previa)

- Originales: 296,100 filas (329 sismo / 295,771 ruido).
- Duplicados exactos eliminados: 237,922.
- Vectores ambiguos (etiqueta 1 y 0 a la vez): 30 (60 filas eliminadas).
- Dataset final: 58,118 filas (296 sismo / 57,822 ruido), 0.51 % de positivos.

## Metodologia

- Validacion cruzada estratificada de 5 pliegues (semilla 42): cada pliegue entrena con el 80 % y evalua en el 20 % restante, conservando la proporcion natural de clases.
- Submuestreo 1:10 aplicado SOLO a los datos de entrenamiento de los modelos B y D (el test de cada pliegue nunca se re muestrea).
- El umbral del modelo D se elige en una validacion interna (20 % estratificado del train de cada pliegue) maximizando F1: el pliegue de test no participa en ninguna decision.
- Referencia de azar: PR-AUC ~ 0.005 (proporcion de positivos); predecir siempre 'ruido' daria exactitud ~ 0.995.

## Resultados (media +/- desviacion tipica sobre 5 pliegues)

| Modelo | Precision | Recall | F1 | PR-AUC | ROC-AUC | Exactitud* |
|---|---|---|---|---|---|---|
| A. MLP sin tratar el desbalance (referencia) | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.000 ± 0.000 | 0.014 ± 0.003 | 0.658 ± 0.047 | 0.995 ± 0.000 |
| B. MLP con submuestreo 1:10 en train | 0.046 ± 0.049 | 0.027 ± 0.035 | 0.032 ± 0.040 | 0.021 ± 0.019 | 0.617 ± 0.200 | 0.993 ± 0.002 |
| C. Regresion logistica con pesos por clase (balanced) | 0.020 ± 0.003 | 0.618 ± 0.078 | 0.038 ± 0.005 | 0.039 ± 0.014 | 0.805 ± 0.042 | 0.842 ± 0.006 |
| D. MLP submuestreo 1:10 + umbral max-F1 | 0.025 ± 0.025 | 0.308 ± 0.409 | 0.037 ± 0.032 | 0.027 ± 0.015 | 0.696 ± 0.166 | 0.782 ± 0.434 |

\* La exactitud NO es valida como metrica principal aqui: predecir siempre 'ruido' rondaria 0.995.

## Umbrales de decision

- A. MLP sin tratar el desbalance (referencia): umbral 0.500 (fijo).
- B. MLP con submuestreo 1:10 en train: umbral 0.500 (fijo).
- C. Regresion logistica con pesos por clase (balanced): umbral 0.500 (fijo).
- D. MLP submuestreo 1:10 + umbral max-F1: media 0.353 (rango 0.020-0.544 entre pliegues).

## Matriz de confusion acumulada (cada fila evaluada exactamente una vez)

| Modelo | VN | FP | FN | VP |
|---|---|---|---|---|
| A. MLP sin tratar el desbalance (referencia) | 57,822 | 0 | 296 | 0 |
| B. MLP con submuestreo 1:10 en train | 57,725 | 97 | 288 | 8 |
| C. Regresion logistica con pesos por clase (balanced) | 48,738 | 9,084 | 113 | 183 |
| D. MLP submuestreo 1:10 + umbral max-F1 | 45,335 | 12,487 | 205 | 91 |

## Condiciones de la ejecucion

- scikit-learn 1.9.1, numpy 2.5.4, pandas 3.0.6, semilla 42.
- MLP: capas (64, 32), ReLU, Adam, early stopping, max_iter=400; StandardScaler ajustado solo en los datos de entrenamiento de cada pliegue.
- Regresion logistica: class_weight='balanced' (pesos por clase) sobre todo el train del pliegue, sin submuestrear.
- Evaluacion de las variantes A-C con umbral 0.5.
