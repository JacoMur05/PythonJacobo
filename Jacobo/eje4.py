def sistema_calificaciones():
    print("=== SISTEMA DE CALIFICACIONES ===")
    
    while True:
        try:
            # 1. Solicitar la calificación al usuario
            entrada = input("\nIngresa la calificación (0.0 a 5.0): ")
            nota = float(entrada)
            
            # 2. Validar que la nota esté dentro del rango permitido
            if 0.0 <= nota <= 5.0:
                break  # Nota válida, salimos del bucle
            else:
                print("Error: La calificación debe estar obligatoriamente entre 0.0 y 5.0.")
        except ValueError:
            print("Error: Por favor, ingresa un número válido (ejemplo: 4.2).")

    # 3. Determinar el estado de aprobación
    # Nota mínima de aprobación: 3.0
    if nota >= 3.0:
        print(f"\nResultado: ¡Aprobado! Tu nota final es {nota:.1f}.")
    else:
        print(f"\nResultado: Reprobado. Tu nota final es {nota:.1f}.")

# Ejecutar el programa
if __name__ == "__main__":
    sistema_calificaciones()