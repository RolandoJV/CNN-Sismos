**Universidad de Oriente**

**Facultad de Ingeniería en Telecomunicaciones, Informática y Biomédica**

![](logo_udo.png)

**Diseño y evaluación de modelos de aprendizaje profundo para la clasificación binaria de señales sísmicas: experimentos con SeisTask y con características sísmicas complementarias**

<u>Integrantes:</u>

Alejandro Manuel Tamayo Morales

Francis Alejandro Liranza Liranza

Rolando Javier Vila Rodríguez

**CARRERA INGENIERÍA INFORMÁTICA**

**2026-2027**

# Resumen

La detección y clasificación automática de señales sísmicas constituye una tarea importante en el análisis de datos geofísicos, debido a la necesidad de identificar patrones asociados a eventos sísmicos y distinguirlos del ruido. En este trabajo se presentan tres etapas experimentales de carácter binario. La primera utiliza el conjunto de datos SeisTask, con señales semisintéticas equilibradas, sobre el que se entrenó una red neuronal convolucional unidimensional que alcanzó una exactitud del 87,53 % y un AUC de 0,9505 en el conjunto de prueba. La segunda etapa aborda un conjunto de 296 100 registros tabulares de ocho características con etiqueta de golpe o sin golpe, cuya depuración eliminó 237 922 duplicados y 60 registros ambiguos; sobre los 58 118 registros restantes, con una proporción de positivos del 0,51 %, se evaluaron cuatro modelos mediante validación cruzada estratificada de cinco pliegues. La regresión logística con pesos por clase obtuvo la mayor estabilidad, con una exhaustividad de 0,618 y un PR-AUC de 0,039 frente al valor de azar de 0,005. La tercera etapa, todavía en curso, plantea la clasificación de ventanas de cinco segundos de una traza sísmica real de la estación QMBU mediante una CNN unidimensional. Se discuten las limitaciones derivadas del desbalance de clases, la ausencia de etiquetas y el carácter binario de los datos disponibles.

**Palabras clave**: inteligencia artificial, redes neuronales convolucionales, señales sísmicas, clasificación binaria, aprendizaje profundo, datos desbalanceados.

# Summary

The automatic detection and classification of seismic signals is an important task in geophysical data analysis, due to the need to identify patterns associated with seismic events and distinguish them from noise. This work presents three binary experimental stages. The first uses the SeisTask dataset, composed of balanced semi-synthetic signals, on which a one-dimensional convolutional neural network was trained, reaching an accuracy of 87.53 % and an AUC of 0.9505 on the test set. The second stage addresses a dataset of 296,100 tabular records with eight features labeled as hit or no-hit; its cleaning removed 237,922 duplicates and 60 ambiguous records, and four models were evaluated on the remaining 58,118 records, with a positive rate of 0.51 %, using stratified five-fold cross-validation. Logistic regression with class weights proved the most stable, with a recall of 0.618 and a PR-AUC of 0.039 against a random baseline of 0.005. The third stage, still in progress, addresses the classification of five-second windows from a real seismic trace recorded at the QMBU station using a one-dimensional CNN. Limitations arising from class imbalance, the absence of labels, and the binary nature of the available data are discussed.

**Keywords**: artificial intelligence, convolutional neural networks, seismic signals, binary classification, deep learning, imbalanced data.

# Introducción

Los terremotos y otros fenómenos sísmicos generan señales que pueden ser registradas mediante estaciones de monitoreo y utilizadas para estudiar la actividad del subsuelo. El análisis de estas señales permite identificar características relevantes de los eventos registrados y contribuye al desarrollo de sistemas automáticos de detección y clasificación.

Sin embargo, el procesamiento manual de grandes volúmenes de datos sísmicos puede resultar complejo y requerir un esfuerzo considerable. Además, las señales de interés pueden presentar características similares a las del ruido, lo que dificulta su identificación mediante métodos tradicionales basados exclusivamente en reglas definidas previamente.

En este contexto, la inteligencia artificial ofrece herramientas que permiten aprender patrones directamente a partir de los datos. En particular, las redes neuronales convolucionales han demostrado utilidad en el procesamiento de señales y en tareas de reconocimiento de patrones, ya que pueden extraer características relevantes durante el entrenamiento.

El presente trabajo extiende el experimento inicial realizado con el conjunto de datos SeisTask y lo integra con dos material complementario: un conjunto tabular de características con etiquetas de golpe y sin golpe, y una traza sísmica continua registrada por la estación QMBU de la red cubana. El material se organiza en tres etapas experimentales de clasificación binaria, decisión que responde a las etiquetas efectivamente disponibles en los datos: los resultados y el material de cada etapa se describen con sus respectivas limitaciones.

