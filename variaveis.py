tabuada = int(input("Digite um número para exibir a tabuada: "))
print("Tabuada do número", tabuada)
decisao = "SIM"
while decisao == "SIM":
    for valor in range(1,11,1):
        print(str(tabuada) +'x'+ str(valor)+ '=' +str(tabuada*valor))
        total = tabuada * valor
        if total == tabuada * 10:
            decisao = input("Deseja continuar?sim/nao ").upper()
            if decisao == "SIM":
                tabuada = int(input("Digite um número para exibir a tabuada: "))
            else:
                decisao == "NAO"



iventario = []
resposta = "S"
while resposta == "S":
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Numero Serial: ")),
                   input("Departamento: ")]
    iventario.append(equipamento)
    resposta = input("Deseja continuar?s/n ").upper()

