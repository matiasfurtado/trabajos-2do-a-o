#Ejercicio 20

def registrar_movimientos():

    pila_movimientos = []
    
    print("--- INICIO DE REGISTRO ---")
    print("Direcciones: N, S, E, O, NE, NO, SE, SO (Escriba 'FIN' para salir)")
    
    while True:
        direccion = input("\nDirección: ").upper()
        
        if direccion == "FIN":
            break
            
        pasos = int(input("Cantidad de pasos: "))
        
        pila_movimientos.append([pasos, direccion])
        
    return pila_movimientos

def vuelta(pila_ida):
    opuestos = {
        "N": "S", "S": "N", "E": "O", "O": "E",
        "NE": "SO", "NO": "SE", "SE": "NO", "SO": "NE"
    }
    
    print("\n--- GENERANDO CAMINO DE REGRESO ---")
    
    while len(pila_ida) > 0:
        ultimo_movimiento = pila_ida.pop()
        
        pasos = ultimo_movimiento[0]
        direccion_ida = ultimo_movimiento[1]
        
        direccion_vuelta = opuestos[direccion_ida]
        
        print(f"Mover {pasos} pasos hacia el {direccion_vuelta}")
        
# Paso 1: El robot se mueve y se registra
recorrido = registrar_movimientos()

# Paso 2: El robot vuelve al origen usando la pila
if len(recorrido) > 0:
    vuelta(recorrido)
else:
    print("No se registraron movimientos.")



