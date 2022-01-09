nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa?:")

if idade<= 65:
    print("Paciente com PRIORIDADE ")
    if doenca_infectocontagiosa=="SIM":
        print("O paciente será encaminhado para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("O paciente será encaminhado para sala BRANCA")

    else:
        print("O paciente está de alta!")

else:
    print("Paciente SEM prioridade")
    if doenca_infectocontagiosa=="SIM":
        print("O paciente será encaminhado para sala AMARELA")
    elif doenca_infectocontagiosa=="NAO":
        print("O paciente será encaminhado para sala BRANCA")

    else:
        print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")