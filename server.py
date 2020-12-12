import socket
import tqdm
import os
import datetime
import time
while True:
    os.system("cls")
    SERVER_HOST = "192.168.101.6"
    SERVER_PORT = 1218
    BUFFER_SIZE = 4096
    SEPARATOR = "<SEPARATOR>"
    f = datetime.datetime.now().strftime(" %Y-%m-%d %H-%M-%S")
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    print(f"[*] Escuchando como {SERVER_HOST}:{SERVER_PORT}")
    client_socket, address = s.accept() 
    print(f"[+] {address} esta conectado.")
    received = client_socket.recv(BUFFER_SIZE).decode()
    filename, filesize = received.split(SEPARATOR)
    filename = "keys {}.txt".format(f)
    filesize = int(filesize)
    progress = tqdm.tqdm(range(filesize), f"Recibiendo {filename}", unit="B", unit_scale=True, unit_divisor=1024)
    with open(filename, "wb") as f:
        for _ in progress:
            bytes_read = client_socket.recv(BUFFER_SIZE)
            if not bytes_read:    
                break
            f.write(bytes_read)
            progress.update(len(bytes_read))

    client_socket.close()
    s.close()
    time.sleep(3)