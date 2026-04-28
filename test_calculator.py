import sys

class Calculadora:
    def multiplicar(self, a, b):
        return a * b

if __name__ == "__main__":
    calc = Calculadora()

    try:
        if len(sys.argv) == 3:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
        else:
            print("Modo interactivo:")
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))

        resultado = calc.multiplicar(num1, num2)
        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: debes introducir números válidos")