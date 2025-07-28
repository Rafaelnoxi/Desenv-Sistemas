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
    

# soma = 0

# for i in range(1, 21):  
#     soma += i

# print("A soma dos números de 1 a 20 é:", soma)

soma = 0

for _ in range(1000): 
    entrada = input("Digite um número (ou qualquer outra coisa para sair): ")
    if entrada.isdigit():
        soma += int(entrada)
    else:
        break

print("A soma total dos números digitados é:", soma)

