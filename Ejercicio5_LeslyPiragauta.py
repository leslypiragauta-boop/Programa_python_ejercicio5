# DATOS DEL TRABAJO
# Lesly Yulieth Piragauta Patiño
# Fundamentos de programación
# Fase 5 - Evaluación Final POA 
# Ejercicio 5


# Horas trabajadas durante la semana
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

