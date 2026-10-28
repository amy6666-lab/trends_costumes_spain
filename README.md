Análisis de Google Trends: Disfraces en España

1) Descripción del proyecto

Este proyecto analiza la evolución del interés de búsqueda del término "disfraces" en España mediante datos de Google Trends.
El objetivo es identificar los periodos del año en los que aumenta el interés por los disfraces y explorar cómo esta información puede ayudar a una tienda a planificar sus campañas de marketing.
El análisis se desarrolla con Python y herramientas de análisis y visualización de datos.

2) Objetivos

·Analizar la evolución del interés de búsqueda a lo largo del tiempo.
·Identificar los meses con mayor interés.
·Comparar los patrones de búsqueda entre distintos años.
·Estudiar los cambios del interés entre meses consecutivos.
·Proponer recomendaciones para planificar campañas de marketing relacionadas con Carnaval y Halloween.

3) Fuente de datos

Los datos utilizados proceden de Google Trends y corresponden al término de búsqueda "disfraces" en España.
El periodo analizado abarca desde octubre de 2021 hasta octubre de 2026.
Importante: Google Trends utiliza un índice de interés relativo normalizado entre 0 y 100. Estos valores no representan el número absoluto de búsquedas, las ventas ni las interacciones con anuncios.

4) Herramientas utilizadas

·Python: desarrollo del análisis.
·pandas: carga, transformación y análisis de los datos.
·Matplotlib: creación de gráficos.
·pathlib: gestión de las rutas y localización del archivo CSV.

5) Metodología

El análisis se desarrolla en las siguientes etapas:
·Localización y carga del archivo CSV.
·Conversión de las fechas y ordenación cronológica.
·Extracción del año y del número de mes.
·Identificación de los meses con mayor interés en cada año.
·Cálculo del interés medio por mes.
·Comparación del interés mensual entre distintos años.
·Cálculo de las variaciones del interés entre meses consecutivos.
·Interpretación de los resultados desde una perspectiva de marketing.

6) Visualizaciones y resultados  

6.1 Evolución temporal del interés
El primer gráfico permite observar cómo ha evolucionado el interés de búsqueda de "disfraces" a lo largo del periodo analizado.
Esta visualización ayuda a detectar aumentos y descensos del interés y a localizar posibles patrones estacionales.

6.2 Interés medio por mes
El gráfico de barras muestra el interés medio asociado a cada mes.
Los resultados destacan especialmente febrero y octubre, dos periodos relacionados con celebraciones en las que los disfraces tienen un papel importante.
Febrero se relaciona con las celebraciones de Carnaval, mientras que octubre destaca por Halloween.

6.3 Comparación entre años
La comparación mensual permite observar qué patrones se repiten y qué diferencias aparecen entre años.
Aunque se identifican periodos de mayor interés similares, las variaciones entre años pueden estar relacionadas con factores como el calendario de las celebraciones, los hábitos de búsqueda y otros acontecimientos.

6.4 Cambios mensuales del interés
El último gráfico representa la diferencia entre el índice de interés de un mes y el del mes anterior para cada año.
Esta comparación permite observar cuándo se producen aumentos o descensos más pronunciados del interés de búsqueda.

7) Interpretación desde el marketing

Los resultados sugieren que Carnaval y Halloween son dos oportunidades relevantes para una tienda de disfraces.
·Campaña de Carnaval
Se propone comenzar la planificación y preparación de la campaña en diciembre, con el objetivo de lanzar las acciones comerciales durante enero.
La intención es dar visibilidad a los productos antes de los principales periodos de compra y aprovechar el aumento del interés que se observa en torno a febrero.
·Campaña de Halloween
Se propone iniciar la campaña a mediados de septiembre, antes del incremento de interés asociado a octubre.
Esta anticipación permitiría dar visibilidad al catálogo, comunicar diferentes opciones de disfraces y preparar el stock con suficiente margen.
Estas fechas son recomendaciones iniciales basadas en el patrón de búsqueda observado. Para optimizarlas, sería necesario contrastarlas con datos de ventas, conversiones y resultados de campañas publicitarias.

8) Conclusiones

El análisis muestra una concentración del interés de búsqueda en determinados periodos del año, especialmente febrero y octubre.
Este patrón puede servir como referencia para anticipar la preparación de campañas, organizar el calendario comercial y planificar las necesidades de inventario.
Sin embargo, el interés de búsqueda no garantiza una compra. Por ello, los datos de Google Trends deberían complementarse con información comercial para tomar decisiones más precisas.

9) Limitaciones del análisis

·Google Trends proporciona un índice relativo, no el volumen absoluto de búsquedas.
·El interés de búsqueda no equivale necesariamente a intención de compra.
·Los resultados por año pueden verse afectados por las fechas concretas de las celebraciones.
·El periodo analizado comienza en octubre de 2021 y termina en octubre de 2026, por lo que esos años no contienen doce meses completos.
·Las relaciones observadas no demuestran por sí solas que una celebración sea la causa de un aumento del interés.

10) Estructura del proyecto

·trends_disfraces_espana.py: script principal del análisis.
·data/: carpeta que contiene los datos originales.
·README.md: documentación del proyecto.

Autora: Amelia Graciela Flores Aravena.
Proyecto personal de análisis de datos con enfoque en marketing.

Muchas gracias por llegar aquí y si puedes dejarme comentarios para poder mejorar estare muy agradecida :D 
