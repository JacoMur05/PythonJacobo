def calcular_costo_evento(alquiler, materiales, transporte, alimentacion):
    costo_total = alquiler + materiales + transporte + alimentacion
    return costo_total


costo_alquiler = float(input("Ingresa el costo del alquiler: "))
costo_materiales = float(input("Ingresa el costo de los materiales: "))
costo_transporte = float(input("Ingresa el costo del transporte: "))
costo_alimentacion = float(input("Ingresa el costo de la alimentación: "))

total = calcular_costo_evento(
    costo_alquiler, costo_materiales, costo_transporte, costo_alimentacion
)

print(f"\nEl costo total del evento es: ${total:.2f}")