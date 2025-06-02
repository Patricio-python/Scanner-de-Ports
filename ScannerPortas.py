# Import da lib socket para conexões e tqdm para criar a barra de progressão
import socket
from tqdm import tqdm
import pyfiglet
banner = pyfiglet.figlet_format("Scanner de Portas", font = "slant") 
print(banner) 

def opcao():
      #Função ultilizada para mostrar os tipo de portas e alcance do scanner assim como a opção de escolher o tipo digitando o número.
    global tipo
    tipo = int(input("\n1: Portas Bem conhecidas (0 até 1023)\n2: Portas Registradas (1024 até 49151)\n3: Scanner completo (0 até 49151)\nDigite 0 para cancelar\n\n"))

def scan():
    # Função para realizar o scanner.
    # O alcance será definido pela opção que será selecionada antes dessa função ser usada. 
    try:
        # O ip do alvo será digitado pelo usuário
        alvo = input('Digite o IP/Dominio: ')
        # Lista que receberá o número das portas que estão abertas
        portaAberta=[]
        #Criação das variáveis globais, cujos os valores serão recebidos pela escolha feita
        global scannerInicial, scannerFinal
        # Loop de acordo com o tipo selecionado
        for porta in tqdm(range(scannerInicial, scannerFinal)):
            client = socket.socket()
            client.settimeout(0.05)
            # Setando e configurando o cliente
            # Se a porta estiver aberta, é adicionada a lista de portas abertas
            if client.connect_ex((alvo, porta)) == 0:
                portaAberta.append(porta)
        # listagem das portas abertas
        print("\nPortas abertas: \n",portaAberta)
        print("\nDeseja realizar outro Scan?") 
        opcao()
    #No caso de algum erro um aviso será dado que o scanner não pode ser realizado e dará a opção de tentar realizar outro scan se assim desejar
    except:
            print("\nAconteceu algum erro e o Scanner não pode ser realizado.\nDeseja tentar de novo?")
            opcao()  
print("Bem vindo ao scanner de portas.\nPor favor selcione o tipo de scanner que deseja realizar.")
opcao()
while tipo != 0:
    #Setup para o range do scanner de acordo com o tipo selecionado
    if tipo == 1:
        scannerInicial=int(1)
        scannerFinal=int(1024)
        scan()
    elif tipo == 2:
        scannerInicial=int(1024)
        scannerFinal=int(49152)
        scan()
    elif tipo==3:
        scannerInicial=int(1)
        scannerFinal=int(49152)
        scan()
    else:
    # Opção para o caso de selecionar o valor que não esta nas opções.
        print("\nOpção invalida!! Selecione uma opção valida")
        opcao()
print("Obrigado por usar o Scanner de Portas")