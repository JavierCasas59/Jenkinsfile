class Calculadora:
    def multiplicar(self, a, b):
        return a * b

if __name__ == "__main__":
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))

        calc = Calculadora()
        resultado = calc.multiplicar(num1, num2)

        print(f"Resultado: {resultado}")

    except ValueError:
        print("Error: debes introducir números válidos")
