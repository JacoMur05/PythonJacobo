def sistema_presupuesto():
    print("=== SISTEMA DE PRESUPUESTO PERSONAL ===\n")

    # 1. Captura de Ingresos
    print("--- REGISTRO DE INGRESOS ---")
    ingresos = []
    while True:
        fuente = input("Nombre del ingreso (o presiona Enter para finalizar): ").strip()
        if not fuente:
            break
        try:
            monto = float(input(f"Monto para '{fuente}': $"))
            if monto < 0:
                print("El monto no puede ser negativo. Inténtalo de nuevo.")
                continue
            ingresos.append({"fuente": fuente, "monto": monto})
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

    # 2. Captura de Gastos
    print("\n--- REGISTRO DE GASTOS ---")
    gastos = []
    while True:
        concepto = input("Nombre del gasto (o presiona Enter para finalizar): ").strip()
        if not concepto:
            break
        try:
            monto = float(input(f"Monto para '{concepto}': $"))
            if monto < 0:
                print("El monto no puede ser negativo. Inténtalo de nuevo.")
                continue
            gastos.append({"concepto": concepto, "monto": monto})
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número válido.")

    # 3. Cálculos
    total_ingresos = sum(item["monto"] for item in ingresos)
    total_gastos = sum(item["monto"] for item in gastos)
    saldo_disponible = total_ingresos - total_gastos
    tasa_ahorro = ((saldo_disponible / total_ingresos) * 100) if total_ingresos > 0 else 0.0

    # 4. Presentación de Resultados
    print("\n" + "=" * 40)
    print("         RESUMEN FINANCIERO          ")
    print("=" * 40)

    print("\n[INGRESOS]")
    if ingresos:
        for item in ingresos:
            print(f"  • {item['fuente']:<20}: ${item['monto']:>10,.2f}")
    else:
        print("  No se registraron ingresos.")
    print(f"  TOTAL INGRESOS      : ${total_ingresos:>10,.2f}")

    print("\n[GASTOS]")
    if gastos:
        for item in gastos:
            print(f"  • {item['concepto']:<20}: ${item['monto']:>10,.2f}")
    else:
        print("  No se registraron gastos.")
    print(f"  TOTAL GASTOS        : ${total_gastos:>10,.2f}")

    print("-" * 40)
    print(f"  SALDO DISPONIBLE    : ${saldo_disponible:>10,.2f}")
    print(f"  TASA DE AHORRO      : {tasa_ahorro:>10.1f}%")
    print("=" * 40)

    # Diagnóstico del saldo
    if saldo_disponible > 0:
        print("\n¡Presupuesto superavitario! Tienes un saldo a favor.")
    elif saldo_disponible == 0:
        print("\nPresupuesto equilibrado: tus ingresos cubren exactamente tus gastos.")
    else:
        print("\n¡Atención! Presupuesto deficitario: tus gastos superan tus ingresos.")

# Ejecutar el programa
if __name__ == "__main__":
    sistema_presupuesto()