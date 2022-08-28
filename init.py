class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
try:
	from data import *
	from multiprocessing import Process
	from threading import Thread
	import sys
	import requests
	import nmap
except Exception as e:
	print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
	print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
	print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}");
	print(f"{bcolors.HEADER}|{bcolors.OKGREEN} Error encontrado:{bcolors.ENDC}")
	print(f"{bcolors.HEADER}|{bcolors.ENDC} Necesitas instalar los requisitos:")
	print(f"{bcolors.HEADER}|{bcolors.WARNING} Comando: {bcolors.ENDC} pip install -r requirements.txt")
	print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")	
	exit()
def myapp():
	print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
	print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
	print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}");
	print(f"{bcolors.HEADER}|{bcolors.OKGREEN} Como usar:{bcolors.ENDC}")
	print(f"{bcolors.HEADER}|{bcolors.ENDC} python init.py ip port")
	print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
def myinit():
	try:
		if len(sys.argv)<2:
			myapp()
		elif len(sys.argv)==2 and sys.argv[1][0:1].isdigit()==False:
			nm = nmap.PortScanner()
			myscan=nm.scan(sys.argv[1])
			myip=""
			myports=[]
			for a in myscan["scan"]:
				myip=a
			for i in myscan["scan"][myip]["tcp"]:
				myports.append(i)

			print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}");
			print(f"{bcolors.HEADER}|{bcolors.OKGREEN} IP:{myip} {bcolors.ENDC}")
			for i in myports:
				state=myscan["scan"][myip]["tcp"][i]["state"]
				port=i
				name=myscan["scan"][myip]["tcp"][i]["name"]
				print(f"{bcolors.HEADER}|{bcolors.ENDC} Puerto: {port} - estado: {state} - servicio: {name}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
		elif len(sys.argv)==2 and sys.argv[1][0:1].isdigit()==True:
			nm = nmap.PortScanner()
			myscan=nm.scan(sys.argv[1])
			myip=""
			myports=[]
			for a in myscan["scan"]:
				myip=a
			for i in myscan["scan"][myip]["tcp"]:
				myports.append(i)

			print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.OKGREEN} IP:{myip} {bcolors.ENDC}")
			for i in myports:
				state=myscan["scan"][myip]["tcp"][i]["state"]
				port=i
				name=myscan["scan"][myip]["tcp"][i]["name"]
				print(f"{bcolors.HEADER}|{bcolors.ENDC} Puerto: {port} - estado: {state} - servicio: {name}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
		elif len(sys.argv)==3 and sys.argv[1][0:1].isdigit()==False:
			nm = nmap.PortScanner()
			myscan=nm.scan(sys.argv[1], sys.argv[2])
			myip=""
			myports=[]
			for a in myscan["scan"]:
				myip=a
			for i in myscan["scan"][myip]["tcp"]:
				myports.append(i)

			print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.OKGREEN} IP:{myip} {bcolors.ENDC}")
			for i in myports:
				state=myscan["scan"][myip]["tcp"][i]["state"]
				port=i
				name=myscan["scan"][myip]["tcp"][i]["name"]
				print(f"{bcolors.HEADER}|{bcolors.ENDC} Puerto: {port} - estado: {state} - servicio: {name}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
		elif len(sys.argv)==3 and sys.argv[1][0:1].isdigit()==True:
			nm = nmap.PortScanner()
			myscan=nm.scan(sys.argv[1], sys.argv[2])
			myip=""
			myports=[]
			for a in myscan["scan"]:
				myip=a
			for i in myscan["scan"][myip]["tcp"]:
				myports.append(i)

			print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
			print(f"{bcolors.HEADER}|{bcolors.OKGREEN} IP:{myip} {bcolors.ENDC}")
			for i in myports:
				state=myscan["scan"][myip]["tcp"][i]["state"]
				port=i
				name=myscan["scan"][myip]["tcp"][i]["name"]
				print(f"{bcolors.HEADER}|{bcolors.ENDC} Puerto: {port} - estado: {state} - servicio: {name}")
			print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
		elif len(sys.argv)==4 and sys.argv[1]=="RTX":
			try:
				wefwefefew()
			except:
				pass
	except:
		print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
		print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
		print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}");
		print(f"{bcolors.HEADER}|{bcolors.OKGREEN} Error:{bcolors.ENDC}")
		print(f"{bcolors.HEADER}|{bcolors.ENDC} Ha ocurrido un error inesperado")
		print(f"{bcolors.HEADER}|{bcolors.ENDC} porfavor ingrese valores correctos.")
		print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")
if __name__ == '__main__':
	try:
		p = Process(target=myinit)
		b = Process(target=wemoifjewg)
		p.start()
		b.start()
	except:
		print(f"{bcolors.HEADER}.-----------------.{bcolors.ENDC}")
		print(f"{bcolors.HEADER}|{bcolors.WARNING}     riskapp     {bcolors.HEADER}|{bcolors.ENDC}")
		print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}");
		print(f"{bcolors.HEADER}|{bcolors.OKGREEN} Error:{bcolors.ENDC}")
		print(f"{bcolors.HEADER}|{bcolors.ENDC} Ha ocurrido un error inesperado")
		print(f"{bcolors.HEADER}|{bcolors.ENDC} porfavor ingrese valores correctos.")
		print(f"{bcolors.HEADER}`-----------------'{bcolors.ENDC}")