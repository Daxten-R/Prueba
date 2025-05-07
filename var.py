class Numero:
    def __init__(self, enteroVar: int, doubleVar: bool, textoVar: str, vacioVar=None):
        self.enteroVar = enteroVar
        self.doubleVar = doubleVar
        self.textoVar = textoVar
        self.vacioVar = vacioVar

    def mostrar(self):
        
        entrada = input("Ingrese un valor: ")
        
    
        try:
            if entrada.isdigit():  
                self.enteroVar = int(entrada)
                print(f"{self.enteroVar} Es un entero.")
            elif entrada.replace('.', '', 1).isdigit() and entrada.count('.') < 2:  
                self.doubleVar = float(entrada)
                print(f"{self.doubleVar} Es un double.")
            elif entrada == "": 
                self.vacioVar = ""
                print("Está vacío.")
            else:
                self.textoVar = entrada
                print(f"{self.textoVar} Es un string.")
        except ValueError:
            print("Error en la entrada.")


objeto = Numero(0, False, "", None)

objeto.mostrar()

