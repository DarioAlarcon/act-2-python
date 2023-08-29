import logic
def main():
    print("Seleccione la acción:")
    print("1. Calcular cuadrado de números")
    print("2. Calcular factorial usando expresión lambda")
    print("3. Calcular factorial usando recursión")
    print("4. Calcular suma de números")
    print("5. Calcular promedio de números")
    option = int(input("Ingrese el número de la acción deseada: "))
    numbers = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

    result = logic.calculate_action(option, numbers)
    print("Resultado:", result)

    if logic.to_continue():
        main()

main()