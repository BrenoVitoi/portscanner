import nmap

scanner = nmap.PortScanner()

print("Seja bem vindo ao DIOScanner")
print("<-------------------------->")

ip = input("Digite o ip a ser varrido: ")
print("O ip digitado foi: ", ip)
type(ip)

menu = input(""""\n Escolha o tipo de varredura a ser realizada
                1 -> Varredura do Tipo SYN
                2 -> Varredura do Tipo UDP
                3 ->  Varredura do Tipo Intensa
                Digite a opção escolhida: """)
print("A opção escolhida foi", menu)
