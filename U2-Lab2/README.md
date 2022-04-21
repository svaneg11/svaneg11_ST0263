# Unidad 2 - Lab 2 -TET
La evidencia del trabajo se encuentra en el archivo pdf.


## Version Monolitica

* Se creo una carpeta "monolitico" para la primera version de una sola maquina virtual.


* La version monolitica funciona con un solo docker compose.

## Version Distribuida

* Se creo la carpeta "distribuido" para el laboratorio hecho en varias maquinas virtuales.


* La version distribuida tiene un docker-compose para cada servicio backend, frontend, nginx-front, nginx-back.


* Ademas en cada carpeta hay un script .sh que se encarga de instalar las dependencias y correr el compose.

* Las VM de mongo estan en baremetal, pero tambien cuentan con su archivo.sh