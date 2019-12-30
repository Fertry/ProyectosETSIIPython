
import csv
from collections import namedtuple

Juego = namedtuple("Juego","rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales")

def lee_juegos(fichero):

    resultado = []

    with open(fichero, encoding="utf-8") as f:

        datos = csv.reader(f)
        next(datos)

        for rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales in datos:

            rank = int(rank)
            year = int(year)
            na_sales = float(na_sales)
            eu_sales = float(eu_sales)
            jp_sales = float(jp_sales)
            other_sales = float(other_sales)
            global_sales = float(global_sales)

            tupla = Juego(rank,name,platform,year,genre,publisher,na_sales,eu_sales,jp_sales,other_sales,global_sales)

            resultado.append(tupla)

        f.close()

    return resultado

def juegos_distribuidora_anyo(juegos, publisher, anyo):

    lista = [j.name for j in juegos if j.publisher == publisher and j.anyo == anyo]

    return lista

def juegos_mas_ventas_globales_saga(juegos, saga):

    tupla = max((j.global_sales, j.name, j.year) for j in juegos if saga in j.name)

    return tupla

def ventas_por_zonas(juegos, anyo_inicial = None, anyo_final = None):

    resultado = {"America":0, "Europa":0, "Japon":0, "Otros":0}

    for juego in juegos:

        if anyo_inicial is None and anyo_final is None:

            resultado["America"] += round(juego.na_sales, 2)
            resultado["Europa"] += round(juego.eu_sales, 2)
            resultado["Japon"] += round(juego.jp_sales, 2)
            resultado["Otros"] += round(juego.other_sales, 2)

        elif anyo_inicial is None:

            if juego.year < anyo_final:

                resultado["America"] += round(juego.na_sales, 2)
                resultado["Europa"] += round(juego.eu_sales, 2)
                resultado["Japon"] += round(juego.jp_sales, 2)
                resultado["Otros"] += round(juego.other_sales, 2)

        elif anyo_final is None:

            if juego.year > anyo_inicial:

                resultado["America"] += round(juego.na_sales, 2)
                resultado["Europa"] += round(juego.eu_sales, 2)
                resultado["Japon"] += round(juego.jp_sales, 2)
                resultado["Otros"] += round(juego.other_sales, 2)

        else:

            if juego.year > anyo_inicial and juego.year < anyo_final:
                
                resultado["America"] += round(juego.na_sales, 2)
                resultado["Europa"] += round(juego.eu_sales, 2)
                resultado["Japon"] += round(juego.jp_sales, 2)
                resultado["Otros"] += round(juego.other_sales, 2)

    return resultado

def top_n_juegos_por_genero(juegos, n=1):

    resultado = {}

    for juego in juegos:

        clave = juego.genre

        if clave not in resultado:

            resultado[clave] = []

        if len(resultado[clave]) < n:

            items = {j.rank : j.name for j in juegos if j.genre == clave}

            resultado[clave].append(sorted(items.items(), key = lambda x:x[0])[:n])

    return resultado

#def distribuidora_mas_juegos_genero(juegos, genero):

print("##############################################################################################################")

ruta_datos = "C:/Drive/Programacion/Python/PythonSeptiembre/Juegos/datos.csv"

datos_leidos = lee_juegos(ruta_datos)

print("Datos leidos: ")
print(datos_leidos)

print("##############################################################################################################")

publisher = "NINTENDO"
anyo = 2006

lista_nintendo_2006 = juegos_distribuidora_anyo(datos_leidos, publisher, anyo)

print("Juegos de Nintendo en 2006: ")
print(lista_nintendo_2006)

print("##############################################################################################################")

nombre_juego = "MARIO"

juegos_mas_vendidos_global = juegos_mas_ventas_globales_saga(datos_leidos, nombre_juego)

print("Ventas globales del juego mas vendido con el nombre MARIO: ")
print(juegos_mas_vendidos_global)

print("##############################################################################################################")

ventas1 = ventas_por_zonas(datos_leidos, None, None)
ventas2 = ventas_por_zonas(datos_leidos, None, 2015)
ventas3 = ventas_por_zonas(datos_leidos, 2006, None)
ventas4 = ventas_por_zonas(datos_leidos, 2008, 2018)

print("Juegos en zonas: ")
print(ventas1)
print(ventas2)
print(ventas3)
print(ventas4)

print("##############################################################################################################")

diccionario_genero = top_n_juegos_por_genero(datos_leidos, 2)

print("Diccionario con los n mejores juegos por genero: ")
print(diccionario_genero)

print("##############################################################################################################")
