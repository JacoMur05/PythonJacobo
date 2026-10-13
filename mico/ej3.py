from datetime import datetime

print("=== SISTEMA DE PRESUPUESTO PERSONAL ===")
print(f"Fecha de registro: {datetime.now().strftime('%d/%m/%Y')}\n")

# 1. Entrada de datos de Ingresos
print("--- REGISTRO DE INGRESOS ---")
ingreso_principal = float(input("Ingresa tu ingreso principal (ej. Salario): $"))
ingreso_adicional = float(input("Ingresa otros ingresos adicionales: $"))

# 2. Entrada de datos de Gastos
print("\n--- REGISTRO DE GASTOS ---")
gasto_fijo = float(input("Ingresa tus gastos fijos (ej. Renta, Servicios): $"))
gasto_variable = float(input("Ingresa tus gastos variables (ej. Comida, Ocio): $"))
ahorro_deseado = float(input("Ingresa el monto que deseas destinar a ahorro: $"))

# 3. Operaciones Matemáticas
total_ingresos = ingreso_principal + ingreso_adicional
total_gastos = gasto_fijo + gasto_variable + ahorro_deseado
saldo_disponible = total_ingresos - total_gastos

# 4. Salida por pantalla y Resumen
print("\n=======================================")
print("          RESUMEN FINANCIERO           ")
print("=======================================")
print(f"Total de Ingresos:   ${total_ingresos:,.2f}")
print(f"Total de Gastos:     ${total_gastos:,.2f}")
print("---------------------------------------")
print(f"Saldo Disponible:    ${saldo_disponible:,.2f}")
print("=======================================")

# Diagnóstico del estado financiero
if saldo_disponible > 0:
    print("STATUS: ¡Excelente! Tienes un superávit financiero.")
elif saldo_disponible == 0:
    print("STATUS: Atención, estás justo en el límite (gastas exactamente lo que ganas).")
else:
    print("STATUS: ¡Alerta! Tienes un déficit financiero. Tus gastos superan tus ingresos.")
    