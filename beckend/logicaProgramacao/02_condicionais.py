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

# soma = 0
# numero = int(input("Digite um numero (0 Para Sair): "))

# while numero != 0:
#     soma = soma + numero
#     numero = int(input("Digite um numero (0 Para Sair): "))
    
# print("A soma total dos números digitados é:", soma)

# soma2 = 0

# while True:
#     operacao = input("Digite 'D' para depositar ou 'S' para sacar: ").upper()

#     if operacao not in ['D', 'S']:
#         print("Operação inválida. Use apenas D ou S.")
#         continue

#     valor = float(input("Digite o valor (0 para sair): "))

#     if valor == 0:
#         break

#     if operacao == 'D':
#         soma2 += valor
#     elif operacao == 'S':
#         soma2 -= valor

# print("Saldo final:", soma2)

# senha_correta = int(input("Digite uma senha: "))
# senha = int(input("Digite sua senha: "))

# while senha != senha_correta:
#     print("senha invalida")
#     senha = int(input("Digite sua senha: "))

# print("acesso liberado")

senha = int(input("Digite uma senha?: "))
nome = input("Digite Seu nome: ")
senha_correta = int(input("digite sua senha: "))

while senha != senha_correta:
    print("Senha incorreta: ")
    senha_correta = int(input("digite sua senha"))

print("bem vindo!", nome)

salario = float(input("Digite seu salario: "))

salario_anual = salario * 12

print("Seu salario anual é: ", salario_anual)

if salario_anual > 100000:
    print("rico")