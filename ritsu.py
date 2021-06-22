import colorama 
from colorama import Fore, Back, Style 
colorama.init(autoreset=True)
import os, colorama, platform, socket
from colorama import Fore
so = platform.system()

def clear():
	if so == "Windows":
		os.system("cls")
	else:
		os.system("clear")

def help():
	print(f"""{Fore.LIGHTCYAN_EX}
╔═══════════════╦═══════════════════════════╗
║               ║                           ║
║ scan          ║ Obtiene puertos de una IP ║
║ getip         ║ Obtiene la IP del servidor║
║ dedfinder     ║ Encuentra deds en el sv   ║
║               ║                           ║
║ clear         ║  Limpia la pantalla       ║
║               ║                           ║
╠═══════════════╩═══════════════════════════╣
║                                           ║
║ https://discord.gg/teHjXfD5               ║
║ Ghostrick                                 ║
║ #SafoSquad                                ║
║                                           ║
╚═══════════════════════════════════════════╝
	""")

def logo():
	print(f"""{Fore.RED}

     
  	
     

 ██▀███   ██▓▄▄▄█████▓  ██████  █    ██ 
▓██ ▒ ██▒▓██▒▓  ██▒ ▓▒▒██    ▒  ██  ▓██▒
▓██ ░▄█ ▒▒██▒▒ ▓██░ ▒░░ ▓██▄   ▓██  ▒██░
▒██▀▀█▄  ░██░░ ▓██▓ ░   ▒   ██▒▓▓█  ░██░
░██▓ ▒██▒░██░  ▒██▒ ░ ▒██████▒▒▒▒█████▓ 
░ ▒▓ ░▒▓░░▓    ▒ ░░   ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ 
  ░▒ ░ ▒░ ▒ ░    ░    ░ ░▒  ░ ░░░▒░ ░ ░ 
  ░░   ░  ▒ ░  ░      ░  ░  ░   ░░░ ░ ░ 
   ░      ░                 ░     ░     
                                        
                           \033[1;33m#SafoSquad | Ghostrick\033[1;m                                                     
                                                              
                                                              """)
	print(f"{Fore.LIGHTBLUE_EX}Escribe la palabra help para ver los comandos..")
def main1():
	clear()
	logo()
	while True:
		cmd = input(f"{Fore.GREEN}root@Ritsu:~{Fore.LIGHTGREEN_EX}")
		if cmd == "help":
			help()
		elif cmd == "clear":
			clear()
			logo()
		elif cmd == "scan":
			scan()
		elif cmd == "getip":
			getip()
		elif cmd == "dedfinder":
			dedfinder()
		else:
			print(f"{Fore.RED}Comando desconocido. Escriba help.")

def getip():
	domain = input("Insertar dominio: ")
	result = socket.gethostbyname(str(domain))
	print(result)

def dedfinder():
	ip = input("Insertar dominio: ")
	deds = ["node1", "node2", "node3", "node 4", "node5", "node6", "node7", "node8", "node9", "node10", "node11", "node12", "node13", "node14", "node15", "node16", "node17", "node18", "node19", "node20", "node001", "node002", "node01", "node02", "node003", "sys001", "sys002", "go", "admin", "eggwars", "bedwars", "lobby1", "hub", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "builds", "testing", "server", "pvp", "skywars", "survival", "skyblock", "lobby", "hg", "games", "sys001", "sys002", "node001", "node002", "games001", "games002", "us72", "us1", "us2", "us3", "us4", "us5", "goliathdev", "staticassets", "rewards", "rpsrv", "ftp", "ssh", "web", "jobs", "render", "www", "build", "web", "dev", "staff", "mc", "play", "sys", "live"]
	for subd in subdominios:
		try:
			ipsrv = str(subd) + "."+str(ip)
			iphost = socket.gethostbyname(str(ipsrv))
			print (Fore.LIGHTBLACK_EX + "    [" + Fore.GREEN + "√" + Fore.LIGHTBLACK_EX + "]" + Fore.GREEN + " Subdomain found " + Fore.LIGHTBLACK_EX + "» " + Fore.LIGHTWHITE_EX + "" + str(subd)+"."+str(ip) + Fore.BLACK+"" + str(iphost))
		except:
			pass

def scan():
	ip = input("Servidor IP: ")
	ports = input("Puertos: ")
	os.system(f"nmap -p {ports} -v -T5 --open -Pn -A {ip}")
main1()
