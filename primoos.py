n = int(input("Ingresa un número: "))
if n <= 1:
    print("No es primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")