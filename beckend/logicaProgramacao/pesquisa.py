# # pesquisar como alterar e excluir registros do arquivo.txt e criar um comentario no arquivo phyton com a explicação 

# with open("arquivo.txt", "r") as arquivo:
#     linhas = arquivo.readlines()

# # Suponha que queremos substituir "João" por "Maria"
# with open("arquivo.txt", "w") as arquivo:
#     for linha in linhas:
#         if "João" in linha:
#             linha = linha.replace("João", "Maria")
#         arquivo.write(linha)

# #Excluir uma linha

# with open("arquivo.txt", "r") as arquivo:
#     linhas = arquivo.readlines()

# # Suponha que queremos remover linhas que contenham "João"
# with open("arquivo.txt", "w") as arquivo:
#     for linha in linhas:
#         if "João" not in linha:
#             arquivo.write(linha)


while True:
    print("\n=== Loja de Carros ===")
    print("1. Cadastrar")
    print("2. Listar")
    print("3. Alterar")
    print("4. Excluir")
    print("5. Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        # Cadastrar carro
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        preco = input("Preço: ")
        with open("carros.txt", "a") as f:
            f.write(f"{marca}|{modelo}|{ano}|{preco}\n")
        print("Carro cadastrado!")

    elif opcao == "2":
        # Listar carros
        with open("carros.txt", "r") as f:
            carros = f.readlines()
            for i, carro in enumerate(carros):
                marca, modelo, ano, preco = carro.strip().split("|")
                print(f"[{i}] {marca} | {modelo} | {ano} | R${preco}")

    elif opcao == "3":
        # Alterar carro
        with open("carros.txt", "r") as f:
            carros = f.readlines()
        for i, carro in enumerate(carros):
            print(f"[{i}] {carro.strip()}")
        idx = int(input("Digite o número do carro para alterar: "))
        marca = input("Nova Marca: ")
        modelo = input("Novo Modelo: ")
        ano = input("Novo Ano: ")
        preco = input("Novo Preço: ")
        carros[idx] = f"{marca}|{modelo}|{ano}|{preco}\n"
        with open("carros.txt", "w") as f:
            f.writelines(carros)
        print("Carro alterado!")

    elif opcao == "4":
        # Excluir carro
        with open("carros.txt", "r") as f:
            carros = f.readlines()
        for i, carro in enumerate(carros):
            print(f"[{i}] {carro.strip()}")
        idx = int(input("Digite o número do carro para excluir: "))
        del carros[idx]
        with open("carros.txt", "w") as f:
            f.writelines(carros)
        print("Carro excluído!")

    elif opcao == "5":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")
