#Cristian Uriel Nava Ibañez 
# programa redondo de ferrocarril
destino1 = "Acapulco"
precio1 = 350

destino2 = "Michoacan"
precio2 = 850

print("AGENCIA DE VIAJES")
print("1.", destino1, "- $", precio1)
print("2.", destino2, "- $", precio2)

opcion = int(input("Elige el destino (1 o 2): "))
pasajeros = int(input("Ingresa el numero de pasajeros: "))

if opcion == 1:
    destino = destino1
    costo_pasajero = precio1
else:
    destino = destino2
    costo_pasajero = precio2

total_pagar = pasajeros * costo_pasajero

print("\nRESUMEN DEL VIAJE")
print("Destino:", destino)
print("Pasajeros:", pasajeros)
print("Costo por pasajero: $", costo_pasajero)
print("Total a pagar: $", total_pagar)