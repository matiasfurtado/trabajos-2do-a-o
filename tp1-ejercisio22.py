#trabajo practico 1: ejercisio 22.
#Debera resolver los ejercicios 5 y 22 de la guia de ejercicios de recursividad del libro, subirlos a github y pasar el link en la entrega.
def usar_la_fuerza(mochila,objetos_sacados=0):
    #La mochila está vacía
    if len(mochila) == 0:
        return False, objetos_sacados

    #Sacamos un objeto a la vez
    objeto_actual = mochila[0]
    objetos_sacados += 1

    print(f"Extrayendo objeto {objetos_sacados}: {objeto_actual}...")

    #Determinar si es el sable de luz
    if objeto_actual == "sable de luz":
        return True, objetos_sacados

    #Llamada recursiva
    return usar_la_fuerza(mochila[1:], objetos_sacados)

#Objetos en la mochila
mi_mochila = ["comida", "venda", "grogu", "blaster", "sable de luz", "mapa"]

#Ejecución de la función
encontrado, total = usar_la_fuerza(mi_mochila)

#Mostrar resultados finales
print("---------------")
if encontrado:
    print(f"Sable de luz encontrado")
    print(f"Cantidad de objetos extraídos: {total}")
else:
    print("El sable de luz no se encuentra en esta mochila.")