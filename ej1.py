from datetime import datetime

print("=== BIENVENIDO A MI PRIMER PROGRAMA ===")

nombre_usuario = input("Por favor, ingresa tu nombre: ")

fecha_actual = datetime.now()
fecha_formateada = fecha_actual.strftime("%d/%m/%Y")

print("\n----------------------------------------")
print(f"¡Hola, {nombre_usuario}! Es un placer saludarte.")
print(f"La fecha de ejecución de este programa es: {fecha_formateada}")
print("----------------------------------------")