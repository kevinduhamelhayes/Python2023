"""vamos a mostrar la serie de fibonacci"""
print("cuantos numeros de fibonacci quieres?")
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

cantidad = int(input("¿Cuántos números de la serie Fibonacci desea ver? "))

print(list(fibonacci(cantidad)))

