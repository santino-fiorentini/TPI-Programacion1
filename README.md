# 🌎 Trabajo Práctico Integrador – Programación I  
## Gestión de Datos de Países en Python

---

### 🏫 Datos de la Universidad y la Cátedra
**Carrera:** Tecnicatura Universitaria en Programación  
**Materia:** Programación I  
**Comisiones:** 2 y 4  
**Coordinador:** Alberto Cortez  
**Profesores:** Oscar Londero (Comisión 2) | Ana Mutti (Comisión 4)

---

### 👥 Integrantes
| Nombre | Comisión |
|---------|-----------|
| **Facundo Bailo** | Comisión 2 |
| **Santino Fiorentini** | Comisión 4 |
---

## 🧠 Descripción general del proyecto
Este proyecto es una aplicación de **gestión de países** desarrollada en Python como parte del **Trabajo Práctico Integrador de Programación I**.  
Permite **cargar, buscar, actualizar, filtrar, ordenar y analizar información de países**, almacenada en un archivo CSV persistente.  

El objetivo principal es aplicar los conceptos vistos en la materia:  
- Listas y diccionarios  
- Funciones y modularización  
- Condicionales  
- Ordenamientos  
- Estadísticas básicas  
- Manejo de archivos CSV  

---

## ⚙️ Estructura del proyecto
```
📁 Proyecto-TPI-Paises/
├── Capturas de Pantalla                # Carpeta con capturas de ejecución
├── paises_base.csv                     # Dataset base de países
├── Parte Teórica - parte-teorica.docx  # Informe teórico
├── TPI - Paises.py                     # Programa principal
└── README.md                           # Documento unificado
```

---

## 🧩 Librerías utilizadas
Librerías estándar de Python (no requiere instalación adicional):
- `os` → manejo de archivos  
- `csv` → lectura y escritura del archivo CSV  

---

## ▶️ Instrucciones de ejecución
1. Asegurarse de tener **Python 3.x** instalado.  
2. Clonar o descargar este repositorio.  
3. Ubicar `paises_base.csv` en el mismo directorio que el script principal.  
4. Ejecutar el programa con:
   ```bash
   python "TPI - Paises.py"
   ```
   5. Seguir las opciones del menú interactivo.

---

## 🧩 Ejemplos del código real

### 🟦 Listas
```python
paises = cargar_paises(UBICACION_DATA)
```

### 🟦 Diccionarios
```python
pais = {'nombre': nombre, 'poblacion': poblacion_parseada, 'superficie': superficie_parseada, 'continente': continente}
```

### 🟦 Funciones
```python
def validar_texto(texto):
	if not texto or texto.strip() == '':
		return False
	return True
```

### 🟦 Condicionales
```python
if not validar_texto(nombre):
	print("Nombre inválido.")
	return
```

### 🟦 Ordenamientos
```python
def ordenar_por_poblacion(paises):
	poblacion = sorted(paises, key=obtener_poblacion, reverse=True)
	for pais in poblacion:
		mostrar_pais(pais)
	return poblacion
```

### 🟦 Estadísticas básicas
```python
def estadistica_promedio_poblacion(paises):
    if not paises:
        print("No hay países para calcular el promedio de población.")
        return
    total_poblacion = sum(p['poblacion'] for p in paises)
    promedio_poblacion = total_poblacion / len(paises)
    print(f"El promedio de población de los países es {promedio_poblacion:.2f} habitantes.")
```

### 🟦 Archivos CSV
```python
with open(dataset, 'r', encoding='utf-8') as archivo:
	reader = csv.DictReader(archivo)
	for indice, registro in enumerate(reader):
		pais = validar_y_parsear_registro(registro)
		if pais:
			paises.append(pais)
		else:
			print(f"Registro inválido en la fila {indice + 2}")
```

---

## 🧮 Ejemplos de ejecución

### ➕ Agregar país
**Entrada:**
```
Ingrese el nombre del país: Paraguay
Ingrese la población del país: 7132530
Ingrese la superficie del país: 406752
Ingrese el continente del país: América
```
**Salida:**
```
País 'Paraguay' agregado correctamente.
```

---

### 🔍 Buscar país
**Entrada:**
```
Ingrese el nombre del país que desea buscar: arg
```
**Salida:**
```
El país 'Argentina' fue encontrado en el índice 0.
Argentina - 45376763 habitantes - 2780400 km^2 - América
```

---

### 📊 Promedio de población
**Salida:**
```
El promedio de población de los países es 128,237,800 habitantes.
```

---

## 🧾 Conclusión grupal
Durante el desarrollo de este trabajo aplicamos de forma integrada los contenidos de **Programación I**, utilizando listas, diccionarios, funciones, condicionales y manejo de archivos CSV.  
Logramos construir un sistema funcional que permite gestionar datos reales y generar estadísticas automáticas.  
El trabajo en equipo permitió dividir tareas, validar resultados y mejorar la claridad del código.  
Como mejora futura, se podría agregar manejo de excepciones más avanzado y una interfaz gráfica simple para la interacción con el usuario.

---

## 🗺️ Diagrama de flujo
![Diagrama de flujo](Capturas%20de%20Pantalla/diagrama_flujo_tpi.jpg)

---

## 📘 Fuentes bibliográficas
- Material de Cátedra de la materia Programación 1
---

## 🎥 Enlaces
- **Video de presentación:** *(Agregar link una vez publicado)*  
