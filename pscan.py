import socket



ip = input("Digite o host ou ip a ser verificado: ")

#Criando vetor ports e contador count iniciando em 0
ports = []
count = 0

#Definindo contador
while count < 10:
    ports.append(int(input("Digite a porta a ser verificada: ")))
    count +=1

for port in ports:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.05)
    code = cliente.connect_ex((ip, port))

    if code == 0:
        print(str(port), " -> Porta Aberta")
    else:
        print(str(port), " -> Porta Fechada")

print("Scan Finalizado")