El desarrollo de este sistema permitirá estudiar la aplicación de técnicas de aprendizaje profundo al análisis de señales sísmicas, así como identificar las dificultades y limitaciones que deben considerarse al construir modelos de clasificación automática con datos reales, desbalanceados y, en parte, sin etiquetas.

# Planteamiento del problema

El análisis automático de señales sísmicas constituye un desafío debido a la variabilidad de las señales registradas, la presencia de ruido y las semejanzas que pueden existir entre diferentes patrones. Estas características dificultan la identificación automática de los eventos y hacen necesario desarrollar métodos capaces de reconocer las propiedades relevantes de las señales.

A este desafío se suman problemas propios de los conjuntos de datos reales. En el material empleado en este trabajo, la clase de ruido supera ampliamente a la de eventos: existen 295 771 registros de ruido frente a 329 de golpe, una proporción cercana a 1:899. Un modelo que prediga siempre la clase mayoritaria alcanzaría una exactitud superior al 99 % sin haber aprendido nada. Además, el conjunto contiene una proporción elevada de duplicados exactos y algunos registros con etiquetas contradictorias, cuya presencia simultánea en los subconjuntos de entrenamiento y prueba produciría métricas artificialmente optimistas.

Las técnicas de aprendizaje profundo, particularmente las redes neuronales convolucionales (CNN), permiten aprender características a partir de los datos y utilizarlas para realizar tareas de clasificación. Sin embargo, su eficacia depende de factores como la calidad y representatividad del conjunto de datos, el preprocesamiento aplicado, la arquitectura seleccionada y los parámetros empleados durante el entrenamiento.

A partir de esta situación, se plantea la necesidad de diseñar y evaluar modelos de aprendizaje profundo capaces de clasificar señales y características sísmicas en dos categorías previamente definidas, utilizando métricas que permitan medir objetivamente su rendimiento incluso ante desbalance severo de clases.

**Problema científico:** ¿Cómo diseñar, entrenar y evaluar modelos de aprendizaje profundo para la clasificación binaria de señales y características sísmicas, tratando el desbalance de clases y la calidad de las etiquetas, y qué desempeño se obtiene en cada etapa del experimento?

# Justificación de la investigación

La realización de esta investigación se justifica por la importancia de explorar métodos de inteligencia artificial aplicados al procesamiento y análisis de señales sísmicas. La clasificación automática puede contribuir a reducir la intervención manual en el análisis de grandes volúmenes de datos y facilitar la identificación de patrones relevantes.

Desde el punto de vista científico y tecnológico, el trabajo permite estudiar la capacidad de las redes neuronales convolucionales para extraer características de señales temporales, así como el comportamiento de modelos de aprendizaje automático clásicos ante conjuntos de datos desbalanceados y con problemas de calidad, como duplicados y etiquetas contradictorias. Asimismo, posibilita analizar cómo influyen la depuración, la estrategia de balanceo y la métrica de evaluación en los resultados obtenidos.

Desde el punto de vista académico, el proyecto integra conocimientos de inteligencia artificial, aprendizaje profundo, procesamiento de señales y evaluación experimental de modelos. Además, proporciona una experiencia práctica en el desarrollo de un sistema de clasificación, desde la preparación de los datos hasta el análisis de los resultados.

Finalmente, la evaluación mediante métricas cuantitativas permitirá identificar las fortalezas y limitaciones del modelo, así como establecer posibles mejoras para trabajos futuros, incluida la ampliación a un catálogo de eventos que permita una clasificación con tres categorías.

# Objetivo general

Diseñar, entrenar y evaluar modelos de aprendizaje profundo para la clasificación binaria de señales y características sísmicas, en tres etapas experimentales, mediante el uso de conjuntos de datos etiquetados y métricas de evaluación apropiadas para datos desbalanceados.

# Objetivos específicos

1. Caracterizar y depurar los conjuntos de datos disponibles (SeisTask, el conjunto de características golpe/sin golpe y la traza de la estación QMBU), eliminando duplicados y registros ambiguos antes de cualquier división de los datos.
2. Realizar el preprocesamiento de los datos para garantizar un formato adecuado para el entrenamiento de los modelos.
3. Entrenar y evaluar un modelo de capas densas (MLP) sobre las características golpe/sin golpe, aplicando estrategias de balanceo y validación cruzada estratificada.
4. Diseñar la metodología de ventana de cinco segundos y la arquitectura de red neuronal convolucional unidimensional para la traza de la estación QMBU.
5. Evaluar los modelos con métricas apropiadas para datos desbalanceados (precisión, exhaustividad, F1 y PR-AUC), además de la exactitud y el AUC.
6. Analizar los resultados obtenidos, identificar las principales limitaciones del trabajo —incluida la ausencia de etiquetas para la traza real— y proponer posibles mejoras.

