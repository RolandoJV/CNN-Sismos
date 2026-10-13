**Universidad de Oriente**

**Facultad de Ingeniería en Telecomunicaciones, Informática y Biomédica**

![](data:image/png;base64...)

**Diseño y evaluación de una red neuronal convolucional unidimensional para la clasificación binaria de señales sísmicas utilizando el conjunto de datos SeisTask**

<u>Integrantes:</u>

Alejandro Manuel Tamayo Morales

Francis Alejandro Liranza Liranza

Rolando Javier Vila Rodríguez

**CARRERA INGENIERÍA INFORMÁTICA**

**2026-2027**

**Resumen**

La detección y clasificación automática de señales sísmicas constituye una tarea importante en el análisis de datos geofísicos, debido a la necesidad de identificar patrones asociados a diferentes tipos de eventos y distinguirlos de las señales de ruido. En este trabajo se propone el diseño y entrenamiento de una red neuronal convolucional (CNN) para la clasificación automática de señales sísmicas en tres categorías. La metodología contempla la selección y preparación de un conjunto de datos etiquetado, el preprocesamiento de las señales, el diseño de la arquitectura de la red neuronal y la evaluación de su desempeño mediante métricas de clasificación. Asimismo, se analizarán los resultados obtenidos para identificar las fortalezas y limitaciones del modelo propuesto.Finalmente, se valorará la utilidad de las redes neuronales convolucionales en el reconocimiento de patrones presentes en señales sísmicas.

**Palabras clave**: inteligencia artificial, redes neuronales convolucionales, señales sísmicas, clasificación multiclase, aprendizaje profundo.

**Summary**

The automatic detection and classification of seismic signals is a crucial task in geophysical data analysis, driven by the need to identify patterns associated with different types of events and distinguish them from noise. This study proposes the design and training of a convolutional neural network (CNN) for the automatic classification of seismic signals into three categories. The methodology encompasses the selection and preparation of a labeled dataset, signal preprocessing, the design of the neural network architecture, and performance evaluation using classification metrics. Additionally, the results will be analyzed to identify the strengths and limitations of the proposed model. Finally, the utility of convolutional neural networks for recognizing patterns in seismic signals will be assessed.

**Keywords**: artificial intelligence, convolutional neural networks, seismic signals, multi-class classification, deep learning.

**Introducción**

Los terremotos y otros fenómenos sísmicos generan señales que pueden ser registradas mediante estaciones de monitoreo y utilizadas para estudiar la actividad del subsuelo. El análisis de estas señales permite identificar características relevantes de los eventos registrados y contribuye al desarrollo de sistemas automáticos de detección y clasificación.

Sin embargo, el procesamiento manual de grandes volúmenes de datos sísmicos puede resultar complejo y requerir un esfuerzo considerable. Además, las señales de interés pueden presentar características similares a las del ruido, lo que dificulta su identificación mediante métodos tradicionales basados exclusivamente en reglas definidas previamente.

En este contexto, la inteligencia artificial ofrece herramientas que permiten aprender patrones directamente a partir de los datos. En particular, las redes neuronales convolucionales han demostrado utilidad en el procesamiento de señales y en tareas de reconocimiento de patrones, ya que pueden extraer características relevantes durante el entrenamiento.

El presente trabajo se centra en el diseño y entrenamiento de una red neuronal convolucional para clasificar señales sísmicas en tres categorías. Para ello, se estudiarán las características del conjunto de datos seleccionado, se establecerá una metodología de preprocesamiento y entrenamiento, y se evaluará el rendimiento del modelo mediante métricas apropiadas para problemas de clasificación multiclase.

El desarrollo de este sistema permitirá estudiar la aplicación de técnicas de aprendizaje profundo al análisis de señales sísmicas, así como identificar las dificultades y limitaciones que deben considerarse al construir modelos de clasificación automática.

**Planteamiento del problema**

El análisis automático de señales sísmicas constituye un desafío debido a la variabilidad de las señales registradas, la presencia de ruido y las semejanzas que pueden existir entre diferentes patrones. Estas características dificultan la identificación automática de los eventos y hacen necesario desarrollar métodos capaces de reconocer las propiedades relevantes de las señales.

