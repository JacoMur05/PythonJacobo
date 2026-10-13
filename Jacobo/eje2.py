def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    
    opcion = input("\nSelecciona una opción (1-4): ")

    # Validar que la opción elegida sea válida
    if opcion in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")
            return

        # Operaciones
        if opcion == '1':
            resultado = num1 + num2
            print(f"\nResultado: {num1} + {num2} = {resultado}")
            
        elif opcion == '2':
            resultado = num1 - num2
            print(f"\nResultado: {num1} - {num2} = {resultado}")
            
        elif opcion == '3':
            resultado = num1 * num2
            print(f"\nResultado: {num1} * {num2} = {resultado}")
            
        elif opcion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"\nResultado: {num1} / {num2} = {resultado}")
            else:
                print("\nError: No se puede dividir entre cero.")
    else:
        print("\nOpción no válida. Por favor, elige un número del 1 al 4.")

# Ejecutar el programa
calculadora()