# Marco teórico

La inteligencia artificial (IA) es una rama de la informática orientada al desarrollo de sistemas capaces de realizar tareas como el reconocimiento de patrones, el aprendizaje y la toma de decisiones. Dentro de esta disciplina, el aprendizaje automático permite construir modelos que identifican relaciones a partir de los datos, sin necesidad de definir manualmente todas las reglas que deben seguir.

El aprendizaje profundo (*Deep Learning*) constituye una subárea del aprendizaje automático basada en redes neuronales artificiales con múltiples capas. Estas redes pueden aprender representaciones progresivamente más complejas de los datos durante el entrenamiento.

En el análisis de señales sísmicas, el aprendizaje profundo permite estudiar patrones temporales y características de las formas de onda que pueden resultar útiles para diferenciar distintos tipos de señales. Su desempeño depende de la calidad de los datos, de la arquitectura empleada y de la metodología de entrenamiento y evaluación.

Las redes neuronales convolucionales (*Convolutional Neural Networks*, CNN) son modelos de aprendizaje profundo que emplean operaciones de convolución para extraer características relevantes de los datos. Las redes convolucionales unidimensionales, conocidas como Conv1D, aplican filtros sobre secuencias de datos para reconocer patrones locales. En señales temporales, estos patrones pueden estar relacionados con cambios de amplitud, variaciones de la forma de onda y otras estructuras que ayudan a diferenciar las clases. Una CNN suele combinar capas convolucionales con operaciones de reducción dimensional, capas de agregación de características y capas densas que producen la salida del modelo.

En este trabajo se utiliza una CNN unidimensional en la etapa que trabaja con señales en el tiempo, porque las señales sísmicas están representadas como secuencias temporales. En cambio, cuando los datos ya están reducidos a un vector de características por ejemplo, como ocurre en el conjunto golpe/sin golpe, la arquitectura adecuada es una red de capas densas (*Multi-Layer Perceptron*, MLP), ya que no existe dimensión temporal sobre la cual aplicar convoluciones. Esta distinción condiciona el diseño de cada etapa del experimento.

Una señal sísmica es una representación temporal del movimiento del suelo registrado mediante instrumentos de medición, como los sismómetros. Estas señales pueden contener información asociada a terremotos y otros fenómenos, además de componentes de ruido procedentes del entorno, de los instrumentos o de otras fuentes. El ruido sísmico puede aparecer incluso cuando no existe un evento de interés claramente identificable, por lo que diferenciar el ruido de las señales que contienen eventos constituye una tarea relevante.

En el conjunto de datos empleado inicialmente en este trabajo se utilizan ejemplos de ruido puro y señales sintéticas que incorporan eventos sísmicos al ruido. Esta característica debe tenerse en cuenta al interpretar los resultados, ya que el desempeño obtenido con datos sintéticos no garantiza automáticamente el mismo comportamiento ante registros sísmicos reales.

La clasificación supervisada es una técnica de aprendizaje automático en la que el modelo se entrena utilizando ejemplos acompañados de sus etiquetas correspondientes. En la clasificación binaria existen dos categorías posibles, mientras que en la clasificación multiclase se consideran tres o más categorías. En este trabajo se adopta la clasificación binaria porque los datos disponibles solo sustentan dos categorías de manera verificable: ampliarlo a tres exigiría un catálogo de eventos que permita etiquetar las señales, cuestión que se analiza en la sección de limitaciones.

Para evaluar adecuadamente un modelo, los datos suelen dividirse en entrenamiento, validación y prueba. El conjunto de entrenamiento se utiliza para ajustar los parámetros de la red; el de validación permite supervisar el aprendizaje y detectar indicios de sobreajuste; y el de prueba se reserva para estimar el desempeño sobre ejemplos que no participaron en el ajuste. Cuando el conjunto de datos es pequeño en una de las clases, una única división produce estimaciones poco estables, por lo que se recurre a la validación cruzada: los datos se parten en *k* pliegues y cada pliegue actúa a su vez como conjunto de prueba, de modo que el resultado se expresa como media y desviación típica de las métricas.

Un problema de desbalance de clases ocurre cuando una categoría es mucho más frecuente que la otra. En estas situaciones la exactitud (*accuracy*) resulta engañosa, porque predecir siempre la clase mayoritaria produce una exactitud altísima sin ningún valor práctico. Se recurre entonces a otras métricas: la precisión (*precision*) mide qué proporción de las predicciones positivas son realmente positivas; la exhaustividad (*recall*) mide qué proporción de los positivos reales fueron detectados; y la puntuación F1 combina ambos mediante su media armónica. El área bajo la curva ROC (AUC) evalúa la capacidad de discriminación a través de distintos umbrales, mientras que el área bajo la curva precisión-exhaustividad (PR-AUC) resulta más informativa cuando los positivos son escasos, ya que su valor de referencia es la proporción de positivos del conjunto.