Las técnicas de aprendizaje profundo, particularmente las redes neuronales convolucionales (CNN), permiten aprender características a partir de los datos y utilizarlas para realizar tareas de clasificación. Sin embargo, su eficacia depende de factores como la calidad y representatividad del conjunto de datos, el preprocesamiento aplicado, la arquitectura seleccionada y los parámetros empleados durante el entrenamiento.

A partir de esta situación, se plantea la necesidad de diseñar y evaluar un modelo de red neuronal convolucional capaz de clasificar señales sísmicas en tres categorías previamente definidas, utilizando un conjunto de datos etiquetado y métricas que permitan medir objetivamente su rendimiento.

**Problema científico:** ¿Cómo diseñar y entrenar una red neuronal convolucional que permita clasificar automáticamente señales sísmicas en tres categorías y evaluar su desempeño mediante métricas de clasificación?

Justificación de la investigación

La realización de esta investigación se justifica por la importancia de explorar métodos de inteligencia artificial aplicados al procesamiento y análisis de señales sísmicas. La clasificación automática puede contribuir a reducir la intervención manual en el análisis de grandes volúmenes de datos y facilitar la identificación de patrones relevantes.

Desde el punto de vista científico y tecnológico, el trabajo permite estudiar la capacidad de las redes neuronales convolucionales para extraer características de señales temporales y utilizarlas en una tarea de clasificación multiclase. Asimismo, posibilita analizar cómo influyen el preprocesamiento, la arquitectura de la red y los parámetros de entrenamiento en los resultados obtenidos.

Desde el punto de vista académico, el proyecto integra conocimientos de inteligencia artificial, aprendizaje profundo, procesamiento de señales y evaluación experimental de modelos. Además, proporciona una experiencia práctica en el desarrollo de un sistema de clasificación, desde la preparación de los datos hasta el análisis de los resultados.

Finalmente, la evaluación mediante métricas cuantitativas permitirá identificar las fortalezas y limitaciones del modelo, así como establecer posibles mejoras para trabajos futuros.

**Objetivo General**

Diseñar, entrenar y evaluar una red neuronal convolucional para la clasificación automática de señales sísmicas en tres categorías, mediante el uso de un conjunto de datos etiquetado y métricas de evaluación apropiadas.

**Objetivos específicos**

1. Seleccionar y caracterizar un conjunto de datos adecuado para la clasificación de señales sísmicas en tres categorías.
2. Realizar el preprocesamiento de los datos para garantizar un formato adecuado para el entrenamiento de la red neuronal.
3. Diseñar una arquitectura de red neuronal convolucional adaptada a las características temporales de las señales.
4. Entrenar el modelo utilizando un conjunto de datos de entrenamiento y supervisar su desempeño mediante un conjunto de validación.
5. Evaluar el modelo con datos de prueba independientes, utilizando métricas como exactitud, precisión, exhaustividad y puntuación F1.
6. Analizar los resultados obtenidos, identificar las principales limitaciones del modelo y proponer posibles mejoras.

**Marco teórico**

La inteligencia artificial (IA) es una rama de la informática orientada al desarrollo de sistemas capaces de realizar tareas que requieren capacidades como el reconocimiento de patrones, el aprendizaje y la toma de decisiones. Dentro de esta disciplina, el aprendizaje automático permite construir modelos que identifican relaciones a partir de los datos, sin necesidad de definir manualmente todas las reglas que deben seguir.

El aprendizaje profundo (*Deep Learning*) constituye una subárea del aprendizaje automático basada en redes neuronales artificiales con múltiples capas. Estas redes pueden aprender representaciones progresivamente más complejas de los datos durante el entrenamiento.

En el análisis de señales sísmicas, el aprendizaje profundo permite estudiar patrones temporales y características de las formas de onda que pueden resultar útiles para diferenciar distintos tipos de señales. Su desempeño depende de la calidad de los datos, de la arquitectura empleada y de la metodología de entrenamiento y evaluación.

Las redes neuronales convolucionales (*Convolutional Neural Networks*, CNN) son modelos de aprendizaje profundo que emplean operaciones de convolución para extraer características relevantes de los datos. Aunque se utilizan ampliamente en el procesamiento de imágenes, también existen variantes diseñadas para trabajar con señales unidimensionales.

