# TRABAJO PRÁCTICO INTEGRADOR - Facundo Bailo y Santino Fiorentini

import os
import csv

def validar_texto(texto):
	if not texto or texto.strip() == '':
		return False
	return True

def validar_y_parsear_opcion_menu(opcion):
	opcion = opcion.strip()
	if not opcion.isdigit():
		return None
	return int(opcion)

def validar_y_parsear_numero(texto, tipo=int):
    if not validar_texto(texto):
        return None
    texto = texto.strip()
    if not texto.replace('.', '').isdigit():
        return None
    numero = float(texto)
    if tipo == int:
        return int(numero)
    return numero

def validar_y_parsear_registro(registro):
	nombre = registro.get('nombre')
	poblacion = registro.get('poblacion')
	superficie = registro.get('superficie')
	continente = registro.get('continente')
	es_valido = (validar_texto(nombre) and validar_y_parsear_numero(poblacion, int) and validar_y_parsear_numero(superficie, int) and validar_texto(continente))
	if not es_valido:
		return None
	return {'nombre': nombre, 'poblacion': int(poblacion), 'superficie': int(superficie), 'continente': continente}

def parsear_nombre(nombre):
	nombre = nombre.lower().replace('á', 'a').replace('é', 'e').replace('í', 'i').replace('ó', 'o').replace('ú', 'u')
	return nombre

def crear_archivo(dataset):
	with open(dataset, 'w', newline='', encoding='utf-8') as archivo:
		writer = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
		writer.writeheader()
		print(f"Archivo {dataset} creado correctamente.")
	return

def agregar_pais_en_archivo(dataset, registro):
	with open(dataset, 'a', newline='', encoding='utf-8') as archivo:
		writer = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
		writer.writerow(registro)
	return

def cargar_paises(dataset):
	paises = []
	if os.path.exists(dataset):
		with open(dataset, 'r', encoding='utf-8') as archivo:
			reader = csv.DictReader(archivo)
			for indice, registro in enumerate(reader):
				pais = validar_y_parsear_registro(registro)
				if pais:
					paises.append(pais)
				else:
					print(f"Registro inválido en la fila {indice + 2}")
		print(f"Se cargaron {len(paises)} paises.")
	else:
		print(f"Error al cargar los paises: {dataset} no existe. Creando archivo...")
		crear_archivo(dataset)
	return paises

def mostrar_pais(pais):
	print(f"{pais['nombre']} - {pais['poblacion']} habitantes - {pais['superficie']} km^2 - {pais['continente']}")

def mostrar_paises(paises):
	if not paises:
		print("No hay paises para listar.")
		return
	print(f"Lista de {len(paises)} paises:")
	for pais in paises:
		mostrar_pais(pais)

def agregar_pais(paises, dataset):
    nombre = input("Ingrese el nombre del pais: ").strip()
    if not validar_texto(nombre):
        print("Nombre inválido.")
        return
    for pais in paises:
        if parsear_nombre(pais['nombre']) == parsear_nombre(nombre):
            print(f"El país '{nombre}' ya fue agregado previamente.")
            return
    poblacion = input("Ingrese la población del pais: ")
    poblacion_parseada = validar_y_parsear_numero(poblacion, int)
    if not poblacion_parseada:
        print("Población inválida.")
        return
    superficie = input("Ingrese la superficie del pais: ")
    superficie_parseada = validar_y_parsear_numero(superficie, int)
    if not superficie_parseada:
        print("Superficie inválida.")
        return
    continente = input("Ingrese el continente del pais: ").strip()
    if not validar_texto(continente):
        print("Continente inválido.")
        return
    pais = {'nombre': nombre, 'poblacion': poblacion_parseada, 'superficie': superficie_parseada, 'continente': continente}
    if os.path.exists(dataset):
        agregar_pais_en_archivo(dataset, pais)
    else:
        print(f"Error al agregar el pais. El archivo {dataset} no existe. Creando archivo...")
        crear_archivo(dataset)
        agregar_pais_en_archivo(dataset, pais)
    paises.append(pais)
    print(f"País '{nombre}' agregado correctamente.")