Para compensar el desbalance se emplean dos estrategias clásicas, aplicadas en este trabajo: los pesos por clase, que multiplican la pérdida de los ejemplos de la clase minoritaria durante el entrenamiento, y el submuestreo, que reduce aleatoriamente la clase mayoritaria hasta alcanzar una proporción dada. En ambos casos, el balanceo debe aplicarse únicamente a los datos de entrenamiento: si se modifica también el conjunto de prueba, las métricas dejan de reflejar la distribución real y dejan de ser comparables.

Por último, la depuración previa de los datos es un requisito metodológico. Los registros duplicados que aparecen a la vez en entrenamiento y prueba permiten al modelo "memorizar" respuestas que luego encuentra en la evaluación, inflando las métricas. De manera similar, un registro con características idénticas presentes en clases distintas es intrínsecamente ambiguo y debe eliminarse antes de dividir los datos.

# Trabajos relacionados

La aplicación de redes neuronales convolucionales al análisis de señales sísmicas ha sido estudiada en diversas investigaciones. Entre los recursos relevantes se encuentra STEAD (*STanford EArthquake Dataset*), presentado por Mousavi y colaboradores en 2019, que proporciona una amplia colección de registros sísmicos reales y señales de ruido para el desarrollo y la evaluación de modelos de aprendizaje automático.

En comparación con conjuntos de datos de gran escala como STEAD, el conjunto SeisTask utilizado en la primera etapa presenta características que facilitan el desarrollo de pruebas controladas: contiene 102 060 señales de tamaño fijo, organizadas en dos categorías, y permite trabajar con una estructura de datos uniforme. Estas características favorecen la preparación de los datos y el entrenamiento de modelos convolucionales en un entorno de recursos computacionales limitados.

El conjunto golpe/sin golpe empleado en la segunda etapa representa un tipo de material distinto: datos tabulares de características precalculadas, con un desbalance muy superior (1:899) y problemas de calidad ausentes en SeisTask, como duplicados exactos y etiquetas contradictorias. Este contraste permite estudiar, dentro del mismo trabajo, cómo el origen y la calidad de los datos condicionan la elección del modelo y la métrica.

El aporte de esta investigación consiste en diseñar, implementar y evaluar una CNN unidimensional y modelos de capas densas sobre conjuntos de datos específicos, así como en analizar sus resultados, limitaciones y posibilidades de mejora. No sería científicamente correcto concluir que un modelo supera a los de investigaciones anteriores basándose únicamente en la exactitud obtenida: para una comparación directa sería necesario utilizar los mismos datos de evaluación o conjuntos equivalentes, establecer categorías comparables y controlar las condiciones experimentales.

# Materiales y métodos

## Entorno de experimentación

Para la primera etapa se utilizó Google Colab como entorno de programación y ejecución de código Python, con NumPy para operaciones con matrices, pandas para la lectura de metadatos, h5py para acceder a los datos en formato HDF5 y TensorFlow con Keras para definir, entrenar y evaluar la red neuronal convolucional.

Las etapas 2 y 3 se desarrollaron en un entorno local de Python 3.13 con NumPy 2.5.4, pandas 3.0.6 y scikit-learn 1.9.1. Todo el proceso está automatizado en dos scripts versionados: `test.py`, que genera un perfil de cada archivo del conjunto de datos, y `entrenar_mlp.py`, que ejecuta la depuración, la validación cruzada y el cálculo de métricas de la segunda etapa. Se fijó la semilla 42 en todas las operaciones aleatorias para que los resultados sean reproducibles.

## Descripción de los conjuntos de datos

**SeisTask.** Conjunto de 102 060 señales semisintéticas publicado en Zenodo en 2026, con estructura (102 060, 2, 500): dos componentes y 500 muestras por ejemplo, equivalentes a intervalos de cinco segundos muestreados a 100 Hz. Para la primera etapa se utilizaron las etiquetas que diferencian ruido puro de señales con eventos sísmicos sintéticos.

**Conjunto golpe/sin golpe.** Dos archivos de texto sin encabezado, con ocho características numéricas por fila más la etiqueta binaria, separadas por espacios: `allhitexp.csv`, con 329 filas etiquetadas como golpe (1), y `nohitexp.csv`, con 295 771 filas etiquetadas como sin golpe (0). En total, 296 100 registros con una proporción de positivos del 0,11 % (1:899). Los archivos no incluyen nombres ni descripción de las ocho características, por lo que se trataron exclusivamente como variables numéricas sin interpretar.

