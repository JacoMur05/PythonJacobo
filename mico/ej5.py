def calcular_costo_evento(alquiler, materiales, transporte, alimentacion):
    """
    Calcula el costo total de un evento sumando todos los rubros.
    Retorna un diccionario con el desglose y el costo total.
    """
    total = alquiler + materiales + transporte + alimentacion
    
    return {
        "alquiler": alquiler,
        "materiales": materiales,
        "transporte": transporte,
        "alimentacion": alimentacion,
        "total": total
    }

# --- PROGRAMA PRINCIPAL ---
print("=== CALCULADORA DE COSTOS DE EVENTOS ===\n")

# 1. Entrada de datos por parte del usuario
gastos_alquiler = float(input("Costo de alquiler del salón/lugar: $"))
gastos_materiales = float(input("Costo de materiales y decoración: $"))
gastos_transporte = float(input("Costo de transporte y logística: $"))
gastos_alimentacion = float(input("Costo de alimentación/catering: $"))

# 2. Llamada a la función
resumen = calcular_costo_evento(
    alquiler=gastos_alquiler,
    materiales=gastos_materiales,
    transporte=gastos_transporte,
    alimentacion=gastos_alimentacion
)

# 3. Salida de resultados por pantalla
print("\n==========================================")
print("          DESGLOSE DEL PRESUPUESTO        ")
print("==========================================")
print(f"Alquiler:       ${resumen['alquiler']:,.2f}")
print(f"Materiales:     ${resumen['materiales']:,.2f}")
print(f"Transporte:     ${resumen['transporte']:,.2f}")
print(f"Alimentación:   ${resumen['alimentacion']:,.2f}")
print("------------------------------------------")
print(f"COSTO TOTAL:    ${resumen['total']:,.2f}")
print("==========================================")