with open("teste.txt", "r+b") as arquivo:
    conteudo=arquivo.readlines()
print("Tipo de dado da variável",type(conteudo))
print("Conteúdo do arquivo",conteudo)