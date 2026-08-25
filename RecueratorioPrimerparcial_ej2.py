from collections import deque

from list import Lista
from super_heroes_data import superheroes


class Personaje:

    def __init__(
        self,
        name,
        alias,
        real_name,
        bio,
        first_appearance,
        is_villain
    ):
        self.name = name
        self.alias = alias
        self.real_name = real_name
        self.bio = bio
        self.first_appearance = first_appearance
        self.is_villain = is_villain

    def __str__(self):

        tipo = "Villano" if self.is_villain else "Héroe"

        return f"{self.name} | real: {self.real_name} | {self.first_appearance} | {tipo}"


# ---------------------------------------------------------
# CRITERIOS
# ---------------------------------------------------------

def by_name(item):
    return item.name


def by_real_name(item):
    return item.real_name or ""


def by_first_appearance(item):
    return item.first_appearance


# ---------------------------------------------------------
# CREAR LISTA
# ---------------------------------------------------------

lista = Lista()

lista.add_criterion("name", by_name)
lista.add_criterion("real_name", by_real_name)
lista.add_criterion("first_appearance", by_first_appearance)


# ---------------------------------------------------------
# CARGAR PERSONAJES
# ---------------------------------------------------------

for hero in superheroes:

    lista.append(
        Personaje(
            hero["name"],
            hero["alias"],
            hero["real_name"],
            hero["short_bio"],
            hero["first_appearance"],
            hero["is_villain"]
        )
    )


# =========================================================
# EJERCICIO 2
# =========================================================

if __name__ == "__main__":

    # -----------------------------------------------------
    # 1) ORDENAR POR NOMBRE
    # -----------------------------------------------------

    print("\n1) PERSONAJES ORDENADOS POR NOMBRE")

    lista.sort_by_criterion("name")

    lista.show()


    # -----------------------------------------------------
    # 2) BUSCAR THE THING Y ROCKET RACCOON
    # -----------------------------------------------------

    print("\n2) POSICIONES")

    pos_thing = lista.search("The Thing", "name")

    pos_rocket = lista.search("Rocket Raccoon", "name")

    print("The Thing:", pos_thing)

    print("Rocket Raccoon:", pos_rocket)


    # -----------------------------------------------------
    # 3) LISTAR TODOS LOS VILLANOS
    # -----------------------------------------------------

    print("\n3) VILLANOS")

    villanos = Lista()

    for personaje in lista:

        if personaje.is_villain:
            villanos.append(personaje)

    villanos.show()


    # -----------------------------------------------------
    # 4) COLA DE VILLANOS
    # -----------------------------------------------------

    print("\n4) VILLANOS QUE APARECIERON ANTES DE 1980")

    cola_villanos = deque(villanos)

    while cola_villanos:

        villano = cola_villanos.popleft()

        if villano.first_appearance < 1980:
            print(villano)


    # -----------------------------------------------------
    # 5) COMIENZAN CON Bl, G, My Y W
    # -----------------------------------------------------

    print("\n5) PERSONAJES QUE COMIENZAN CON Bl, G, My Y W")

    lista.filter_start_with(
        ("Bl", "G", "My", "W")
    )


    # -----------------------------------------------------
    # 6) ORDENAR POR NOMBRE REAL
    # -----------------------------------------------------

    print("\n6) PERSONAJES ORDENADOS POR NOMBRE REAL")

    lista.sort_by_criterion("real_name")

    lista.show()


    # -----------------------------------------------------
    # 7) ORDENAR POR FECHA DE APARICIÓN
    # -----------------------------------------------------

    print("\n7) PERSONAJES ORDENADOS POR FECHA DE APARICIÓN")

    lista.sort_by_criterion("first_appearance")

    lista.show()


    # -----------------------------------------------------
    # 8) MODIFICAR ANT MAN
    # -----------------------------------------------------

    print("\n8) MODIFICAR NOMBRE REAL DE ANT MAN")

    pos_ant_man = lista.search("Ant Man", "name")

    if pos_ant_man is not None:

        lista[pos_ant_man].real_name = "Scott Lang"

        print(lista[pos_ant_man])

    else:

        print("No se encontró Ant Man")


    # -----------------------------------------------------
    # 9) BUSCAR TIME-TRAVELING O SUIT
    # -----------------------------------------------------

    print("\n9) PERSONAJES CON TIME-TRAVELING O SUIT")

    lista.filter_contain_on_bio(
        ["time-traveling", "suit"]
    )


    # -----------------------------------------------------
    # 10) ELIMINAR ELECTRO Y BARON ZEMO
    # -----------------------------------------------------

    print("\n10) ELIMINAR ELECTRO Y BARON ZEMO")

    eliminado = lista.delete_value(
        "Electro",
        "name"
    )

    if eliminado:

        print("Eliminado:", eliminado)

    else:

        print("Electro no estaba en la lista")


    eliminado = lista.delete_value(
        "Baron Zemo",
        "name"
    )

    if eliminado:

        print("Eliminado:", eliminado)

    else:

        print("Baron Zemo no estaba en la lista")