La depuración, realizada antes de cualquier división de los datos, eliminó 237 922 filas duplicadas exactas (237 919 del archivo de ruido y 3 del de golpe) y 60 filas correspondientes a 30 vectores de características que aparecían simultáneamente con etiqueta 1 y 0 en los dos archivos, los cuales son ambiguos y se descartaron. El conjunto final quedó en 58 118 registros: 296 positivos y 57 822 negativos (0,51 % de positivos).

**Traza de la estación QMBU.** Archivo `CW.QMBU.00.HHE.D.2025.122` en formato miniSEED 2.x, correspondiente a la forma de onda continua del canal HHE (componente horizontal este) de la estación QMBU de la red CW, día 122 del año 2025 (2 de mayo de 2025). La cabecera indica 100 Hz de frecuencia de muestreo y compresión STEIM1; el archivo contiene 21 418 registros de 512 bytes con 412 muestras por registro. La exportación asociada (`categoria_sismos.csv`) declara 7 792 650 muestras en total, equivalentes a unas 21,6 horas de señal, de las cuales derivan aproximadamente 15 585 ventanas de cinco segundos sin solapamiento.

**Archivos de apoyo.** `sismos.csv` contiene seis eventos de 2023 en el oriente de Cuba (magnitudes entre 3,5 y 4,2); su procedencia está pendiente de confirmación con la fuente que lo facilitó, por lo que no se cita como referencia oficial y no se utiliza para etiquetar la traza, ya que ninguno de sus eventos corresponde al 2 de mayo de 2025. `sismos_en_tiempo_real.csv` reúne cuatro mediciones recientes de amplitud por estación, y `wilber-stations.txt` lista 149 estaciones de 11 redes que registraron un evento según el servicio Wilber de IRIS. El archivo `winequality-red.csv` (datos de vinos tintos de UCI) fue excluido por no tener relación con el proyecto.

## Etapa 1 — Clasificación con SeisTask (experimento inicial, ya realizado)

Se cargaron las señales y sus etiquetas, se reorganizaron las dimensiones a (102 060, 500, 2) para la capa Conv1D, se representaron en float32 y se dividieron de forma estratificada en 70 % entrenamiento, 15 % validación y 15 % prueba: 71 442, 15 309 y 15 309 ejemplos, respectivamente.

La arquitectura, definida con la API Sequential de Keras, se compone de una primera capa Conv1D con 32 filtros de tamaño 7 y activación ReLU; una capa MaxPooling1D; una segunda Conv1D con 64 filtros de tamaño 5 y activación ReLU; otra MaxPooling1D; una etapa GlobalAveragePooling1D; una capa densa de 64 neuronas con ReLU; una capa Dropout con tasa 0,3; y una neurona de salida con activación sigmoide para la clasificación binaria. El modelo posee aproximadamente 15 009 parámetros entrenables. El entrenamiento utilizó el optimizador Adam, la función de pérdida binary_crossentropy, las métricas exactitud y AUC, un máximo de 20 épocas, tamaño de lote 64, EarlyStopping con paciencia 4 sobre la pérdida de validación y ModelCheckpoint para conservar el mejor modelo en `mejor_cnn.keras`.

## Etapa 2 — Clasificación golpe/sin golpe con capas densas

Sobre el conjunto depurado (58 118 registros) se aplicó validación cruzada estratificada de cinco pliegues con semilla 42: cada pliegue entrena con el 80 % y evalúa en el 20 % restante, conservando la proporción natural de clases en la evaluación (unos 59 positivos por pliegue de prueba). La depuración y la división se realizaron en ese orden, de modo que ningún duplicado pueda caer a la vez en entrenamiento y prueba.

Se evaluaron cuatro modelos sobre los mismos pliegues: **A**, un MLP sin tratar el desbalance, como referencia; **B**, el mismo MLP con submuestreo aleatorio de la clase mayoritaria en proporción 1:10, aplicado solo a los datos de entrenamiento; **C**, una regresión logística con pesos por clase (`class_weight='balanced'`) sobre todo el entrenamiento, sin submuestrear; y **D**, el MLP submuestreado con el umbral de decisión ajustado al valor que maximiza F1 en una validación interna del 20 % del entrenamiento de cada pliegue, de manera que el pliegue de prueba no participa en ninguna decisión.

