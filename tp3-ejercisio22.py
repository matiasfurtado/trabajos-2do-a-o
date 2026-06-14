from collections import deque

# 1. Definición de la estructura de datos (usando una clase simple)
class PersonajeMCU:
    def __init__(self, personaje, superheroe, genero):
        self.personaje = personaje
        self.superheroe = superheroe
        self.genero = genero  # 'M' o 'F'

    def __str__(self):
        return f"{{Personaje: {self.personaje}, Héroe: {self.superheroe}, Género: {self.genero}}}"


# 2. Función principal para resolver las actividades
def resolver_actividades_mcu(cola_original):
    # Cola auxiliar para no perder los datos al procesar
    cola_aux = deque()
    
    # Variables para almacenar resultados de búsquedas específicas
    nombre_capitana_marvel = "No encontrado"
    heroe_scott_lang = "No encontrado"
    carol_danvers_encontrada = False
    heroe_carol_danvers = ""
    
    # Listas para acumular los datos de los incisos de tipo "mostrar listado"
    superheroes_femeninos = []
    personajes_masculinos = []
    comienzan_con_s = []
    
    # Procesamos la cola vaciándola temporalmente
    while len(cola_original) > 0:
        actual = cola_original.popleft()
        
        # a. Determinar el nombre del personaje de Capitana Marvel
        if actual.superheroe == "Capitana Marvel":
            nombre_capitana_marvel = actual.personaje
            
        # b. Mostrar los nombres de los superhéroes femeninos
        if actual.genero == 'F':
            superheroes_femeninos.append(actual.superheroe)
            
        # c. Mostrar los nombres de los personajes masculinos
        if actual.genero == 'M':
            personajes_masculinos.append(actual.personaje)
            
        # d. Determinar el nombre del superhéroe de Scott Lang
        if actual.personaje == "Scott Lang":
            heroe_scott_lang = actual.superheroe
            
        # e. Mostrar todos los datos cuyos nombres comienzan con 'S'
        if actual.personaje.startswith('S') or actual.superheroe.startswith('S'):
            comienzan_con_s.append(actual)
            
        # f. Determinar si Carol Danvers está en la cola e indicar su superhéroe
        if actual.personaje == "Carol Danvers":
            carol_danvers_encontrada = True
            heroe_carol_danvers = actual.superheroe
            
        # Guardamos en la cola auxiliar para preservar el elemento
        cola_aux.append(actual)
        
    # Restauramos la cola original a su estado inicial
    while len(cola_aux) > 0:
        cola_original.append(cola_aux.popleft())
        
    # --- IMPRESIÓN DE RESULTADOS ---
    print("=== RESOLUCIÓN DE ACTIVIDADES ===")
    
    # Inciso a
    print(f"a. Personaje de Capitana Marvel: {nombre_capitana_marvel}")
    
    # Inciso b
    print(f"b. Superhéroes femeninos: {', '.join(superheroes_femeninos)}")
    
    # Inciso c
    print(f"c. Personajes masculinos: {', '.join(personajes_masculinos)}")
    
    # Inciso d
    print(f"d. Superhéroe de Scott Lang: {heroe_scott_lang}")
    
    # Inciso e
    print("e. Datos que comienzan con 'S':")
    for p in comienzan_con_s:
        print(f"   - {p}")
        
    # Inciso f
    if carol_danvers_encontrada:
        print(f"f. Carol Danvers SÍ está en la cola. Su nombre de superhéroe es: {heroe_carol_danvers}")
    else:
        print("f. Carol Danvers NO se encuentra en la cola.")


# 3. Pruebas del algoritmo
if __name__ == "__main__":
    # Creamos la cola de personajes con los ejemplos dados y algunos extras para probar todos los incisos
    cola_mcu = deque([
        PersonajeMCU("Tony Stark", "Iron Man", "M"),
        PersonajeMCU("Steve Rogers", "Capitán América", "M"),
        PersonajeMCU("Natasha Romanoff", "Black Widow", "F"),
        PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"),
        PersonajeMCU("Scott Lang", "Ant-Man", "M"),
        PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F"),
        PersonajeMCU("Sam Wilson", "Falcon", "M")
    ])
    
    # Ejecutamos la función
    resolver_actividades_mcu(cola_mcu)
    
    # Comprobación de que la cola mantiene sus elementos al final
    print(f"\nCantidad de elementos en la cola al finalizar: {len(cola_mcu)} (Estructura preservada)")