Las redes convolucionales unidimensionales, conocidas como Conv1D, aplican filtros sobre secuencias de datos para reconocer patrones locales. En señales temporales, estos patrones pueden estar relacionados con cambios de amplitud, variaciones de la forma de onda y otras estructuras que ayudan a diferenciar las clases.

Una CNN suele combinar capas convolucionales con operaciones de reducción dimensional, capas de extracción o agregación de características y capas densas que producen la salida del modelo. Durante el entrenamiento, los parámetros de los filtros se ajustan para reducir el error entre las predicciones y las etiquetas reales.

En este trabajo se utiliza una CNN unidimensional porque las señales sísmicas están representadas como secuencias temporales. Esta arquitectura permite procesar las muestras de la señal y aprender características que posteriormente se utilizan para realizar la clasificación.

Una señal sísmica es una representación temporal del movimiento del suelo registrado mediante instrumentos de medición, como los sismómetros. Estas señales pueden contener información asociada a terremotos y otros fenómenos, además de componentes de ruido procedentes del entorno, de los instrumentos o de otras fuentes.

El ruido sísmico puede aparecer incluso cuando no existe un evento de interés claramente identificable. Por este motivo, diferenciar el ruido de las señales que contienen eventos sísmicos constituye una tarea relevante para el análisis automático de datos.

Las señales registradas pueden presentar diferencias de amplitud, duración, frecuencia y forma de onda. El aprendizaje automático puede aprovechar estas características para construir modelos que asignen una categoría a cada señal. Sin embargo, la capacidad de generalización depende de que los datos utilizados durante el entrenamiento representen adecuadamente las señales que el sistema encontrará posteriormente.

En el conjunto de datos empleado inicialmente en este trabajo, se utilizan ejemplos de ruido puro y señales sintéticas que incorporan eventos sísmicos al ruido. Esta característica debe tenerse en cuenta al interpretar los resultados, ya que el desempeño obtenido con datos sintéticos no garantiza automáticamente el mismo comportamiento ante registros sísmicos reales.

La clasificación supervisada es una técnica de aprendizaje automático en la que el modelo se entrena utilizando ejemplos acompañados de sus etiquetas correspondientes. Durante el entrenamiento, la red compara sus predicciones con las categorías conocidas y ajusta sus parámetros para reducir los errores.

En la clasificación binaria existen dos categorías posibles, mientras que en la clasificación multiclase se consideran tres o más categorías. La estructura de la capa de salida y la función de pérdida deben seleccionarse de acuerdo con el tipo de clasificación planteado.

En el experimento inicial de este trabajo se utiliza una clasificación binaria, en la que el modelo aprende a diferenciar entre ruido puro y señales que contienen un evento sísmico sintético. La posibilidad de incorporar otras categorías dependerá de las etiquetas disponibles en el conjunto de datos y de los objetivos definitivos del experimento.

Para evaluar adecuadamente un modelo de aprendizaje automático, los datos suelen dividirse en tres subconjuntos: entrenamiento, validación y prueba.

El conjunto de entrenamiento se utiliza para ajustar los parámetros de la red neuronal. El conjunto de validación permite supervisar el aprendizaje, comparar configuraciones y detectar posibles indicios de sobreajuste. Por último, el conjunto de prueba se utiliza para estimar el desempeño del modelo sobre ejemplos que no participaron en el ajuste de sus parámetros.

En este trabajo, los datos se dividieron en un 70 % para entrenamiento, un 15 % para validación y un 15 % para prueba. Se empleó una división estratificada para conservar la proporción de las clases en los diferentes subconjuntos.

Esta separación permite evaluar el modelo de forma más objetiva. No obstante, cuando existen señales relacionadas entre sí o procedentes de una misma fuente, también es importante considerar cómo se realiza la división para evitar que las similitudes entre los subconjuntos produzcan estimaciones excesivamente optimistas.

La evaluación de un clasificador requiere utilizar métricas que permitan analizar distintos aspectos de su desempeño.

La exactitud (*accuracy*) representa la proporción de predicciones correctas respecto al total de ejemplos evaluados. La precisión (*precision*) mide qué proporción de las predicciones asignadas a una clase corresponde realmente a esa clase. La exhaustividad (*recall*) mide qué proporción de los ejemplos reales de una clase fue identificada correctamente.

