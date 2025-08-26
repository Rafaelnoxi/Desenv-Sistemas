#o que é o try except?
#é uma função usada para quando acontecer algumas exceções durante o codigo e apresentar algum erro.

#temos alguns blocos para o try except - try - except - else - finally
# - try - o codigo que pode conter uma exceção
# - except - se ocorrer uma exceção, o try procurá o bloco except para executar
# - else - caso nao ocorra nenhuma exceção o bloco else será executado ( não é obrigatorio )
# - finally - ele é sempre executado ( não é obrigatorio )

# usando (laços, função e try execpt), crie um sistema para receber as notas de um aluno e calcule a media anual, se digitar algo sem ser numero tratar o erro


def calcular_media():
    notas = []
    for i in range(3):
        while True:
            try:
                nota = float(input("Digite a nota: "))
                notas.append(nota)
                break
            except ValueError:
                print("Erro! Digite um número.")
    media = sum(notas) / 3
    print("Média:", media)

calcular_media()


# usando (lista, função, laços e try except), voce deverá criar uma lista com numeros e mensagens se for numero adicionar a uma lista a partese for mensagem tratar com o erro de tipo ao final, mostrar a lista so com numeros
 
 def separar_numeros():
    entrada = input("Digite os valores separados por vírgula: ")
    dados = [item.strip() for item in entrada.split(',')]
    
    numeros = []
    for item in dados:
        try:
            num = float(item)
            numeros.append(num)
        except:
            print("Ignorando:", item)
    
    print("Lista só com números:", numeros)

separar_numeros()


# criar uma lista com cadastro de usuario 
# cadastrar 
# alterar 
# excluir 
# listar
# usar (função, lista, try execpt, laços)

usuarios = []

def menu():
    executando = True
    while executando:
        print("\n1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Excluir")
        print("4 - Listar")
        print("5 - Sair")

        try:
            opcao = int(input("Escolha uma opção: "))
        except:
            print("Digite um número!")
            continue

        if opcao == 1:  # Cadastrar
            nome = input("Digite o nome: ")
            usuarios.append(nome)
            print("Cadastrado com sucesso!")

        elif opcao == 2:  # Alterar
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                continue
            for i in range(len(usuarios)):
                print(i, usuarios[i])
            try:
                pos = int(input("Digite o número do usuário para alterar: "))
                if 0 <= pos < len(usuarios):
                    novo_nome = input("Digite o novo nome: ")
                    usuarios[pos] = novo_nome
                    print("Usuário alterado com sucesso!")
                else:
                    print("Índice inválido.")
            except:
                print("Erro ao alterar!")

        elif opcao == 3:  # Excluir
            if not usuarios:
                print("Nenhum usuário cadastrado.")
                continue
            for i in range(len(usuarios)):
                print(i, usuarios[i])
            try:
                pos = int(input("Digite o número do usuário para excluir: "))
                if 0 <= pos < len(usuarios):
                    usuarios.pop(pos)
                    print("Usuário excluído com sucesso!")
                else:
                    print("Índice inválido.")
            except:
                print("Erro ao excluir!")

        elif opcao == 4:  # Listar
            if usuarios:
                print("Usuários cadastrados:")
                for u in usuarios:
                    print(u)
            else:
                print("Nenhum usuário cadastrado.")

        elif opcao == 5:  # Sair
            executando = False

        else:
            print("Opção inválida!")

menu()

