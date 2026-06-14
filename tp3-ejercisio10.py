from collections import deque
from datetime import datetime

# =====================================================================
# RESOLUCIÓN DE LAS ACTIVIDADES (FUNCIONES)
# =====================================================================

# a. Función para eliminar de la cola todas las notificaciones de Facebook
def eliminar_facebook(cola):
    tamanio_inicial = len(cola)
    for _ in range(tamanio_inicial):
        notificacion = cola.popleft()  # Desencolar
        if notificacion["app"] != "Facebook":
            cola.append(notificacion)  # Si no es Facebook, vuelve a la cola

# b. Función para mostrar notificaciones de Twitter con la palabra 'Python'
def mostrar_twitter_python(cola):
    tamanio_inicial = len(cola)
    print("\n--- NOTIFICACIONES DE TWITTER SOBRE 'PYTHON' ---")
    for _ in range(tamanio_inicial):
        notificacion = cola.popleft()
        
        es_twitter = notificacion["app"] == "Twitter"
        tiene_python = "python" in notificacion["mensaje"].lower()
        
        if es_twitter and tiene_python:
            print(f"[{notificacion['hora']}] {notificacion['app']}: {notificacion['mensaje']}")
            
        cola.append(notificacion)  # Se vuelve a encolar para no perder datos
    print("------------------------------------------------")

# c. Función para filtrar por rango horario utilizando una pila temporal
def filtrar_por_horario_y_contar(cola):
    pila_temporal = []  # Estructura LIFO para el almacenamiento temporáneo
    
    hora_inicio = datetime.strptime("11:43", "%H:%M").time()
    hora_fin = datetime.strptime("15:57", "%H:%M").time()
    
    tamanio_inicial = len(cola)
    for _ in range(tamanio_inicial):
        notificacion = cola.popleft()
        hora_noti = datetime.strptime(notificacion["hora"], "%H:%M").time()
        
        if hora_inicio <= hora_noti <= hora_fin:
            pila_temporal.append(notificacion)  # Apilar (Push)
        else:
            cola.append(notificacion)  # Volver a la cola si está fuera de rango
            
    cantidad = len(pila_temporal)
    print(f"\n>> [PILA]: Se almacenaron {cantidad} notificaciones en el rango horario.")
    
    # Se vacía la pila mostrando su contenido (Comportamiento LIFO)
    while len(pila_temporal) > 0:
        elemento = pila_temporal.pop()  # Desapilar (Pop)
        print(f"   * Elemento en Pila -> [{elemento['hora']}] {elemento['app']}: {elemento['mensaje']}")
        
    return cantidad


# =====================================================================
# BLOQUE DE PRUEBA Y DEMOSTRACIÓN (RECOMENDADO PARA LA ENTREGA)
# =====================================================================
if __name__ == "__main__":
    # 1. Creación de la cola con datos de ejemplo para la demostración
    cola_notificaciones = deque([
        {"hora": "10:30", "app": "Facebook", "mensaje": "A Juan le gustó tu foto"},
        {"hora": "11:45", "app": "Twitter", "mensaje": "¡Nuevo curso de Python disponible!"},
        {"hora": "12:15", "app": "Facebook", "mensaje": "Es el cumpleaños de María"},
        {"hora": "14:20", "app": "Twitter", "mensaje": "Me encanta programar"},
        {"hora": "15:30", "app": "WhatsApp", "mensaje": "Hola, ¿cómo estás?"},
        {"hora": "16:00", "app": "Twitter", "mensaje": "Python en ciencia de datos"},
    ])

    print("=== COLA ORIGINAL ===")
    for n in cola_notificaciones:
        print(f"[{n['hora']}] {n['app']}: {n['mensaje']}")
        
    # Ejecución de la actividad B
    mostrar_twitter_python(cola_notificaciones)
    
    # Ejecución de la actividad C
    filtrar_por_horario_y_contar(cola_notificaciones)
    
    # Ejecución de la actividad A
    eliminar_facebook(cola_notificaciones)
    
    print("\n=== COLA FINAL (Luego de aplicar los procesos y eliminar Facebook) ===")
    for n in cola_notificaciones:
        print(f"[{n['hora']}] {n['app']}: {n['mensaje']}")