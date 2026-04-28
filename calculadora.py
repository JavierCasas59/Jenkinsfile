import sys

class Calculadora:
    def multiplicar(self, a, b):
        return a * b


if __name__ == "__main__":
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        calc = Calculadora()
        resultado = calc.multiplicar(num1, num2)

        print(f"Resultado: {resultado}")

    except (IndexError, ValueError):
        print("Uso correcto: python calculadora.py <num1> <num2>")
