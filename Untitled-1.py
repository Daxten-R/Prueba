while True:
    try:
        n = int(input("Ingresa un número primo: "))  # Entrada de usuario
        if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            print(f" {n} primo.")
            # break
        else:
            print("Es primo.")

    except ValueError:
        print(" Solo se permiten números.")

