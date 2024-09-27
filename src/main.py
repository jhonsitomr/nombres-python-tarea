import form

from util import *

while True:

    opt = force(form.ask_menu_opt)

    match opt:

        case "a":

            file = open("nombres.txt", "a+")

            name = input("Introduce un nombre: ")

            file.write(", " + name)

            file.close()

        case "b":

            try:

                file = open("nombres.txt", "r")

                print("* " * 30)

                for ind, name in enumerate(file.readline().split(", ")[1:]):

                    print(f"{ind}. {name}")

                print("* " * 30)

                file.close()

            except FileNotFoundError:

                print("* " * 30)

                print("Inicializar el archivo agregando nombres.")

                print("* " * 30)

        case "c":

            try:

                file = open("nombres.txt", "r+")

                data = file.readline().split(", ")[1:]

                name = input("Introduce un nombre: ")

                print("* " * 30)

                if name in data:

                    print(f"'{name}' se encuentra en el archivo.")
                else:

                    print(f"'{name}' no se encuentra en el archivo.")

                print("* " * 30)

                file.close()

            except FileNotFoundError:

                print("* " * 30)

                print("Inicializar el archivo agregando nombres.")

                print("* " * 30)

        case "d":

            print("Adios, hasta la proxima.")

            exit()
