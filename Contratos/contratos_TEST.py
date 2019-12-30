# -*- coding: utf-8 -*-
'''
Created on 9 ene. 2019

@author: reinaqu_2
'''

#Arreglar importaciones!
from contratos import *
################################################################
#  Funciones de test
################################################################
def test_trabajadores_contratados_actividad(contratos):
    print('Trabajadores contratados en la actividad 77232:',
          trabajadores_contratados_actividad(contratos, '77232'))
    print()
        
def test_dias_contrato_trabajador(contratos):
    print('Total de días de contrato del trabajador 27634587:',
          dias_contrato_trabajador(contratos, '27634587'))
    print()

def test_trabajador_mas_dias(contratos):
    dias, numeroSS = trabajador_mas_dias(contratos)
    print('Trabajador con más días de contrato:', numeroSS)
    print('Total de días acumulados:', dias)
    print()
    
def test_indexa_contratos_por_actividad(contratos):
    print('Indexando los contratos por actividad.')
    contratos_por_actividad = indexa_contratos_por_actividad(contratos)
    print('Mostrando los 3 contratos con mayor duración de la actividad 77232:')
    for contrato in contratos_por_actividad['77232']:
        print('\t', contrato)
    print()

def test_muestra_evolucion_contratos(contratos):
    codigo = '32391'
    print('Mostrando gráfica con la evolución del número de contratos de la actividad', codigo)
    muestra_evolucion_contratos(contratos, codigo)
    print()
      
################################################################
#  Programa principal
################################################################
if __name__ == '__main__':
    contratos = lee_contratos('contratos.csv')
    print('EJERCICIO 1:')
    print('Número total de contratos:', len(contratos)) 
    print('Mostrando el primer contrato leído:', contratos[0], '\n')
    
    '''
    Elimine los comentarios de las llamadas a los test a medida que
    vaya escribiendo las respectivas funciones
    '''
    
    print('EJERCICIO 2:')
    test_trabajadores_contratados_actividad(contratos)
    
    print('EJERCICIO 3:')
    test_dias_contrato_trabajador(contratos)
    
    print('EJERCICIO 4:')
    test_trabajador_mas_dias(contratos)
    
    #print('EJERCICIO 5:')
    #test_indexa_contratos_por_actividad(contratos)
    
    print('EJERCICIO 6:')
    test_muestra_evolucion_contratos(contratos)