La puntuación F1 combina precisión y exhaustividad mediante su media armónica, proporcionando una medida útil cuando interesa equilibrar ambos indicadores. Por otra parte, el área bajo la curva ROC (AUC) permite evaluar la capacidad de discriminación del modelo a través de distintos umbrales de decisión en una clasificación binaria.

El uso conjunto de estas métricas ofrece una visión más completa del rendimiento que la exactitud por sí sola, especialmente cuando es importante conocer qué tipos de señales se confunden con mayor frecuencia.

**Trabajos Relacionados**

La aplicación de redes neuronales convolucionales al análisis de señales sísmicas ha sido estudiada en diversas investigaciones. Entre los recursos relevantes se encuentra STEAD (*STanford EArthquake Dataset*), presentado por Mousavi y colaboradores en 2019, que proporciona una amplia colección de registros sísmicos reales y señales de ruido para el desarrollo y la evaluación de modelos de aprendizaje automático.

En comparación con conjuntos de datos de gran escala como STEAD, el conjunto SeisTask utilizado en la experimentación inicial presenta características que facilitan el desarrollo de pruebas controladas: contiene 102 060 señales de tamaño fijo, organizadas en dos categorías, y permite trabajar con una estructura de datos uniforme. Estas características favorecen la preparación de los datos y el entrenamiento de modelos convolucionales en un entorno de recursos computacionales limitados.

El aporte de esta investigación consiste en diseñar, implementar y evaluar una red neuronal convolucional unidimensional para aprender patrones temporales de señales sísmicas. El modelo inicial alcanzó una exactitud del 87,53 % sobre el conjunto de prueba, lo que constituye un resultado experimental para la configuración y los datos utilizados.

La principal ventaja del enfoque desarrollado es su sencillez experimental y su posibilidad de reproducción y ampliación. No obstante, debido a las diferencias entre los conjuntos de datos, las etiquetas y las metodologías de evaluación, no es posible concluir que el modelo propuesto sea superior a los publicados en otras investigaciones únicamente a partir de sus valores de exactitud.

Por tanto, la contribución del trabajo se centra en la implementación y evaluación de una CNN sobre un conjunto de datos específico, así como en el análisis de sus resultados, limitaciones y posibilidades de mejora.

**Materiales y métodos**

Para el desarrollo experimental se utilizó Google Colab como entorno de programación y ejecución de código Python. Esta plataforma permite ejecutar experimentos de aprendizaje automático sin necesidad de configurar localmente

El procesamiento de los datos y la construcción del modelo se realizaron mediante bibliotecas especializadas en análisis numérico, manipulación de datos y aprendizaje profundo. Entre las herramientas empleadas se encuentran NumPy para las operaciones con matrices, pandas para la lectura de metadatos, h5py para acceder a los datos almacenados en formato HDF5 y TensorFlow con Keras para definir, entrenar y evaluar la red neuronal convolucional.

El uso de estas herramientas permitió organizar el flujo experimental desde la carga de las señales hasta la obtención de las métricas de evaluación.

El conjunto de datos seleccionado para la experimentación inicial fue SeisTask, publicado en Zenodo en 2026. Este recurso contiene 102 060 señales semisintéticas y sus metadatos asociados.

Las señales están almacenadas en una estructura tridimensional de dimensiones (102060, 2, 500), donde el primer eje representa el número de ejemplos, el segundo corresponde a dos componentes de la señal y el tercero contiene 500 muestras temporales por componente. De acuerdo con la descripción del conjunto de datos, las señales representan intervalos de cinco segundos muestreados a 100 Hz.

Los metadatos incluyen campos como el identificador de la tarea, la réplica, las características de generación de la señal, el rango de frecuencias y la etiqueta de clasificación. Para el experimento inicial se utilizaron las etiquetas que diferencian entre ruido puro y señales con eventos sísmicos sintéticos.

La selección de este conjunto de datos estuvo motivada por su tamaño manejable, la estructura uniforme de las señales y el equilibrio entre las dos categorías utilizadas. Estas propiedades facilitan la preparación de los datos y permiten desarrollar un primer experimento de clasificación mediante una CNN unidimensional.

Debe señalarse que el carácter semisintético del conjunto de datos constituye una limitación al interpretar los resultados: el rendimiento obtenido no demuestra por sí solo que el modelo pueda clasificar con la misma precisión registros sísmicos reales procedentes de diferentes estaciones.

