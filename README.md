# Programa_python_ejercicio5
# Matriz que registra las horas trabajadas por un equipo durante la semana, mostrando como salida el nombre del trabajador, las horas trabajadas y su clasificación de jornada.
# DATOS DEL TRABAJO
# Lesly Yulieth Piragauta Patiño
# Fundamentos de programación
# Fase 5 - Evaluación Final POA
# Ejercicio 5


# Matriz con las horas trabajadas durante la semana
matriz_horas = [
    ["Sandra", 8, 8, 8, 8, 8],
    ["Mario", 9, 8, 8, 9, 8],
    ["Alexandra", 7, 8, 8, 8, 7],
    ["Willian", 10, 9, 9, 8, 8]
]


# suma del total de horas semanales
def calcular_total_horas(recurso):
    total = 0

    for hora in recurso[1:]:
        total += hora

    return total


# Clasificación la jornada laboral
def clasificar_jornada(total):
    if total > 40:
        return "Sobretiempo"
    else:
        return "Horario estándar"


# Reporte
print("REPORTE DE HORAS SEMANALES")
print("--------------------------------")

for recurso in matriz_horas:
    nombre = recurso[0]

    total = calcular_total_horas(recurso)

    jornada = clasificar_jornada(total)

    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", jornada)
    print("--------------------------------")
    
# Salida del ejercicio
REPORTE DE HORAS SEMANALES
--------------------------------
Nombre: Sandra
Total de horas: 40
Clasificación: Horario estándar
--------------------------------
Nombre: Mario
Total de horas: 42
Clasificación: Sobretiempo
--------------------------------
Nombre: Alexandra
Total de horas: 38
Clasificación: Horario estándar
--------------------------------
Nombre: Willian
Total de horas: 44
Clasificación: Sobretiempo
--------------------------------
