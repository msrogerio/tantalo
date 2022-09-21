

caminho = input("Cole aqui o caminho absoluto do arquivo + o seu nome: ")
novo_conteudo = ""

with open(caminho, "r") as arquivo:
    conteudo = arquivo.read()
    linhas = conteudo.split("\n")
    for i in linhas:
        novo_conteudo += i.split("==")[0] + "\n"

with open(caminho, "w") as arquivo:
    arquivo.write(novo_conteudo)