def apply_function_to_list(function, number_list):
    return list(map(function, number_list))

factorial_lambda = lambda n: 1 if n == 0 else n * factorial_lambda(n - 1)

def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)

def calculate_square(x):
    return x ** 2

def calculate_action(option, numbers):
    if option == 1:
        return apply_function_to_list(calculate_square, numbers)
    elif option == 2:
        return apply_function_to_list(factorial_lambda, numbers)
    elif option == 3:
        return apply_function_to_list(recursive_factorial, numbers)
    elif option == 4:
        return sum(numbers)
    elif option == 5:
        total = sum(numbers)
        return total / len(numbers)
    else:
        return "Opción no válida"

def to_continue():
    answer = input("¿Desea realizar otra acción? (s/n): ").lower()
    return answer == 's'
