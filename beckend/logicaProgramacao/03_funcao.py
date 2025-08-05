def saudacao(nome):
    print("ola", nome)

#saudacao("Rafael")

def soma(num1, num2):
    soma = num1 + num2
    print("soma: ", soma)

#soma(3, 4)


# crie uma funçao que faça a media de 3 valores

def media(num1, num2, num3):
    media = num1 + num2 + num3 / 3
    print("sua media é: ", media)

#media(1, 2, 3)

#crie uma funaço aonde calcule o impusto anual do seu salario

def salario_anual(salario):
    salario_anual = salario * 12
    imposto = salario_anual * 0.22
    print("voce pagará: ", imposto)

#salario_anual(10000)

#crie uma funçao que valide se a senha esta correta

def senha(senha_correta):
    senha = int(input("digite sua senha:"))
    while senha != senha_correta:
        print("senha incorreta")
        senha = int(input("digite sua senha:"))
    print("Sucesso")

senha(1234)