def actualizar_pais(paises, dataset):
	pais, indice = buscar_pais(paises)
	if not pais:
		print("Pais no encontrado.")
		return
	poblacion = input("Ingrese la nueva población: ")
	poblacion_parseada = validar_y_parsear_numero(poblacion, int)
	if not poblacion_parseada:
		print("Población inválida.")
		return
	superficie = input("Ingrese la nueva superficie: ")
	superficie_parseada = validar_y_parsear_numero(superficie, int)
	if not superficie_parseada:
		print("Superficie inválida.")
		return
	pais.update({'poblacion': poblacion_parseada, 'superficie': superficie_parseada})
	if os.path.exists(dataset):
		paises[indice] = pais
		with open(dataset, 'w', newline='', encoding='utf-8') as archivo:
			writer = csv.DictWriter(archivo, fieldnames=['nombre', 'poblacion', 'superficie', 'continente'])
			writer.writeheader()
			writer.writerows(paises)
		print("Pais actualizado correctamente.")
	else:
		print(f"Error al actualizar el pais. El archivo {dataset} no existe.")
	return

def buscar_pais(paises):
    pais_buscado = input("Ingrese el nombre del país que desea buscar: ").strip()
    pais_buscado_parseado = parsear_nombre(pais_buscado)
    for i, pais in enumerate(paises):
        nombre_parseado = parsear_nombre(pais["nombre"])
        if pais_buscado_parseado in nombre_parseado:
            print(f"El país '{pais['nombre']}' fue encontrado en el índice {i}.")
            mostrar_pais(pais)
            return pais, i
    print(f"No se encontró el país '{pais_buscado}'.")
    return None, None

def filtrar_por_continente(paises):
    continente = input("Ingrese el continente: ")
    if not validar_texto(continente):
        print("Continente inválido.")
        return
    continente = parsear_nombre(continente)
    paises_filtrados = [pais for pais in paises if parsear_nombre(pais['continente']) == continente]
    return paises_filtrados

def filtrar_por_rango_poblacion(paises):
    poblacion_minima = input("Ingrese la población mínima: ")
    poblacion_maxima = input("Ingrese la población máxima: ")
    poblacion_minima_parseada = validar_y_parsear_numero(poblacion_minima, int)
    if poblacion_minima_parseada is None:
        print("Población mínima inválida.")
        return
    poblacion_maxima_parseada = validar_y_parsear_numero(poblacion_maxima, int)
    if poblacion_maxima_parseada is None:
        print("Población máxima inválida.")
        return
    if poblacion_minima_parseada > poblacion_maxima_parseada:
        print("La población mínima debe ser menor que la máxima.")
        return
    paises_filtrados = [pais for pais in paises if poblacion_minima_parseada <= pais['poblacion'] <= poblacion_maxima_parseada]
    return paises_filtrados

def filtrar_por_rango_superficie(paises):
    superficie_minima = input("Ingrese la superficie mínima: ")
    superficie_maxima = input("Ingrese la superficie máxima: ")
    superficie_minima_parseada = validar_y_parsear_numero(superficie_minima, int)
    if superficie_minima_parseada is None:
        print("Superficie mínima inválida.")
        return
    superficie_maxima_parseada = validar_y_parsear_numero(superficie_maxima, int)
    if superficie_maxima_parseada is None:
        print("Superficie máxima inválida.")
        return
    if superficie_minima_parseada > superficie_maxima_parseada:
        print("La superficie mínima debe ser menor que la máxima.")
        return
    paises_filtrados = [pais for pais in paises if superficie_minima_parseada <= pais['superficie'] <= superficie_maxima_parseada]
    return paises_filtrados

def filtrar_paises(paises):
	print("Filtrar países por:")
	print("1) Continente")
	print("2) Rango de población")
	print("3) Rango de superficie")
	print("4) Volver al menú principal")
	while True:
		opcion = validar_y_parsear_opcion_menu(input("Ingrese la opción de filtrado: "))
		match opcion:
			case 1:
				mostrar_paises(filtrar_por_continente(paises))
				break
			case 2:
				mostrar_paises(filtrar_por_rango_poblacion(paises))
				break
			case 3:
				mostrar_paises(filtrar_por_rango_superficie(paises))
				break
			case 4:
				break
			case _:
				print("Opción inválida.")

def obtener_nombre(pais):
	return pais["nombre"]

def obtener_poblacion(pais):
	return pais["poblacion"]

def obtener_superficie(pais):
	return pais["superficie"]

def ordenar_por_nombre(paises):
	paises_ordenados = sorted(paises, key=obtener_nombre)
	for pais in paises_ordenados:
		mostrar_pais(pais)
	return paises_ordenados

def ordenar_por_poblacion(paises):
	poblacion = sorted(paises, key=obtener_poblacion, reverse=True)
	for pais in poblacion:
		mostrar_pais(pais)
	return poblacion

