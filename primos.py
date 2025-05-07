class Primos:
    def __init__(self, numero):
        self.numero = numero

    def primo(self):
        if self.numero <= 1:
            return False  
        for i in range(2, self.numero):
            if self.numero % i == 0:
                return False  # Si el número es divisible por otro número que no sea 1 ni él mismo, no es primo
        return True  # Si no se encuentra ningún divisor, es primo

numero = int(input("Ingrese un número: "))

# Crear un objeto de la clase Primos
primo = Primos(numero)

# Verificar si el número es primo
if primo.primo():
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