El MLP utiliza capas (64, 32) con activación ReLU, optimizador Adam, early stopping y un máximo de 400 iteraciones; la regresión logística emplea un máximo de 1 000 iteraciones. En ambos casos, el escalado de las características (StandardScaler) se ajustó únicamente con los datos de entrenamiento de cada pliegue. Se calcularon precisión, exhaustividad, F1, PR-AUC, ROC-AUC y exactitud, además de la matriz de confusión acumulada sobre los cinco pliegues, en la que cada fila aparece evaluada exactamente una vez.

## Etapa 3 — CNN unidimensional sobre ventanas de la traza QMBU (metodología, en curso)

La metodología prevista consiste en dividir la traza de la estación QMBU en ventanas de 500 muestras (cinco segundos a 100 Hz), compatibles con el formato empleado en SeisTask, normalizar cada ventana y entrenar una CNN unidimensional de arquitectura compacta análoga a la de la primera etapa, con salida sigmoide para clasificación binaria. El conjunto de ventanas se dividiría en entrenamiento, validación y prueba de forma estratificada, y la evaluación emplearía las mismas métricas de desbalance utilizadas en la etapa 2.

El punto crítico de esta etapa es la ausencia de etiquetas: el archivo `sismos.csv` no sirve para etiquetar la traza porque ninguno de sus seis eventos corresponde al 2 de mayo de 2025, y su procedencia además está por confirmar. Para obtener etiquetas verificables hace falta un catálogo de eventos del día del registro, por ejemplo del Centro Nacional de Sismología (CENAIS) o de un servicio FDSN, operación que queda pendiente. En consecuencia, esta etapa se presenta únicamente como metodología y trabajo en curso: no se reportan métricas, para no incluir cifras no obtenidas.

# Resultados experimentales

## Etapa 1 — SeisTask

Durante el entrenamiento se estableció un máximo de 20 épocas. La mejor configuración según la pérdida de validación se obtuvo en la época 19, con una pérdida de validación de 0,29483, una exactitud de validación de 87,55 % y un AUC de 0,9485. En la época 20 la pérdida de validación aumentó a aproximadamente 0,2974; debido a la recuperación de los mejores pesos, el modelo conservó los parámetros de la época con menor pérdida.

En la evaluación final, el modelo obtuvo una pérdida de 0,2887, una exactitud de 87,53 % y un AUC de 0,9505 sobre el conjunto de prueba de 15 309 señales. Por categoría, la clase 0 alcanzó una precisión de 0,89 y una exhaustividad de 0,86, mientras que la clase 1 obtuvo una precisión de 0,86 y una exhaustividad de 0,89, con puntuaciones F1 aproximadas de 0,87 y 0,88. Estos valores corresponden exclusivamente al experimento binario con SeisTask y no constituyen una evaluación de un clasificador de tres categorías.

## Etapa 2 — Conjunto golpe/sin golpe

La tabla 1 resume las métricas de los cuatro modelos como media y desviación típica sobre los cinco pliegues de la validación cruzada.

**Tabla 1.** Métricas de los modelos (media ± desviación típica, 5 pliegues).

| Modelo | Precisión | Exhaustividad | F1 | PR-AUC | ROC-AUC | Exactitud* |
|---|---|---|---|---|---|---|
| A. MLP sin tratar el desbalance | 0,000 ± 0,000 | 0,000 ± 0,000 | 0,000 ± 0,000 | 0,014 ± 0,003 | 0,658 ± 0,047 | 0,995 ± 0,000 |
| B. MLP con submuestreo 1:10 | 0,046 ± 0,049 | 0,027 ± 0,035 | 0,032 ± 0,040 | 0,021 ± 0,019 | 0,617 ± 0,200 | 0,993 ± 0,002 |
| C. Regresión logística con pesos por clase | 0,020 ± 0,003 | 0,618 ± 0,078 | 0,038 ± 0,005 | 0,039 ± 0,014 | 0,805 ± 0,042 | 0,842 ± 0,006 |
| D. MLP submuestreo + umbral max-F1 | 0,025 ± 0,025 | 0,308 ± 0,409 | 0,037 ± 0,032 | 0,027 ± 0,015 | 0,696 ± 0,166 | 0,782 ± 0,434 |

\* La exactitud no es válida como métrica principal: predecir siempre "ruido" produciría una exactitud de 0,995 sin detectar ningún evento.

La matriz de confusión acumulada (tabla 2) muestra el comportamiento concreto de cada modelo sobre los 58 118 registros, cada uno evaluado exactamente una vez.

**Tabla 2.** Matriz de confusión acumulada (filas: real; columnas: predicho).

