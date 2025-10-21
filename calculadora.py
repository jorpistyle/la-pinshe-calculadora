class Calculadora:

    def sumar(self, num1, num2):
        return num1 + num2
    def restar(self, num1, num2):
        return num1 - num2
    def multiplicar(self, num1, num2):
        return num1 * num2

    def dividir(self, num1, num2):
        return num1 / num2

def obtener_numero(mensaje):
    while True:
        try:
            numero = float(input(mensaje))
            return numero
        except ValueError:
            print("Error: Por favor, introduce solo números, bestia")

mi_calculadora = Calculadora()

print("Calculadora Básica")
numero1 = obtener_numero("Introduce el primer número: ")
numero2 = obtener_numero("Introduce el segundo número: ")

suma = mi_calculadora.sumar(numero1, numero2)
resta = mi_calculadora.restar(numero1, numero2)
multiplicacion = mi_calculadora.multiplicar(numero1, numero2)
division = mi_calculadora.dividir(numero1, numero2)

print("\nResultados")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print("no me exigas mas que hasta aca llego yo")
