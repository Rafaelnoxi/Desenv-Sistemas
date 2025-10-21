with open ("alunos.txt","w") as arquivo:
    arquivo.write("Rafael\n")
    arquivo.write("Nicolas\n")
    arquivo.write("Rafaela\n")
    arquivo.write("Guilherme\n")
    arquivo.write("Agner\n")

with open ("alunos.txt","r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)