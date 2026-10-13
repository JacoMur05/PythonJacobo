# 1. Entrada de datos (convertimos la entrada a float para permitir decimales)
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

# 2. Operaciones matemáticas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

# Para la división verificamos que el segundo número no sea cero para evitar errores
if num2 != 0:
    division = num1 / num2
else:
    division = "No se puede dividir entre cero"

# 3. Salida por pantalla
print("\n--- RESULTADOS ---")
print(f"Suma ({num1} + {num2}): {suma}")
print(f"Resta ({num1} - {num2}): {resta}")
print(f"Multiplicación ({num1} * {num2}): {multiplicacion}")
print(f"División ({num1} / {num2}): {division}") 
