from estudiantes.registro import depurar_datos, mostrar_estudiantes, calcular_promedio

def main():

    with open("estudiantes.csv",mode="r") as file:
        est_valid = depurar_datos(file)
        mostrar_estudiantes(est_valid)
        print()
        print("Promedio:",calcular_promedio(est_valid))
    

if __name__ == "__main__":
    main()

