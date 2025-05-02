# Import da lib socket para conexões e tqdm para criar a barra de progressão
import socket
from tqdm import tqdm
import pyfiglet
banner = pyfiglet.figlet_format("Scanner de Portas", font = "slant") 
print(banner) 
tipo = int(input("Bem vindo ao scanner de portas."
      "\nPor favor selcione o tipo de scanner que deseja realizar.\n" 
      "\n1 : Portas Bem conhecidas (0 até 1023)"
      "\n2 : Portas Registradas (1024 até 49151)"
      "\n3 : Scanner completo (0 até 49151)"
      "\nDigite 0 para cancelar\n"))

while tipo != 0:
    #Setup para o range do scanner de acordo com o tipo selecionado
    if tipo == 1:
        scannerInicial=int(1)
        scannerFinal=int(1024)
    elif tipo == 2:
        scannerInicial=int(1024)
        scannerFinal=int(49152)
    else:
        scannerInicial=int(1)
        scannerFinal=int(49152)
    # O ip do alvo será digitado pelo usuário
    alvo = input('Digite o IP/Dominio: ')
    # Lista que receberá o número das portas que estão abertas
    portaAberta=[]
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
    #Opção para selecionar outro Scan ou finalizar
    tipo = int(input("Deseja realizar outro Scan?.\n" 
    "\n1 : Portas Bem conhecidas (0 até 1023)"
    "\n2 : Portas Registradas (1024 até 49151)"
    "\n3 : Scanner completo (0 até 49151)"
    "\nDigite 0 para cancelar\n"))