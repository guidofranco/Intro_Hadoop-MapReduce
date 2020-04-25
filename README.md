# Conociendo Apache Hadoop y MapReduce

Este repositorio contiene el desarrollo de ejercicios propuestos en el curso [Intro to Hadoop and MapReduce](https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617) disponible en la plataforma [Udacity](https://www.udacity.com/)

La práctica consiste en implementar el modelo de programación MapReduce en Python para procesar tres archivos diferentes y responder a determinadas preguntas

## Primer dataset: Ventas

El código para esta sección está disponible en el folder *purchases*

El dataset en cuestión, *purchases.txt*, debe ser volcado en el sistema de archivos distribuido, *HDFS*.

```bash
# Primero creamos unos directorios en el filesystem
hdfs dfs -mkdir /user && hdfs dfs -mkdir /user/guido
hdfs dfs -mkdir input

hdfs dfs -put purchases.txt input
```

#### Consigna 1
Encontrar el valor de las ventas totales para las sig. categorias:

- Toys

- Consumer electronics

Ejecutamos el job de MapReduce correspondiente de la siguiente forma:

```bash
mapred streaming -input input -output output -mapper mapper_item.py -file mapper_item.py -reducer reducer_item.py -file reducer_item.py
```

El resultado contendrá el total para todas las categorías existententes, entonces lo filtraremos para responder lo solicitado

```bash
hdfs dfs -cat output_1/* | grep Toys
hdfs dfs -cat output_1/* | grep "Consumer electronics"
```

#### Consigna 2
Encontrar el valor monetario de la venta mas alta para las siguientes tiendas:
- Reno
- Toledo
- Chandler

Ejecutamos el job de MapReduce correspondiente para encontrar los valores solicitados:

```bash
mapred streaming -input input -output output_2 -mapper mapper_highest_sale.py -file mapper_highest_sale.py -reducer reducer_highest_sale.py -file reducer_highest_sale.py
```

El resultado contendrá el valor de la venta mas alta para cada tienda, entonces es necesario filtrar:

```bash
hdfs dfs -cat output_2/* | grep Reno
hdfs dfs -cat output_2/* | grep Toledo
hdfs dfs -cat output_2/* | grep Chandler
```

#### Consigna 3
Calcular el valor total de las ventas y la cantidad de ventas, abarcando todas las tiendas:

Ejecutamos el job de MapReduce correspondiente:

```bash
mapred streaming -input input -output output_3 -mapper mapper_total.py -file mapper_total.py -reducer reducer_total.py -file reducer_total.py

# Vemos el resultado obtenido
hdfs dfs -cat output_3/*
```

#### Consigna 4
Encontrar el valor promedio de ventas para cada día de la semana

```bash
mapred streaming -input input -output output_4 -mapper mapper_sales_mean.py -file mapper_sales_mean -reducer reducer_sales_mean.py -file reducer_sales_mean.py

hdfs dfs -cat output_4/*
```

#### Consigna 5
Calcular el monto total de ventas para cada día de la semana, usando un *combiner*

```bash
mapred streaming -input input -output output_5 -mapper mapper_sales_mean.py -file mapper_sales_mean.py -combner reducer_sumsales_wcombiner.py -file reducer_sumsales_wcombiner.py -reducer reducer_sumsales_wcombiner.py -file reducer_sumsales_wcombiner.py
```

Con esto verificamos como se reduce notablemente el número de entradas a la fase de Reducer al usar un *combiner*

## Segundo dataset: Logs
Se trabaja con un logfile de un web server anónimo.

El archivo sigue el formato [Common Log Format](https://es.wikipedia.org/wiki/Common_Log_Format).

Aquí una línea de ejemplo del mismo:

10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469

%h %l %u %t \"%r\" %>s %b

Donde:

%h: IP del cliente

%l: es la identidad del cliente, en caso de no estar disponible es "-".

%u: username del cliente, "-" si no está disponible.

%t: tiempo en el que el server terminó de procesar la request. El formato del mismo es [day/month/year:hour:minute:second zone]

%r: es una linea correspondiente a la request del cliente. Contiene el método, path, query-string y el protocolo.

%>s es el status code que el server devuelve al cliente.

%b es el tamaño, en bytes, del objeto que el server devuelve al cliente.

El archivo en cuestión debe ser insertado en el HDFS:
```bash
hdfs dfs -put acces_log input
```

#### Consigna 1

Calcular el nro. de hits por cada file del sitio web. Cuántos hits se hicieron a /assets/js/the-associates.js?

```bash
mapred streaming -input input -output output_1 -mapper mapper_hits_per_file.py -file mapper_hits_per_file.py -reducer reducer_hits_per_file.py -file reducer_hits per_file.py

hdfs dfs -cat output_1/* | grep assets/js/the-associates.js
```

#### Consigna 2

Calcular la cantidad de hits hechos por cada dirección IP. Cuántos hits fueron hechos por la ip 10.99.99.186?

```bash
mapred streaming -input input -output output_2 -mapper mapper_hits_per_ip.py -file mapper_hits_per_ip.py -reducer reducer_hits_per_ip.py -file reducer_hits_per_ip.py

hdfs dfs -cat output_2/* | grep 10.99.99.186
 ```

 #### Consigna 3

 Obtener el archivo mas popular del sitio, es decir aquel con mas ocurrencias en el logfile.

```bash
mapred streaming -input input -output output_3 -mapper mapper_most_popular_site.py -file mapper_most_popular_site.py -reducer reducer_most_popular_site.py -file reducer_most_popular_site.py

hdfs dfs -cat output_3/*
 ```

