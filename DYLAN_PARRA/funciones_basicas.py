def menuBasica():
    while True:
        print("\nFunciones matemáticas incorporadas")
        print("1. abs(x)")
        print("2. round(x, n)")
        print("3. pow(x, y)")
        print("4. divmod(x, y)")
        print("5. sum(iterable)")
        print("6. min(iterable)")
        print("7. max(iterable)")
        print("8. Regresar al menú principal")

        opcion = input("Selecciona una función: ")

        if opcion == '1':
            x = float(input("Introduce un número: "))
            print("Resultado:", abs(x))
        elif opcion == '2':
            x = float(input("Introduce un número: "))
            n = int(input("Introduce el número de decimales: "))
            print("Resultado:", round(x, n))
        elif opcion == '3':
            x = float(input("Introduce la base: "))
            y = float(input("Introduce el exponente: "))
            print("Resultado:", pow(x, y))
        elif opcion == '4':
            x = float(input("Introduce el dividendo: "))
            y = float(input("Introduce el divisor: "))
            print("Resultado:", divmod(x, y))
        elif opcion == '5':
            elementos = list(map(float, input("Introduce una lista de números separados por espacio: ").split()))
            print("Resultado:", sum(elementos))
        elif opcion == '6':
            elementos = list(map(float, input("Introduce una lista de números separados por espacio: ").split()))
            print("Resultado:", min(elementos))
        elif opcion == '7':
            elementos = list(map(float, input("Introduce una lista de números separados por espacio: ").split()))
            print("Resultado:", max(elementos))
        elif opcion == '8':
            break
        else:
            print("Opción no válida, intenta de nuevo.")
