nota = float(input("Ingresa la calificación: "))

if nota < 0 or nota > 5:
    print("Error: La calificación debe estar entre 0 y 5.")
elif nota >= 3.0:
    print("El estudiante aprobó.")
else:
    print("El estudiante reprobó.")