
from collections import namedtuple
import csv

Registro = namedtuple("Registro", "distrito,seccion,barrio,pais,hombres,mujeres")

def lee_datos_extranjeros(fichero):

    registros = []

    with open(fichero, encoding="utf-8") as f:

        datos = csv.reader(f)

        next(datos)

        for distrito,seccion,barrio,pais,hombres,mujeres in datos:

            hombres = int(hombres)
            mujeres = int(mujeres)

            tupla = Registro(distrito,seccion,barrio,pais,hombres,mujeres)

            registros.append(tupla)

    f.close()

    return registros

def numero_nacionalidades_distintas(registros):

    conjunto_nacionalidades = {r.pais for r in registros}
    
    return len(conjunto_nacionalidades)

def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):

    tupla = set((r.distrito, r.seccion) for r in registros if r.pais in paises)
        
    return sorted(tupla)

def total_extranjeros_por_pais(registros):

    diccionario = {}

    for registro in registros:

        clave = registro.pais

        if clave not in diccionario:

            diccionario[clave] = registro.hombres + registro.mujeres

        else:

            diccionario[clave] += registro.hombres + registro.mujeres

    return diccionario

def top_n_extranjeria(registros, n=3):

    diccionario = total_extranjeros_por_pais(registros)

    resultado = sorted(diccionario.items(), key = lambda x:x[1], reverse = True)

    return resultado[:n]

def calculaPaisesPorBarrio(registros, barrio):

    paises = []

    paises.append(r.pais for r in registros if r.barrio == barrio)

    return len(paises)

def barrio_mas_multicultural(registros):

    maximo = 0
    mayor = None

    diccionario = {r.barrio : calculaPaisesPorBarrio(registros, r.barrio) for r in registros} 

    for barrio in diccionario.keys():

        for numero in diccionario.values():

            if numero > maximo:

                maximo = numero
                mayor = barrio

    return mayor

def calculaExtranjerosDadoUnTipo(registros, tipo):

    diccionario = {}

    for registro in registros:

        clave = registro.barrio

        if clave not in diccionario:

            diccionario[clave] = 0
        
        if tipo == "Hombres":

            diccionario[clave] += registro.hombres

        elif tipo == "Mujeres":

            diccionario[clave] += registro.mujeres

        else: 

            diccionario[clave] += registro.hombres + registro.mujeres

    return diccionario

def barrio_con_mas_extranjeros(registros, tipo = None):

    diccionario = calculaExtranjerosDadoUnTipo(registros, tipo)

    #Haya el maximo valor numerico de entre los elementos del diccionario comparando por valores no claves:
    resultado = max(diccionario.items(), key = lambda x:x[1])

    #Devuelve la clave asociada a ese valor maximo:
    return resultado[0]

def pais_mas_representado_por_distrito(registros):

    diccionario = agrupar_por_distrito(registros)

    resultado = {}

    for (distrito, registros_diccionario) in diccionario:

        #Llamamos a la funcion top_n_extranjeria, le pasamos los registros calculados por la funcion auxiliar y nos devuelve el mayor registro para ese distrito:
        resultado[distrito] = top_n_extranjeria(registros_diccionario, 1)[0][0]

    return resultado

def agrupar_por_distrito(registros):

    resultado = {}

    for registro in registros:

        clave = registro.distrito

        if clave not in resultado:

            resultado[clave] = [registro]

        else:

            resultado[clave].append(registro)

    return resultado

print("#############################################################################################################")
        
registros_leidos = lee_datos_extranjeros("C:/Drive/Programacion/Python/PythonSeptiembre/Extranjeria/datos.csv")

print("Registros:")
print(registros_leidos)

print("#############################################################################################################")

numero = numero_nacionalidades_distintas(registros_leidos)

print("Numero de nacionalidades:")
print(numero)

numero_nacionalidades_distintas

print("#############################################################################################################")

paises_leidos = ("ARGENTINA", "PERU", "ARMENIA")

tuplitas = secciones_distritos_con_extranjeros_nacionalidades(registros_leidos, paises_leidos)

print("Lista tuplas con distrito/seccion para los paises dados:")
print(tuplitas)

print("#############################################################################################################")

diccionario = total_extranjeros_por_pais(registros_leidos)

print("Diccionario numero extranjeros por pais:")
print(diccionario)

print("#############################################################################################################")

diccionario_n_extranjeros = top_n_extranjeria(registros_leidos, n=2)

print("Diccionario con los n paises de mas extranjeros:")
print(diccionario_n_extranjeros)

print("#############################################################################################################")

barrio = barrio_mas_multicultural(registros_leidos)

print("Barrio con mas paises:")
print(barrio)

print("#############################################################################################################")

barrio_mayor_none = barrio_con_mas_extranjeros(registros_leidos, tipo = None)
barrio_mayor_hombres = barrio_con_mas_extranjeros(registros_leidos, tipo = "Hombres")
barrio_mayor_mujeres = barrio_con_mas_extranjeros(registros_leidos, tipo = "Mujeres")

print("Barrio con mayor numero de extranjeros de ambos sexos:")
print(barrio_mayor_none)
print("Barrio con mayor numero de extranjeros masculinos:")
print(barrio_mayor_hombres)
print("Barrio con mayor numero de extranjeros femeninos:")
print(barrio_mayor_mujeres)

print("#############################################################################################################")

resultado_diccionario = pais_mas_representado_por_distrito(registros_leidos)

print("Diccionario con el pais mas representado por distrito:")
print(resultado_diccionario)

print("#############################################################################################################")
