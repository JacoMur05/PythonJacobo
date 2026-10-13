from datetime import datetime

# 1. Solicitar el nombre al usuario
nombre = input("Por favor, ingresa tu nombre: ")

# 2. Obtener la fecha de ejecución
fecha_actual = datetime.now().strftime("%d/%m/%Y")

# 3. Mostrar el mensaje de bienvenida y la fecha
print(f"\n¡Hola, {nombre}! Bienvenido/a a tu primer programa.")
print(f"Fecha de ejecución: {fecha_actual}")