Antes del entrenamiento, los datos fueron preparados para adaptarlos al formato de entrada requerido por la red neuronal convolucional.

En primer lugar, se cargaron las señales y sus etiquetas correspondientes. Posteriormente, se reorganizaron las dimensiones de los datos para obtener una representación de forma (102060, 500, 2), adecuada para una capa Conv1D que procesa secuencias temporales con dos componentes por instante.

Las señales se representaron utilizando el tipo de dato de punto flotante de 32 bits (float32). A continuación, los ejemplos se dividieron en tres subconjuntos: entrenamiento, validación y prueba. Se empleó una distribución del 70 %, 15 % y 15 %, respectivamente, con división estratificada para mantener la proporción de las categorías.

De esta forma, el conjunto de entrenamiento quedó compuesto por 71 442 ejemplos, mientras que los conjuntos de validación y prueba contenían 15 309 ejemplos cada uno.

El conjunto de entrenamiento se utilizó para ajustar los parámetros de la red; el de validación permitió supervisar el aprendizaje, y el de prueba se reservó para la evaluación final.

Se diseñó una red neuronal convolucional unidimensional mediante la API Sequential de Keras. La arquitectura se compone de capas convolucionales para extraer características temporales, capas de reducción dimensional, una etapa de agregación global y capas densas para realizar la clasificación.

La primera capa convolucional utiliza 32 filtros de tamaño 7 y función de activación ReLU. A continuación, una capa MaxPooling1D reduce la dimensión temporal. La segunda capa convolucional utiliza 64 filtros de tamaño 5, también con activación ReLU, seguida de otra operación de reducción temporal.

Posteriormente, GlobalAveragePooling1D resume las características extraídas a lo largo del tiempo. La representación resultante se procesa mediante una capa densa de 64 neuronas con activación ReLU y una capa Dropout con una tasa de 0,3, destinada a reducir el riesgo de sobreajuste.

Finalmente, el modelo incorpora una neurona de salida con activación sigmoide (sigmoid), que produce un valor entre cero y uno para la clasificación binaria. La arquitectura posee aproximadamente 15 009 parámetros entrenables.

Esta configuración fue seleccionada como una arquitectura inicial relativamente compacta, apropiada para estudiar la capacidad de las CNN unidimensionales para aprender patrones temporales en señales sísmicas.

El entrenamiento se realizó mediante el optimizador Adam y la función de pérdida binary\_crossentropy, apropiada para la clasificación binaria implementada. Se utilizaron la exactitud (accuracy) y el área bajo la curva ROC (AUC) como métricas de seguimiento.

Se estableció un máximo de 20 épocas de entrenamiento y un tamaño de lote (*batch size*) de 64 ejemplos. Además, se aplicó EarlyStopping, supervisando la pérdida de validación y utilizando una paciencia de cuatro épocas para detener el entrenamiento cuando no se observaran mejoras suficientes. Esta técnica se configuró para recuperar los pesos correspondientes a la mejor época de validación.

También se empleó ModelCheckpoint para guardar los pesos y la configuración del mejor modelo en el archivo mejor\_cnn.keras.

La configuración permitió supervisar el proceso de aprendizaje y conservar la versión del modelo que obtuvo el mejor resultado según la pérdida de validación.

Una vez finalizado el entrenamiento, se evaluó el modelo sobre el conjunto de prueba, que no se utilizó para ajustar los parámetros de la red. Se registraron la pérdida, la exactitud y el AUC, y se calcularon métricas por categoría mediante el informe de clasificación.

Las métricas de precisión, exhaustividad (*recall*) y puntuación F1 permitieron analizar el comportamiento del clasificador para cada una de las dos categorías. Este análisis complementa la exactitud global y permite identificar diferencias en la capacidad del modelo para reconocer los ejemplos de cada clase.

Los resultados obtenidos corresponden exclusivamente al experimento de clasificación binaria realizado con SeisTask. Por ello, no se interpretan como una evaluación de un clasificador de tres categorías ni como una demostración de desempeño general sobre terremotos reales.

**Resultados experimentales**

Durante el entrenamiento se estableció un máximo de 20 épocas. La mejor configuración según la pérdida de validación se obtuvo en la época 19, con una pérdida de validación de 0,29483, una exactitud de validación de 87,55 % y un AUC de 0,9485.

