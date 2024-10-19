import math

def menuConstantes():
    while True:
        print("\nFunciones de constantes")
        print("1. Pi")
        print("2. e")
        print("3. tau")
        print("4. inf")
        print("5. nan")
        print("6. Regresar al menú principal")

        opcion = input("Selecciona una constante: ")

        if opcion == '1':
            print("Pi:", math.pi)
        elif opcion == '2':
            print("e:", math.e)
        elif opcion == '3':
            print("Tau:", math.tau)
        elif opcion == '4':
            print("Infinito:", math.inf)
        elif opcion == '5':
            print("NaN:", math.nan)
        elif opcion == '6':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
