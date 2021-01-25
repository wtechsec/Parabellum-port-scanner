from termcolor import colored
import sys
import nmap
from pyfiglet import Figlet
scan_row=[]

print("-" * 50)
f = Figlet(font='slant')
print(colored(f.renderText("PARABELLUM"), 'green')) #banner
print("-" * 50)
f = Figlet(font='slant')
print(colored(f.renderText("PORT-SCANNER"), 'green')) #banner
print("-" * 50)
f = Figlet(font='digital')
print(colored(f.renderText("by wtechsec"), 'green')) #banner
print("-" * 50)

input_data = input("Coloque IP e PORTA: ")
scan_row = input_data.split(" ")

if len(scan_row)!=2:
    print("Dados errados, olhe o exemplo  \"192.168.1.0/24 80,443,22\" ")
    sys.exit(0)

hosts=scan_row[0] #Recebe a informacao do host do usuario
port=scan_row[1] #recebe a informacao de porta do usuario

try:
 nm = nmap.PortScanner() #Cria um objeto de verificacao de porta
except nmap.PortScannerError:
    print('Nmap nao encontrado', sys.exc_info()[0])
    sys.exit(0)
except:
    print("erro nao esperado:", sys.exc_info()[0])
    sys.exit(0)


try:
 #metodo de verificacao comandos nmap
    nm.scan(hosts=hosts, arguments=' -v -sV -sS -p '+port)
except Exception as e:
    print("Scan erro:")+str(e)

for host in nm.all_hosts(): #scan host
   print('----------------------------------------------------')
print('Host : %s (%s)' % (host, nm[host].hostname())) #output host e  hostname
print('Status : %s' % nm[host].state()) #status do host saida como up ou down

for proto in nm[host].all_protocols(): #protocolo, de varredura como tcp, udp
    print('----------')
    print('Protocolo : %s' % proto) #insira o nome do protocolo

    lport = nm[host][proto].keys() #obter todas as portas da varredura do protocol
for port in lport: #status porta de entrada e saida
    print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))
