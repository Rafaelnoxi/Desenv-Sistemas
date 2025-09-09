while True:
    print("\n=== Concessionária de Veículos ===")
    print("1. Cadastrar Carro")
    print("2. Listar Carros")
    print("3. Alterar Carro")
    print("4. Excluir Carro")
    print("5. Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        preco = input("Preço: ")
        carro = f"{marca}|{modelo}|{ano}|{preco}\n"
        with open("concessionaria.txt", "a") as arquivo:
            arquivo.writelines([carro])
        print("Carro cadastrado com sucesso!")

    elif opcao == "2":
        try:
            with open("concessionaria.txt", "r") as arquivo:
                carros = arquivo.readlines()
            if not carros:
                print("Nenhum carro cadastrado.")
            else:
                for numero, carro in enumerate(carros):
                    marca, modelo, ano, preco = carro.strip().split("|")
                    print(f"[{numero}] {marca} | {modelo} | {ano} | R${preco}")
        except FileNotFoundError:
            print("Nenhum carro cadastrado ainda.")

    elif opcao == "3":
        try:
            with open("concessionaria.txt", "r") as arquivo:
                carros = arquivo.readlines()
            if not carros:
                print("Nenhum carro para alterar.")
                continue
            for numero, carro in enumerate(carros):
                print(f"[{numero}] {carro.strip()}")
            numero_carro = int(input("Digite o número do carro para alterar: "))
            nova_marca = input("Nova marca: ")
            novo_modelo = input("Novo modelo: ")
            novo_ano = input("Novo ano: ")
            novo_preco = input("Novo preço: ")
            nova_linha = f"{nova_marca}|{novo_modelo}|{novo_ano}|{novo_preco}\n"
            carros[numero_carro] = nova_linha
            with open("concessionaria.txt", "w") as arquivo:
                arquivo.writelines(carros)
            print("Carro alterado com sucesso!")
        except (ValueError, IndexError):
            print("Número inválido.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    elif opcao == "4":
        try:
            with open("concessionaria.txt", "r") as arquivo:
                carros = arquivo.readlines()
            if not carros:
                print("Nenhum carro para excluir.")
                continue
            for numero, carro in enumerate(carros):
                print(f"[{numero}] {carro.strip()}")
            numero_carro = int(input("Digite o número do carro para excluir: "))
            del carros[numero_carro]
            with open("concessionaria.txt", "w") as arquivo:
                arquivo.writelines(carros)
            print("Carro excluído com sucesso!")
        except (ValueError, IndexError):
            print("Número inválido.")
        except FileNotFoundError:
            print("Arquivo não encontrado.")

    elif opcao == "5":
        print("Saindo da concessionária... Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
