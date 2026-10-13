nombre = input("Ingresa tu nombre: ")
ingresos = float(input("Ingresa tus ingresos mensuales: "))
gastos = float(input("Ingresa tus gastos mensuales: "))

saldo_disponible = ingresos - gastos
tiene_saldo_positivo = saldo_disponible > 0

print("\n--- PRESUPUESTO PERSONAL ---")
print(f"Usuario: {nombre}")
print(f"Ingresos: ${ingresos:.2f}")
print(f"Gastos: ${gastos:.2f}")
print(f"Saldo disponible: ${saldo_disponible:.2f}")
print(f"¿Tiene finanzas saludables?: {tiene_saldo_positivo}")