| Modelo | VN | FP | FN | VP |
|---|---|---|---|---|
| A. MLP sin tratar el desbalance | 57 822 | 0 | 296 | 0 |
| B. MLP con submuestreo 1:10 | 57 725 | 97 | 288 | 8 |
| C. Regresión logística con pesos por clase | 48 738 | 9 084 | 113 | 183 |
| D. MLP submuestreo + umbral max-F1 | 45 335 | 12 487 | 205 | 91 |

El modelo A no predijo ni un solo positivo en ningún pliegue: su exactitud de 0,995 es exactamente la del clasificador que ignora la clase minoritaria. El modelo C detectó 183 de los 296 positivos (exhaustividad 0,618) a costa de 9 084 falsos positivos, y presentó la mayor estabilidad entre pliegues (desviación típica de F1 igual a 0,005). El umbral del modelo D, elegido en validación interna, promedió 0,353 con un rango de 0,020 a 0,544 entre pliegues, lo que indica que el punto óptimo de operación varía bastante según la muestra. El PR-AUC del modelo C, 0,039, es unas 7,8 veces el valor de azar (0,005, la proporción de positivos), y su ROC-AUC de 0,805 muestra que las características sí separan ambos razonablemente bien a nivel de ordenación, aunque el umbral y la dispersión limitan la precisión de las predicciones.

## Etapa 3 — Ventanas de la traza QMBU

No se reportan resultados: la etapa está en curso y su etiquetado depende de la obtención de un catálogo de eventos para el día de la traza, pendiente hasta el momento. La metodología completa se describió en la sección anterior.

# Discusión de los resultados

Los resultados de la primera etapa indican que la CNN unidimensional aprendió patrones útiles para diferenciar las dos categorías de SeisTask: una exactitud del 87,53 % y un AUC de 0,9505 sobre 15 309 señales de prueba, con puntuaciones F1 equilibradas entre categorías (0,87 y 0,88). Sin embargo, estos valores deben interpretarse considerando que SeisTask es un conjunto semisintético y equilibrado, y que la clasificación realizada es binaria: no permiten afirmar que el modelo distinga tres categorías ni que rinda igual sobre registros reales de otras estaciones.

Los resultados de la segunda etapa evidencian primero la importancia de tratar el desbalance. El modelo de referencia (A) alcanzó una exactitud aparentemente excelente (0,995) sin detectar un único positivo, ilustrando por qué la exactitud no sirve como métrica principal con un 0,51 % de positivos. Las estrategias de balanceo recuperaron capacidad de detección: los pesos por clase llevaron la exhaustividad de 0 a 0,618 con la menor variabilidad entre pliegues, mientras que el submuestreo y el umbral óptimo produjeron resultados muy variables (desviación típica del F1 igual o superior a su media), un comportamiento esperable con solo unos 236 positivos de entrenamiento por pliegue.

La precisión, en cambio, sigue siendo baja en todos los modelos (máximo 0,046): encontrar un positivo conlleva muchos falsos positivos. Que el ROC-AUC del modelo C llegue a 0,805 mientras su precisión a umbral 0,5 es de 0,020 sugiere que el problema no es solo el balanceo, sino también el punto de operación y la calidad de las ocho características, que carecen de documentación. Como mejora futura cabe estudiar el ajuste del umbral según el coste operativo de los falsos positivos, la selección o ingeniería de características y la incorporación de más ejemplos positivos.

La comparación entre etapas exige cautela: la etapa 1 y la etapa 2 trabajan sobre conjuntos de datos distintos (señales semisintéticas equilibradas frente a características tabulares desbalanceadas), con etiquetas y procedencias diferentes, por lo que sus métricas no son directamente comparables y no permite concluir que un modelo sea superior al otro.

En cuanto a la calidad de los datos, la depuración fue un paso obligatorio: sin eliminar los 237 922 duplicados, estos podrían haber aparecido simultáneamente en entrenamiento y prueba y haber inflado las métricas, y los 60 registros ambiguos habrían introducido ruido de etiqueta. La eliminación se realizó antes de dividir los datos, invirtiendo el orden que muchos procedimientos aplican por defecto.

Entre las limitaciones generales del trabajo destacan: el carácter binario de las clasificaciones realizadas, insuficiente para la clasificación de tres categorías originalmente prevista, lo que exige disponer de un catálogo de eventos que permita etiquetar señales reales; la ausencia de etiquetas en la traza QMBU, que deja la tercera etapa como metodología en curso; la procedencia no confirmada de `sismos.csv`; y la falta de documentación de las ocho características del conjunto golpe/sin golpe. Estas limitaciones no invalidan los resultados obtenidos, sino que delimitan su alcance y establecen las líneas de trabajo siguientes.

# Conclusiones

En este trabajo se presentaron tres etapas experimentales para la clasificación binaria de señales y características sísmicas mediante aprendizaje profundo.