En la época 20, la pérdida de validación aumentó a aproximadamente 0,2974. Debido a la configuración de recuperación de los mejores pesos, el modelo conservó los parámetros correspondientes a la época con menor pérdida de validación.

En la evaluación final, el modelo obtuvo una pérdida de 0,2887, una exactitud de 87,53 % y un AUC de 0,9505 sobre el conjunto de prueba de 15 309 señales.

Estos resultados indican que la CNN aprendió patrones útiles para diferenciar las dos categorías presentes en el experimento. Sin embargo, las métricas deben interpretarse teniendo en cuenta que el conjunto de datos utilizado contiene señales semisintéticas y que la clasificación implementada es binaria.

Por consiguiente, los resultados constituyen una evaluación inicial del método propuesto y no permiten afirmar que el modelo distinga tres categorías ni que presente la misma capacidad de clasificación ante cualquier registro sísmico real.

Las métricas por categoría muestran un comportamiento relativamente equilibrado. Para la clase 0, el modelo obtuvo una precisión de 0,89 y una exhaustividad de 0,86. Para la clase 1, alcanzó una precisión de 0,86 y una exhaustividad de 0,89.

La diferencia entre las métricas indica que el modelo presenta un comportamiento ligeramente distinto según la categoría evaluada. En particular, la exhaustividad de la clase 1 fue superior a la de la clase 0, mientras que la precisión fue mayor para la clase 0.

Estos resultados complementan la exactitud global y permiten analizar el rendimiento del clasificador más allá de una única métrica. No obstante, para determinar qué tipos de errores comete con mayor frecuencia sería conveniente examinar también la matriz de confusión.

**Discusión de los resultados**

Los resultados obtenidos muestran que la red neuronal convolucional unidimensional alcanzó una exactitud del 87,53 % sobre el conjunto de prueba. Este valor indica que el modelo logró clasificar correctamente una proporción considerable de las señales utilizadas en la evaluación.

El valor de AUC de 0,9505 refleja una buena capacidad de discriminación entre las dos categorías del experimento a diferentes umbrales de decisión. Sin embargo, este indicador no debe interpretarse como una exactitud del 95,05 %, ya que mide una propiedad diferente del clasificador.

El análisis de las métricas por categoría muestra que el modelo obtuvo valores de F1 de aproximadamente 0,87 para la clase de ruido puro y 0,88 para la clase de señales con eventos sísmicos sintéticos. La proximidad entre ambos valores sugiere que el rendimiento fue relativamente equilibrado para las dos categorías evaluadas.

En conjunto, los resultados indican que la arquitectura implementada pudo aprender patrones útiles para la clasificación binaria de las señales de SeisTask. No obstante, estos resultados corresponden a un conjunto de datos específico y no garantizan un rendimiento equivalente sobre señales sísmicas reales procedentes de otras fuentes.

La comparación con investigaciones anteriores permite situar el experimento dentro del campo del aprendizaje profundo aplicado a la sismología. El conjunto STEAD, presentado por Mousavi y colaboradores, proporciona una colección de registros sísmicos reales y señales de ruido a mayor escala que SeisTask, lo que facilita el estudio de modelos con datos más diversos.

Frente a este tipo de recursos, SeisTask ofrece una estructura de datos uniforme y un volumen de señales que facilita la experimentación inicial con recursos computacionales limitados. Esta característica representa una ventaja práctica para el desarrollo y la evaluación de una arquitectura convolucional compacta.

Sin embargo, no sería científicamente correcto concluir que el modelo desarrollado supera a los modelos de investigaciones anteriores basándose únicamente en la exactitud obtenida. Para realizar una comparación directa sería necesario utilizar los mismos datos de evaluación o conjuntos equivalentes, establecer categorías comparables y controlar las condiciones experimentales.

Por tanto, la principal aportación del experimento consiste en demostrar la viabilidad de implementar y evaluar una CNN unidimensional para clasificar las dos categorías disponibles en el conjunto de datos seleccionado. La comparación con otros enfoques permite identificar oportunidades para ampliar la investigación y evaluar su capacidad de generalización.

El experimento presenta varias limitaciones que deben tenerse en cuenta al interpretar sus resultados.

