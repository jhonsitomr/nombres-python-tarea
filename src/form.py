def ask_menu_opt() -> str:

    print("""a. Agregar un nombre.
b. Mostrar todos los nombres.
c. Buscar un nombre.
d. Salir.""")

    res = input(": ")

    if len(res) > 0:

        return res.lower()
