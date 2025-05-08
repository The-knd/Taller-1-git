import csv

def depurar_datos(file_est):
    estudiantes_validos=[]
    reader = csv.DictReader(file_est)
    for row in reader:
        nombre = row['nombre']
        try:
            nota = float(row['nota'])
            if 0.0 <= nota <= 5.0:
                estudiantes_validos.append({'nombre': nombre, 'nota': nota})
        except ValueError:
            continue
    return estudiantes_validos

def mostrar_estudiantes(estudiantes):
    estudiantes_ordenados = sorted(estudiantes, key=lambda x: x['nombre'])
    print(f"{'Nombre':<20} {'Nota':<5}")
    print("-" * 25)
    for estudiante in estudiantes_ordenados:
        print(f"{estudiante['nombre']:<20} {estudiante['nota']:<5.2f}")

def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0.0
    total = sum(estudiante['nota'] for estudiante in estudiantes)
    return total / len(estudiantes)

if __name__ == "__main__":
    with open("../estudiantes.csv",mode="r") as file:
        est_valid = depurar_datos(file)
        mostrar_estudiantes(est_valid)
        print()
        calcular_promedio(est_valid)

