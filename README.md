# [ICS1113] - Modelo Proyecto

En el archivo `main.py` está todo el códgio correspondiente al modelo, junto a las variables implementadas, la carga de datos de los parametros, y las restricciones definidas hasta ahora :sweat_smile:.

Con el archivo `maker.py` se crea o actualiza el archivo `parameters.json` que contine todos los valores relacionados con los parametros que se utilizan. Estos son cargados al modelo mediante la función `load_data` definida en el archivo principal.

Dentro del archivo `parameters.json` solo se pueden editar los máximos correspondiente a los **Conjuntos**, ya que estos son lo sutilizados para finalmente crearlos en el modelo.

Además, en el archivo `maker.py` se pueden editar los atributos del diccionario `aux3`, el cual contine **MIN, MAX** de cada parametro para crear valores random *(mientras tanto)*.

\
Atte,\
Ian B.