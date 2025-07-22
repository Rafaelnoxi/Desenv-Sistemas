# nota = int(input("Digite sua nota: "))

# if (nota >= 80):
#     print("Parabens")
# elif (nota < 80 and nota >= 60):
#     print("Pode Melhorar")
# elif (nota < 60):
#     print("Recuperação")

# nota1 = int(input("Digite sua nota1: "))
# nota2 = int(input("Digite sua nota2: "))
# nota3 = int(input("Digite sua nota3: "))
# nota4 = int(input("Digite sua nota4: "))

# notafinal = (nota1 + nota2 + nota3 + nota4)/4

# print("Sua nota foi:", notafinal)

# if (notafinal >= 80):
#     print("Exelente")
# elif (notafinal < 80 and notafinal >= 60):
#     print("Passou")
# elif (notafinal < 60):
#     print("Até ano que vem ")


# valor1 = int(input("Digite um numero: "))
# valor2 = int(input("Digite um numero: "))

# if (valor1 > valor2):
#     print("o maior valor é:", valor1)
# elif (valor1 < valor2):
#     print("o maior valor é:", valor2)
# elif (valor1 == valor2):
#     print("os valores são iguais")

# numero1 = float(input("digite o numero: "))
# numero2 = float(input("digite o numero: "))

# soma = numero1 + numero2 
# subtracao = numero1 - numero2
# multiplicacao = numero1 * numero2
# divisao = numero1 / numero2

# print("a soma desse numero é: ", soma),
# print("a subtração desse numero é: ", subtracao)
# print("a multiplicação desse numero é: ", multiplicacao)
# print("a divisão desse numero é: ", divisao)

salario = float(input("digite o seu salario: "))
salarioanual = salario * 12

if (salario > 5000):
    imposto1 = salario / 100 * 8
    print("você pagará: ", imposto1)
elif (salario < 5000):
    imposto2 = salario / 100 * 5
    print("você pagará: ", imposto2)
