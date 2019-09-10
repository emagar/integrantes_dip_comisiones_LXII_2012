# Diputados Integrantes de Comisiones, Legislatura LXII 2012-2015


En este repositorio se trata de reintegrar, a partir de las actas de sesiones, las asistencias de los diputados a sus respectivas comisiones.
El caso que se analiza es el de la cámara de diputados de México en la legislatura de 2012-2015 (LXII).

La fuente de datos que se utilizó fue la gaceta parlamentaria en su versión digital con url: http://gaceta.diputados.gob.mx/gp62_actas.html  activa aún el 2 de julio de 2019. En caso de que llegue a estar fuera de linea https://archive.org tiene una versión del 2 de abril de 2016 que parece ser idéntica a la aquí consultada.

En general las actas no siguen una estructura establecida. Muchas veces en ellas no se encuentra registro más que de los diputados integrantes de la Junta Directiva. Algunas otras veces tiene la asistencia de los que solo son integrantes y en algunas inclusive tiene la información de los ausentes o de los que presentaron su justificante de inasistencia. Asimismo, debido a una estructura no homologada a la hora de redactar las actas es frecuente encontrar que las estructuras son diferentes de una comisión a otra. Se hizo lo posible por tratar de unificarlos en una forma compatible.

Dada la estructura heterogénea de las actas y la forma en la que está construida la página web fue necesario hacer los extractos manualmente ya que las formas que se intentaron para scrapear la información no fueron fructíferas. 

Los extractos de las actas obtenidos manualmente se encuentran en data/asistencias_extractos_actas/ en la carpeta se encuentra un csv por cada comisión el cual contiene la información respectiva a las asistencias de todas las sesiones disponibles. 

El código para generar una sola tabla se encuentra en code/script_comisiones_asistencia.py. Este archivo contiene un programa en python que organiza la información de los extractos. El resultado que arroja es un csv con separación por tabuladores (en vez de comas) mismo que es escrito junto a este archivo en la ubicación principal del proyecto con el nombre "Asistencia_diputados.csv". Este archivo tiene 6 variables las cuales son: Comision, Fecha, Nombre, Rango, Tipo y Parrafo_dia. Las tres primeras se explican solas. Para las últimas se necesita entender solo un par de cosas. Cada archivo de extracto que corresponde a cada comisión se encuentra estructurado por Fecha/Tipo de referencía/Rango lo que esto quiere decir es que por cada comisión se subdividió en días y cada día se subdivide en Tipo de referencia (puede ser asistente, justificante, ausente, etc.) dentro de cada uno se subdivide por rango (presidente, secretarios, integrantes) cuando dicha información está disponible. Finalmente la variable Parrafo_dia fue una forma fácil de medir errores ya que está estrechamente relacionada a "Tipo_referencia" con ella es fácil notar si se está escribiendo de más en un día si es que parece contener demasiados párrafos (comúnmente no tienen más de 3), esto ocurre cuando hay errores de captura dentro de los extractos de cada comisión.

En el archivo data/Capturados.csv se encuentra una bitácora en la que se indicaron observaciones particulares que se encontraron en algunas de las comisiones, así como una columna que indica la ronda en la cual el capturista hizo las respectivas comisiones. Esto último es para poder notar si es que al momento de extraer la información dependiendo de la ronda se cometió algún tipo de error consistente. Es algo así como dividir por lotes de producción.

Finalmente, se recalca que la base no puede ser usada para ver asistencias o inasistencias con total fiabilidad ya que a veces los diputados no incluyeron en la minuta a todos los asistentes sino solo a los integrantes de la mesa directiva y a su vez, en estos casos, se incluyeron nombres sin que figurara la rúbrica correspondiente a su asistencia.


