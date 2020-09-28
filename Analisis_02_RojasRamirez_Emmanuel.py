from builtins import input


def opci1():
    import csv

    lista_datos = []

    with open('synergy_logistics_database.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            lista_datos.append(linea)  # hacemos copia del archivo

            # generar rutas y agregar el valor

    def rutasc(dire):
        contador = 0  # cuantas veces sucede la ruta Mexico Japon
        rutas_contada = []  # agrega las rutas para que ya no se repitan
        conteo_rutas = []
        for ruta in lista_datos:

            if ruta[1] == dire:  # las rutas que me importan, en este caso exportacion
                ruta_actual = [ruta[2], ruta[3]]  # origen y direccion i.e. japon y tailandia

                if ruta_actual not in rutas_contada:  # si tailanda-japon no esta contada, haz esto

                    for ruta2 in lista_datos:  # aqui se debe colocar el condicional de la direccion
                        if ruta_actual == [ruta2[2], ruta2[3]] and ruta2[
                            1] == dire:  # no es la forma mas viable de hacerlo
                            contador += 1
                            # print(ruta_actual)
                    rutas_contada.append(ruta_actual)
                    conteo_rutas.append([ruta[2], ruta[3], contador])  # origen y direccion original
                    contador = 0
        return conteo_rutas

    def sort_list(old_list, orden):  # regresa lista
        a = list(map(list, old_list))  # copy list #map avoids fors #fist list for iterable map object
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if orden == 'may':
                    if a[j][2] < a[j + 1][2]:
                        a[j], a[j + 1] = a[j + 1], a[j]  # se pudo haber eliminado una linea, pero prefiero por claridad
                else:
                    if a[j][2] > a[j + 1][2]:
                        a[j], a[j + 1] = a[j + 1], a[j]
        return a
    opci=int(input('Introduce 1 o 2: 1. Exports 2.Imports'))

    direccion = ['Exports', 'Imports']
    if opci==1:
        direccion2=direccion[0]
    else:
        direccion2=direccion[1]
    conteor = rutasc(direccion2)
    orden = sort_list(conteor, 'may')
    for i in orden:
        print(i)
    print('Num items',len(orden))

def opci2():
    import csv
    lista_datos = []
    with open('synergy_logistics_database.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            lista_datos.append(linea)  # hacemos copia del archivo
    def transpo(dire):
        contador = 0  #
        suma = 0
        medios_ruta = []  #
        conteo_medios = []
        for ruta in lista_datos:
            if ruta[1] == dire:  # las rutas que me importan, en este caso exportacion
                # contar medios
                # sumar valor de cada ruta
                # ordenar de mayor a menor
                ruta_actual = ruta[7]
                if ruta_actual not in medios_ruta:  # si tailanda-japon no esta contada, haz esto
                    for ruta2 in lista_datos:  # aqui se debe colocar el condicional de la direccion
                        if ruta_actual == ruta2[7] and ruta2[1] == dire:  # no es la forma mas viable de hacerlo
                            contador += 1
                            suma += int(ruta2[9])
                    medios_ruta.append(ruta_actual)
                    conteo_medios.append([ruta[7], contador, suma])  # origen y direccion original
                    contador = 0
                    suma = 0
        return conteo_medios
    def sort_list(old_list, orden):  # regresa lista
        a = list(map(list, old_list))  # copy list #map avoids fors #fist list for iterable map object
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if orden == 'may':
                    if a[j][2] < a[j + 1][2]:
                        a[j], a[j + 1] = a[j + 1], a[j]  # se pudo haber eliminado una linea, pero prefiero por claridad
                else:
                    if a[j][2] > a[j + 1][2]:
                        a[j], a[j + 1] = a[j + 1], a[j]
        return a
    def sci(lista):  # anadir en nested list en el tercer reich
        # output=[["{:.4e}".format(i[2])]   for i in input]  se podra haber usado el map?
        input = list(map(list, lista))
        for i in input:
            i[2] = "{:.4e}".format(i[2])
        return input

    direccion = ['Exports', 'Imports']


    opcii=int(input('Introduce un num entero. 1.Exports 2. Imports 3.regresar'))
    while True:
        if opcii==1:
            conteor_export_transporte = transpo(direccion[0])
            orden_valor_transport_exp = sort_list(conteor_export_transporte, 'may')  # aqui no deberia haber sci
            orden_sci_export = sci(orden_valor_transport_exp)
            for elem in orden_sci_export:
                print(elem)
            opcii = int(input('Introduce un num entero. 1.Exports 2. Imports 3.regresar'))
        elif opcii==2:
            conteor_import_transporte = transpo(direccion[1])
            # mayor  #reducir con funciones si hay tiempo
            # orden_valor_transport=sort_list(conteor_transporte,'mayo')
            orden_valor_transport_imp = sort_list(conteor_import_transporte, 'may')  # aqui se modifica mayor o menor
            orden_sci_import = sci(orden_valor_transport_imp)
            for elem in orden_sci_import:
                print(elem)
            opcii = int(input('Introduce un num entero. 1.Exports 2. Imports 3.regresar'))
        else:
            break

def opci3():
    import csv
    lista_datos = []
    with open('synergy_logistics_database.csv', 'r') as archivo_csv:
        lector = csv.reader(archivo_csv)
        for linea in lector:
            lista_datos.append(linea)  # hacemos copia del archivo
            # generar rutas y agregar el valor
    def Sort(sub_li):
        # key is set to sort using second element of
        # sublist lambda has been used
        sub_li.sort(reverse=True, key=lambda x: x[2]) #indice
        return sub_li

    # obtiene el 80% de porcentaje
    def rutasc(dire):
        contador_valor = 0  # cuantas veces sucede la ruta Mexico Japon
        rutas_contada = []  # agrega las rutas para que ya no se repitan
        conteo_rutas = []
        for ruta in lista_datos:

            if ruta[1] == dire:  # las rutas que me importan, en este caso exportacion
                ruta_actual = [ruta[2], ruta[3]]  # origen y direccion i.e. japon y tailandia

                if ruta_actual not in rutas_contada:  # si tailanda-japon no esta contada, haz esto

                    for ruta2 in lista_datos:  # aqui se debe colocar el condicional de la direccion
                        if ruta_actual == [ruta2[2], ruta2[3]] and ruta2[
                            1] == dire:  # no es la forma mas viable de hacerlo
                            contador_valor += int(ruta2[9])
                    rutas_contada.append(ruta_actual)
                    conteo_rutas.append([ruta[2], ruta[3], contador_valor])  # origen y direccion original
                    contador_valor = 0
        # return conteo_rutas
        valortotal = sum(valor[2] for valor in conteo_rutas)
        porcen = []
        for i in conteo_rutas:
            porcen.append([i[0], i[1], (i[2] / valortotal) * 100])
        # porcentajes = (valorin[2]/valortotal for valorin in conteor)
        ord_porce = Sort(porcen)
        sumpor = 0
        epsilon = .4
        ochenta_por = []
        for i in ord_porce:
            sumpor += i[2]
            ochenta_por.append(i)  ###
            if 80 - epsilon < sumpor < epsilon + 80:  # aunque solo se usan valores positivos
                break
        porcentaje=0
        for i in ochenta_por:
            porcentaje+=i[2]
        print('EL PORCENTAJE MOSTRADO ES',porcentaje)
        return ochenta_por  # obtener el 80

    direccion = ['Exports', 'Imports']
    opcii = int(input('Introduce un num entero. 1.Exports 2. Imports 3.regresar'))
    while True:
        if opcii == 1:
            ochenta_por = rutasc(direccion[0])  ####
            for elem in ochenta_por:
                print(elem)
            # print('El porcentaje de elementos mostrados es: ', porcentaje)
            opcii = int(input('Introduce un num entero. 1.Exports 2. Imports 3.regresar'))
        elif opcii == 2:
            ochenta_por = rutasc(direccion[1])  ####
            for elem in ochenta_por:
                print(elem)
            # print('El porcentaje de elementos mostrados es: ', porcentaje)
            opcii = int(input('Introduce un num entero. 1.Exports 2. Imports 3.regresar'))
        else:
            break

salir = False
opcion = 0

while not salir:

    print("1. Opcion 1 Rutas de importacion y exportacion")
    print("2. Opcion 2 Mejores medios de transporte considerando valor")
    print("3. Opcion 3 Valor total de importaciones y exportaciones")
    print("4. Salir")

    print("Elige una opcion")
    opcion=int(input("Introduce un numero entero: "))

    if opcion == 1:
        opci1()
    elif opcion == 2:
        opci2()
    elif opcion == 3:
        opci3()
    elif opcion == 4:
        salir = True
        print('Fin')
    else:
        print("Introduce un numero entre 1 y 3")






