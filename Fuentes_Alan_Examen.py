# Examen
import statistics as st
import csv
import random as r 
import os
os.system('cls')
sueldos=[]
lista_trabajadores=["Juan Pérez","Maria Garcia","Carlos Lopez","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

def menu(titulo,lista):
    print('========================================')
    print(titulo.upper())
    print('========================================')
    while True:
        i=1
        for elem in lista:
            print(i,'.-',elem)
            i+=1
        print(i,'.- Salir')
        opc=input('Ingrese Opción: ')
        if opc.isdigit():
            opc_int=int(opc)
            if opc_int>=1 and opc_int<=i:
                return opc_int
            else:
                print('Debe Ingresar un Número entre 1 y ',i)
        else:
            print('Ingrese Sólo Números')

#================================== 1

def sueldos_aleatorios(sueldos):
    for i in range (0,10):
        sueldo=r.randint(3000000,2500000)
        print(sueldo)
        return sueldos
#================================== 2
def sueldo_800(sueldo):
    for sueldo in lista_trabajadores():
        if sueldo<800000:
            sueldo_menor_800=sueldo_menor_800+1
            return sueldo_800
def sueldo_800_2m(sueldo):
    for sueldo in lista_trabajadores():
        if sueldo>=800000 and sueldo<=2000000:
            sueldo_entre=sueldo_entre+1
            return sueldo_800_2m
def sueldo_2m(sueldo):
    for sueldo in lista_trabajadores():
        if sueldo>2000000:
            sueldo_mayor2m=sueldo_mayor2m+1
            return sueldo_2m
def clasificar_sueldos():
    print('Sueldos menores a $800.000 TOTAL: ' ,sueldo_800)
    print("Nombre empleado | Sueldo")
    print('')
    print('Sueldos entre $800.000 y $2.000.000 TOTAL: ' ,sueldo_800_2m)
    print("Nombre empleado | Sueldo")
    print('')
    print('Sueldos superiores a $2.000.000 TOTAL: ' ,sueldo_2m)
    print("Nombre empleado | Sueldo")
    print('')
    print('TOTAL SUELDOS: $',)

#================================== 3
def estadisticas(sueldos):
    sueldo_alto=print('Sueldo más alto = ',max(sueldos))
    print(sueldo_alto)
    sueldo_bajo=print('Sueldo más bajo =' ,min(sueldos))
    print(sueldo_bajo)
    promedio_sueldo=print('Promedio de sueldos = ',st.mean(int(sueldos)))
    print(promedio_sueldo)
    medida_geometrica=print('Media geométrica = ' ,st.mean(sueldos))
    print(medida_geometrica)

#================================== 4
def reportar_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(["Nombre empleado","Sueldo Base","Descuento Salud","Descuento AFP","Sueldo Líquido"])

        ##descuento_salud
        ##descuento_afp #12%
        #sueldo_liquido=(sueldos-descuento_salud-descuento_afp)##
 
while True:
    opc=menu('Menu principal',['Asignar sueldos aleatorios','Clasificar sueldos','Ver estadisticas','Reporte de sueldos'])
    if opc==1:
        print(sueldos_aleatorios)
    elif opc==2:
        print(clasificar_sueldos)
    elif opc==3:
        print(estadisticas)
    elif opc==4:
        print(reportar_sueldos)
    elif opc==5:
        print('Finalizando programa...')
        print('Desarrollado por Alan Fuentes')
        print('RUT 21.055.714-8')
        break

