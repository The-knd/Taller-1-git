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

if __name__ == "__main__":
    with open("../estudiantes.csv",mode="r") as file:
        depurar_datos(file)