En la primera etapa se entrenó una red neuronal convolucional unidimensional sobre SeisTask, que alcanzó una exactitud del 87,53 % y un AUC de 0,9505 en el conjunto de prueba, con puntuaciones F1 de 0,87 y 0,88 por categoría, demostrando la viabilidad de la arquitectura Conv1D para señales semisintéticas equilibradas.

En la segunda etapa se depuró el conjunto golpe/sin golpe (296 100 registros originales, 237 922 duplicados y 60 ambiguos eliminados, 58 118 finales) y se evaluaron cuatro modelos con validación cruzada estratificada de cinco pliegues. Los resultados confirman que, ante un desbalance del 0,51 % de positivos, la exactitud no es una métrica válida: el modelo sin tratamiento obtuvo 0,995 de exactitud detectando cero eventos. Los pesos por clase ofrecieron el mejor equilibrio entre detección y estabilidad (exhaustividad 0,618 ± 0,078, PR-AUC 0,039 frente a 0,005 de azar), aunque la precisión permanece baja y señala las ocho características como el eslabón a mejorar.

La tercera etapa, sobre ventanas de cinco segundos de la traza real de la estación QMBU, queda establecida como metodología y trabajo en curso: su avance depende de obtener un catálogo de eventos del día del registro que permita etiquetar las ventanas de forma verificable.

Como línea de trabajo futura se plantea completar el etiquetado de la traza real, ampliar el conjunto de ejemplos positivos, documentar e ingeniar las características y, con datos que sustenten tres categorías, extender los modelos a la clasificación multiclase prevista en el objetivo original.

# Referencias bibliográficas

1. Mousavi, S. M., Sheng, Y., Zhu, W., & Beroza, G. C. (2019). STanford EArthquake Dataset (STEAD): A Global Data Set of Seismic Signals for AI. IEEE Access, 7, 179464–179476. https://doi.org/10.1109/ACCESS.2019.2947848

2. Myren, S. (2026). SeisTask: A semi-synthetic, task-oriented, seismic time-series dataset for event detection [Conjunto de datos]. Zenodo. https://doi.org/10.5281/zenodo.18928724

3. TensorFlow. (s. f.). Conv1D layer. Documentación oficial de TensorFlow. https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv1D

4. Keras. (s. f.). EarlyStopping. Documentación oficial de Keras. https://keras.io/api/callbacks/early_stopping/

5. Keras. (s. f.). ModelCheckpoint. Documentación oficial de Keras. https://keras.io/api/callbacks/model_checkpoint/

6. Keras. (s. f.). Training with built-in methods. Guía oficial para el entrenamiento y la evaluación de modelos. https://keras.io/guides/training_with_built_in_methods/

7. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., Blondel, M., Prettenhofer, P., Weiss, R., Dubourg, V., Vanderplas, J., Passos, A., Cournapeau, D., Brucher, M., Perrot, M., & Duchesnay, É. (2011). Scikit-learn: Machine Learning in Python. Journal of Machine Learning Research, 12, 2825–2830.

8. [POR VERIFICAR antes de la entrega] Catálogo de eventos sísmicos del 2 de mayo de 2025 en Cuba (fuente CENAIS o servicio FDSN). Se incorporará con su cita completa en formato IEEE una vez confirmada la fuente, para el etiquetado de la etapa 3.

Nota: las referencias 1 a 7 corresponden a fuentes ya utilizadas y verificadas en el experimento inicial. La referencia 8 queda deliberadamente abierta: no se cita ninguna fuente de eventos que aún no haya sido confirmada.

# Anexos

**Anexo A. Scripts de reproducción.**

- `test.py`: perfilador del conjunto de datos (genera `resumen_dataset.md`).
- `entrenar_mlp.py`: depuración, validación cruzada y métricas de la etapa 2 (genera `resultados_etapa2.md`).
- Ambos se ejecutan con Python 3.13 desde la raíz del proyecto, sin parámetros obligatorios.

**Anexo B. Condiciones de ejecución de la etapa 2.**

- Python 3.13; scikit-learn 1.9.1; NumPy 2.5.4; pandas 3.0.6.
- Semilla 42 en la división, el submuestreo y los modelos.
- MLP: capas (64, 32), ReLU, Adam, early stopping, max_iter = 400, escalado con StandardScaler ajustado solo en entrenamiento.
- Regresión logística: `class_weight='balanced'`, max_iter = 1 000.
- Evaluación de los modelos A a C con umbral 0,5; el modelo D usa el umbral de F1 máximo en validación interna.

**Anexo C. Portada.** Insertar el logotipo de la universidad en la imagen de la portada (`logo_udo.png`), el mismo utilizado en `CNN1D.md`.

