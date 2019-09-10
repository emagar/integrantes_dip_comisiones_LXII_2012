import re
import os

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../data/asistencias_extractos_actas/")

lista = []

#añadir una columna de el nombre de la comision
#ver que pasa en linea 2186
#ver porque los justificantes no se guardan como otra cosa


def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

for filename in listdir_fullpath(path):
    data = open(filename)
    a = data.read()
    #Reemplazos
    a = a.replace(" y ", ",") #para quitar los "y" finales
    a = a.replace(".", "")
    #Necesario para crear division por día
    dias = a.split("\n\n\n")

    fecha = ''
    nombres = []
    #dia = dias[0] #para test
    for dia in dias:
        dia_div = dia.split("\n\n") # en el caso más reducido solo da un número que es la fecha, en el más amplio
        #... están la fecha, los presentes, los ausentes y los que tienen justificante
        fecha = dia_div[0].rstrip() #de la division el primero siempre es la fecha
        tipo = ""
        if len(dia_div) > 1: #Si en la division hay más que la fecha ...
            for i in range(1, len(dia_div)): #empieza en 1 para saltar la fecha e ir a parrafos donde hay nombres
                if bool(re.search(":", dia_div[i]) ): #si hay al menos dos puntos
                    tipo = dia_div[i].split(":",1)[0] #Solo va a hacer una division en caso que encuentre "
                    personas_w_rango = dia_div[i].split(":",1)[1].replace("\n","") #Personas con(with) rango (presidente, secretarios, asistentes)
                else: #si no hay dos puntos
                    tipo = "Asistieron" #Supongo que es el default. No obstante puede suceder que haya parrafos que se parezcan
                    #a los de asistentes normales por no tener una etiqueta inicial.
                    personas_w_rango = dia_div[i].replace("\n","")

                personas = personas_w_rango.split(";") #Aqui se divide en una lista primero presidente, secretarios e integrantes.
                for x, rango in enumerate(personas):
                    nombres = personas[x].split(",") #Ahora dentro de cada rango ya obtiene los nombres uno a uno.
                    for nombre in nombres:
                        lista.append(os.path.basename(filename) + "\t"
                                     + fecha + "\t"
                                     + nombre.rstrip().lstrip(" ") +"\t"
                                     + str(x) + "\t"
                                     + tipo + "\t"
                                     + str(i) + "\n") #Se forma la lista final tipo csv con tabuladores
        else:
            lista.append(os.path.basename(filename) + "\t"
                         + fecha + "\t"
                         + "" + "\t"
                         + "" + "\t"
                         + tipo + "\t"
                         + "" + "\n")

#Guardar en archivo #No lo crea si ya existe uno llamado asi
with open('../Asistencia_diputados.csv', 'w') as file:
    file.write("Comision" + "\t"
               + "Fecha" + "\t"
               + "Nombre" +"\t"
               + "Rango" + "\t"
               + "Tipo" + "\t"
               + "Parrafo_dia" + "\n")
    for entrada in lista:
        file.write(entrada)


# for i, dia in enumerate(dias):
#     dias[i] = dias[i].split("\n\n")
#     dias[i][1] = dias[i][1].split(";")
#     for n, z in enumerate(dias[i][1]):
#         dias[i][1][n] = dias[i][1][n].split(",")
#La mejoor forma de cambiar dentro de una lista en con enumerate.
#El problema es que los strings son inmutables asi que deben ser cambiados desde fuera.




####
####
####
####


# A programar
# Abrir
# Cortar por triple \n
#
# Cortar la fecha y poner en nueva variable
# primero cortar por algo que tenga antes un ":"
# Cortar por ";"
# Cortar por ","

#
