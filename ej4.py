# 1. Entrada de datos
nota = float(input("Ingresa la calificación del estudiante (0.0 a 5.0): "))

# 2. Validación de rango (debe estar entre 0 y 5)
if nota < 0.0 or nota > 5.0:
    print("\n❌ Error: La calificación ingresada no es válida. Debe estar entre 0.0 y 5.0.")
else:
    # 3. Determinación de aprobación (la nota mínima aprobatoria suele ser 3.0)
    print(f"\nCalificación ingresada: {nota:.1f}")
    
    if nota >= 3.0:
        print("RESULTADO: ¡Felicidades! El estudiante ha APROBADO. 🎉")
    else:
        print("RESULTADO: El estudiante ha REPROBADO. ❌")