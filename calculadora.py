import funciones_basicas
import funciones_math
import funciones_trigonometricas
import funciones_hiperbolicas
import funciones_constantes
import funciones_avanzadas

def menu_principal():
    while True:
        print("\nMenú principal")
        print("1. Funciones matemáticas incorporadas")
        print("2. Funciones matemáticas del módulo math")
        print("3. Funciones trigonométricas")
        print("4. Funciones hiperbólicas")
        print("5. Funciones de constantes")
        print("6. Otras funciones avanzadas")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            funciones_basicas.menuBasica()
        elif opcion == '2':
            funciones_math.menuMath()
        elif opcion == '3':
            funciones_trigonometricas.menuTrigonometricas()
        elif opcion == '4':
            funciones_hiperbolicas.menuHiperbolicas()
        elif opcion == '5':
            funciones_constantes.menuConstantes()
        elif opcion == '6':
            funciones_avanzadas.menuAvanzadas()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    menu_principal()