En primer lugar, el modelo se entrenó utilizando dos categorías, por lo que todavía no permite realizar una clasificación multiclase que incluya una tercera categoría de señales. En consecuencia, los resultados obtenidos representan una etapa inicial del proyecto y no demuestran el cumplimiento de una clasificación de tres categorías.

En segundo lugar, el conjunto SeisTask contiene señales semisintéticas. Aunque estas permiten estudiar el comportamiento de la red en condiciones controladas, no garantizan que el modelo generalice adecuadamente a señales registradas durante terremotos reales.

Asimismo, la evaluación se realizó mediante una partición de entrenamiento, validación y prueba. Aunque esta separación permite obtener una estimación del desempeño sobre ejemplos no utilizados para ajustar los parámetros, sería conveniente realizar evaluaciones adicionales con datos independientes de otras fuentes para estudiar la capacidad de generalización.

Estas limitaciones no invalidan los resultados obtenidos, sino que delimitan su alcance y permiten establecer líneas de trabajo para mejorar el sistema.

**Conclusiones**

En este trabajo se diseñó, implementó y evaluó una red neuronal convolucional unidimensional para la clasificación de señales sísmicas mediante técnicas de aprendizaje profundo.

Se utilizó el conjunto de datos SeisTask, compuesto por 102 060 señales semisintéticas, y se desarrolló un procedimiento de preparación de datos que incluyó la reorganización de las dimensiones de las señales y su división en conjuntos de entrenamiento, validación y prueba.

La arquitectura implementada combinó capas convolucionales, operaciones de reducción dimensional, agregación global y capas densas para realizar una clasificación binaria. Durante la evaluación, el modelo alcanzó una exactitud del 87,53 % y un AUC de 0,9505 en el conjunto de prueba. Las métricas por categoría mostraron valores de F1 aproximados de 0,87 y 0,88, respectivamente.

Los resultados evidencian que la CNN aprendió patrones útiles para diferenciar las dos categorías utilizadas en el experimento. Sin embargo, debido a las características semisintéticas de los datos y a la naturaleza binaria de la clasificación, no es posible afirmar que el modelo identifique de forma general terremotos reales o que distinga tres categorías.

Finalmente, se establece como línea de trabajo futura la ampliación del experimento mediante un conjunto de datos con las categorías requeridas, el entrenamiento de una arquitectura adaptada a dicha clasificación y la evaluación de su desempeño mediante métricas comparables. Esto permitiría determinar con mayor precisión el alcance del método y sus posibilidades de aplicación al análisis automático de señales sísmicas.

**Referencias bibliográficas**

1. Mousavi, S. M., Sheng, Y., Zhu, W., & Beroza, G. C. (2019). STanford EArthquake Dataset (STEAD): A Global Data Set of Seismic Signals for AI. IEEE Access, 7, 179464–179476. [<u>https://doi.org/10.1109/ACCESS.2019.2947848</u>](https://doi.org/10.1109/ACCESS.2019.2947848)

2. Myren, S. (2026). SeisTask: A semi-synthetic, task-oriented, seismic time-series dataset for event detection [Conjunto de datos]. Zenodo. [<u>https://doi.org/10.5281/zenodo.18928724</u>](https://doi.org/10.5281/zenodo.18928724)

3. TensorFlow. (s. f.). Conv1D layer. Documentación oficial de TensorFlow. [<u>https://www.tensorflow.org/api\_docs/python/tf/keras/layers/Conv1D</u>](https://www.tensorflow.org/api_docs/python/tf/keras/layers/Conv1D)

4. Keras. (s. f.). EarlyStopping. Documentación oficial de Keras. [<u>https://keras.io/api/callbacks/early\_stopping/</u>](https://keras.io/api/callbacks/early_stopping/)

5. Keras. (s. f.). ModelCheckpoint. Documentación oficial de Keras. [<u>https://keras.io/api/callbacks/model\_checkpoint/</u>](https://keras.io/api/callbacks/model_checkpoint/)

6. Keras. (s. f.). Training with built-in methods. Guía oficial para el entrenamiento y la evaluación de modelos. [<u>https://keras.io/guides/training\_with\_built\_in\_methods/</u>](https://keras.io/guides/training_with_built_in_methods/)

Anexos
![](data:image/png;base64...)