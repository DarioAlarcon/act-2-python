def aplicar_funcion_a_lista(funcion, lista):
    return list(map(funcion, lista))

factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def calcular_cuadrado(x):
    return x ** 2

def calcular_accion(opcion, numeros):
    if opcion == 1:
        return aplicar_funcion_a_lista(calcular_cuadrado, numeros)
    elif opcion == 2:
        return aplicar_funcion_a_lista(factorial_lambda, numeros)
    elif opcion == 3:
        return aplicar_funcion_a_lista(factorial_recursivo, numeros)
    elif opcion == 4:
        return sum(numeros)
    elif opcion == 5:
        total = sum(numeros)
        return total / len(numeros)
    else:
        return "Opción no válida"

def continuar():
    respuesta = input("¿Desea realizar otra acción? (s/n): ").lower()
    return respuesta == 's'

def main():
    print("Seleccione la acción:")
    print("1. Calcular cuadrado de números")
    print("2. Calcular factorial usando expresión lambda")
    print("3. Calcular factorial usando recursión")
    print("4. Calcular suma de números")
    print("5. Calcular promedio de números")
    opcion = int(input("Ingrese el número de la acción deseada: "))
    numeros = list(map(int, input("Ingrese una lista de números separados por espacios: ").split()))

    resultado = calcular_accion(opcion, numeros)
    print("Resultado:", resultado)

    if continuar():
        main()

main()