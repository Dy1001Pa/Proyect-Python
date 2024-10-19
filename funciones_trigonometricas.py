import math

def menuTrigonometricas():
    while True:
        print("\nFunciones trigonométricas")
        print("1. sin(x)")
        print("2. cos(x)")
        print("3. tan(x)")
        print("4. asin(x)")
        print("5. acos(x)")
        print("6. atan(x)")
        print("7. atan2(y, x)")
        print("8. hypot(x, y)")
        print("9. Regresar al menú principal")

        opcion = input("Selecciona una función: ")

        if opcion == '1':
            x = float(input("Introduce un número (en radianes): "))
            print("Resultado de sin:", math.sin(x))
        elif opcion == '2':
            x = float(input("Introduce un número (en radianes): "))
            print("Resultado de cos:", math.cos(x))
        elif opcion == '3':
            x = float(input("Introduce un número (en radianes): "))
            print("Resultado de tan:", math.tan(x))
        elif opcion == '4':
            x = float(input("Introduce un número (entre -1 y 1): "))
            if -1 <= x <= 1:
                print("Resultado de asin:", math.asin(x))
            else:
                print("El número debe estar entre -1 y 1.")
        elif opcion == '5':
            x = float(input("Introduce un número (mayor o igual a -1): "))
            if x >= -1 and x <= 1:
                print("Resultado de acos:", math.acos(x))
            else:
                print("El número debe estar entre -1 y 1.")
        elif opcion == '6':
            x = float(input("Introduce un número: "))
            print("Resultado de atan:", math.atan(x))
        elif opcion == '7':
            y = float(input("Introduce el valor de y: "))
            x = float(input("Introduce el valor de x: "))
            print("Resultado de atan2:", math.atan2(y, x))
        elif opcion == '8':
            x = float(input("Introduce el valor de x: "))
            y = float(input("Introduce el valor de y: "))
            print("Resultado de hypot:", math.hypot(x, y))
        elif opcion == '9':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
