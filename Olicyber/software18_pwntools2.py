#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *
import re

def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-18.challs.olicyber.it"
    PORT = 13001
    r = remote(HOST, PORT)

    data = r.recvuntil(b" ...")
    print("0 - ", data)
    r.sendline(b"Ciao!")

    for i in range(100):
        data = r.recvline().decode()
        print("1 - ", data)

        re_groups = re.search(r"0x[0-9a-f]+", data)
        hex_num = int(re_groups.group(), 16)
        print(hex_num)

        r.recvuntil(b"Result :")

        if "64-bit" in data:
            r.send(p64(hex_num))
            print("p64 sent")
        else:
            r.send(p32(hex_num))
            print("p32 sent")

    data = r.recvline().decode()
    print(data)

    # # .send() può essere invocato sull'oggetto ritornato da remote() per inviare dati
    # r.send(b"Ciao!")

    # # .sendline() è identico a .send(), però appende un newline dopo i dati
    # r.sendline(b"Ciao!")

    # # .sendafter() e .sendlineafter() inviano la stringa "Ciao!"
    # r.sendafter(b"something", b"Ciao!")

    # # solo dopo che viene ricevuta la stringa "something"
    # r.sendlineafter(b"something", b"Ciao!")

    # # .recv() riceve e ritorna al massimo 1024 bytes dalla socket
    # data = r.recv(1024)

    # # .recvline() legge dalla socket fino ad un newline
    # data = r.recvline()

    # # .recvuntil() legge dalla socket finchè non viene incontrata la stringa "something"
    # data = r.recvuntil(b"something")

    # # permette di interagire con la connessione direttamente dalla shell
    # r.interactive()

    # chiude la socket
    r.close()


if __name__ == "__main__":
    main()