def ordenar_por_superficie(paises, descendente=True):
	superficie = sorted(paises, key=obtener_superficie, reverse=descendente)
	for pais in superficie:
		mostrar_pais(pais)
	return superficie

def ordenar_paises(paises):
	print("Ordenar países por:")
	print("1) Nombre")
	print("2) Población")
	print("3) Superficie (ascendente)")
	print("4) Superficie (descendente)")
	print("5) Volver al menú principal")
	while True:
		opcion = validar_y_parsear_opcion_menu(input("Ingrese la opción de ordenamiento: "))
		match opcion:
			case 1:
				ordenar_por_nombre(paises)
				break
			case 2:
				ordenar_por_poblacion(paises)
				break
			case 3:
				ordenar_por_superficie(paises, descendente=False)
				break
			case 4:
				ordenar_por_superficie(paises, descendente=True)
				break
			case 5:
				break
			case _:
				print("Opción inválida.")

def mostrar_estadisticas(paises):
	print("Mostrar estadísticas:")
	print("1) País con mayor y menor población")
	print("2) Promedio de población")
	print("3) Promedio de superficie")
	print("4) Cantidad de países por continente")
	print("5) Volver al menú principal")
	while True:
		opcion = validar_y_parsear_opcion_menu(input("Ingrese la opción de estadística: "))
		match opcion:
			case 1:
				estadistica_mayor_y_menor_poblacion(paises)
				break
			case 2:
				estadistica_promedio_poblacion(paises)
				break
			case 3:
				estadistica_promedio_superficie(paises)
				break
			case 4:
				estadistica_cantidad_paises_por_continente(paises)
				break
			case 5:
				break
			case _:
				print("Opción inválida.")

def estadistica_mayor_y_menor_poblacion(paises):
    if not paises:
        print("No hay países para mostrar estadísticas.")
        return
    mayor_poblacion = None
    menor_poblacion = None
    for pais in paises:
        if mayor_poblacion is None or pais['poblacion'] > mayor_poblacion['poblacion']:
            mayor_poblacion = pais
        if menor_poblacion is None or pais['poblacion'] < menor_poblacion['poblacion']:
            menor_poblacion = pais
    print(f"El país con mayor población es {mayor_poblacion['nombre']} con {mayor_poblacion['poblacion']} habitantes.")
    print(f"El país con menor población es {menor_poblacion['nombre']} con {menor_poblacion['poblacion']} habitantes.")

def estadistica_promedio_poblacion(paises):
    if not paises:
        print("No hay países para calcular el promedio de población.")
        return
    total_poblacion = sum(p['poblacion'] for p in paises)
    promedio_poblacion = total_poblacion / len(paises)
    print(f"El promedio de población de los países es {promedio_poblacion:.2f} habitantes.")

def estadistica_promedio_superficie(paises):
    if not paises:
        print("No hay países para calcular el promedio de superficie.")
        return
    total_superficie = sum(p['superficie'] for p in paises)
    promedio_superficie = total_superficie / len(paises)
    print(f"El promedio de superficie de los países es {promedio_superficie:.2f} km^2.")

def estadistica_cantidad_paises_por_continente(paises):
    if not paises:
        print("No hay países para mostrar la cantidad por continente.")
        return
    cantidad_paises_por_continente = {}
    for pais in paises:
        cantidad_paises_por_continente[pais['continente']] = cantidad_paises_por_continente.get(pais['continente'], 0) + 1
    for continente, cantidad in cantidad_paises_por_continente.items():
        print(f"{continente} tiene {cantidad} países.")

def menu():
	print("\nMenú principal:")
	print("1) Agregar un país")
	print("2) Actualizar un país")
	print("3) Buscar un país")
	print("4) Filtrar países")
	print("5) Ordenar países")
	print("6) Mostrar estadísticas")
	print("7) Salir")
	opcion = input("Ingrese una opcion: ")
	return validar_y_parsear_opcion_menu(opcion)

def inicio():
	UBICACION_DATA = 'paises_base.csv'
	paises = cargar_paises(UBICACION_DATA)
	while True:
		opc = menu()
		match opc:
			case 1:
				agregar_pais(paises=paises, dataset=UBICACION_DATA)
			case 2:
				actualizar_pais(paises=paises, dataset=UBICACION_DATA)
			case 3:
				buscar_pais(paises)
			case 4:
				filtrar_paises(paises)
			case 5:
				ordenar_paises(paises)
			case 6:
				mostrar_estadisticas(paises)
			case 7:
				print("Programa finalizado.")
				break
			case _:
				print("Opción inválida.")

inicio()