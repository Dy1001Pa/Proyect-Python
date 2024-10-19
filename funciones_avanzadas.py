import math

def menuAvanzadas():
    while True:
        print("\nOtras funciones avanzadas")
        print("1. degrees(x)")
        print("2. radians(x)")
        print("3. dist(p, q)")
        print("4. erf(x)")
        print("5. erfc(x)")
        print("6. gamma(x)")
        print("7. lgamma(x)")
        print("8. Regresar al menú principal")

        opcion = input("Selecciona una función: ")

        if opcion == '1':
            x = float(input("Introduce un ángulo en radianes: "))
            print("Resultado en grados:", math.degrees(x))
        elif opcion == '2':
            x = float(input("Introduce un ángulo en grados: "))
            print("Resultado en radianes:", math.radians(x))
        elif opcion == '3':
            p = list(map(float, input("Introduce el primer punto (separado por espacios): ").split()))
            q = list(map(float, input("Introduce el segundo punto (separado por espacios): ").split()))
            print("Distancia entre puntos:", math.dist(p, q))
        elif opcion == '4':
            x = float(input("Introduce un número: "))
            print("Resultado de erf:", math.erf(x))
        elif opcion == '5':
            x = float(input("Introduce un número: "))
            print("Resultado de erfc:", math.erfc(x))
        elif opcion == '6':
            x = float(input("Introduce un número: "))
            print("Resultado de gamma:", math.gamma(x))
        elif opcion == '7':
            x = float(input("Introduce un número: "))
            print("Resultado de lgamma:", math.lgamma(x))
        elif opcion == '8':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
