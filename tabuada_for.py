tabuada=int(input("Digite um número para exibir a tabuada "))
print("Tabuada do número ", tabuada)
for valor in range (1,16,1):
    print(str(tabuada) + " x " + str(valor) + " * " + str((tabuada*valor)))