def calculadora():
    print("=== CALCULADORA BÁSICA ===")
    print("1. Sumar (+)")
    print("2. Restar (-)")
    print("3. Multiplicar (*)")
    print("4. Dividir (/)")
    print("5. Residuo (%)")
    
    opcion = input("\nSelecciona una opción (1-5): ")

    # Validar que la opción elegida sea válida
    if opcion in ['1', '2', '3', '4', '5']:
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

        elif opcion == '5':
            if num2 != 0:
                resultado = num1 % num2
                print(f"\nResultado: {num1} % {num2} = {resultado}")
            else:
                print("\nError: No se puede calcular el residuo con división entre cero.")
    else:
        print("\nOpción no válida. Por favor, elige un número del 1 al 5.")

# Ejecutar el programa
calculadora()