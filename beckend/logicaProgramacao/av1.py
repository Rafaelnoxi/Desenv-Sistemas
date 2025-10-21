while True:
    print("\n=== Padaria do Bairro ===")
    print("1. Cadastrar Produto")
    print("2. Listar Produtos")
    print("3. Alterar Produto")
    print("4. Excluir Produto (Estoque Zerado)")
    print("5. Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        tipo = input("Tipo (pão, bolo, doce, etc.): ")
        preco = input("Preço: ")
        quantidade = input("Quantidade em estoque: ")
        linha = f"{nome}|{tipo}|{preco}|{quantidade}\n"
        with open("padaria.txt", "a") as arquivo:
            arquivo.writelines([linha])
        print("Produto cadastrado com sucesso!")

    elif opcao == "2":
        try:
            with open("padaria.txt", "r") as arquivo:
                produtos = arquivo.readlines()
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                for indice, produto in enumerate(produtos):
                    nome, tipo, preco, quantidade = produto.strip().split("|")
                    print(f"[{indice}] {nome} | {tipo} | R${preco} | Estoque: {quantidade}")
        except FileNotFoundError:
            print("Nenhum produto cadastrado ainda.")

    elif opcao == "3":
        try:
            with open("padaria.txt", "r") as arquivo:
                produtos = arquivo.readlines()
            if not produtos:
                print("Nenhum produto para alterar.")
                continue
            for indice, produto in enumerate(produtos):
                print(f"[{indice}] {produto.strip()}")
            numero_produto = int(input("Digite o número do produto para alterar: "))
            nome = input("Novo nome: ")
            tipo = input("Novo tipo: ")
            preco = input("Novo preço: ")
            quantidade = input("Nova quantidade: ")
            nova_linha = f"{nome}|{tipo}|{preco}|{quantidade}\n"
            produtos[numero_produto] = nova_linha
            with open("padaria.txt", "w") as arquivo:
                arquivo.writelines(produtos)
            print("Produto alterado com sucesso!")
        except (ValueError, IndexError):
            print("Número inválido.")
        except FileNotFoundError:
            print("Arquivo de produtos não encontrado.")

    elif opcao == "4":
        try:
            with open("padaria.txt", "r") as arquivo:
                produtos = arquivo.readlines()
            if not produtos:
                print("Nenhum produto para excluir.")
                continue
            for indice, produto in enumerate(produtos):
                print(f"[{indice}] {produto.strip()}")
            numero_produto = int(input("Digite o número do produto para excluir: "))
            del produtos[numero_produto]
            with open("padaria.txt", "w") as arquivo:
                arquivo.writelines(produtos)
            print("Produto excluído com sucesso!")
        except (ValueError, IndexError):
            print("Número inválido.")
        except FileNotFoundError:
            print("Arquivo de produtos não encontrado.")

    elif opcao == "5":
        print("Saindo da padaria... Até a próxima!")
        break

    else:
        print("Opção inválida. Tente novamente.")
