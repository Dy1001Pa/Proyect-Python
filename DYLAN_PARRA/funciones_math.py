import math

def menuMath():
    while True:
        print("\nFunciones del módulo math")
        print("1. sqrt(x)")
        print("2. exp(x)")
        print("3. log(x, base)")
        print("4. log10(x)")
        print("5. log2(x)")
        print("6. factorial(x)")
        print("7. gcd(a, b)")
        print("8. isqrt(x)")
        print("9. copysign(x, y)")
        print("10. fabs(x)")
        print("11. ceil(x)")
        print("12. floor(x)")
        print("13. trunc(x)")
        print("14. fmod(x, y)")
        print("15. prod(iterable)")
        print("16. Regresar al menú principal")

        opcion = input("Selecciona una función: ")

        if opcion == '1':
            x = float(input("Introduce un número: "))
            print("Resultado:", math.sqrt(x))
        # Agrega el resto de las funciones según el mismo patrón...
        elif opcion == '16':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
