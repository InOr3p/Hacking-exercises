#!/usr/bin/env python3

import ast
# Importa la libreria di pwntools
from pwn import *


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    HOST = "software-17.challs.olicyber.it"
    PORT = 13000
    r = remote(HOST, PORT)

    data = r.recvuntil(b" ...")
    print("0 - ", data)
    r.sendline(b"Ciao!")

    for i in range(10):
        data = r.recvline()
        # Somma questi numeri
        print("1 - ", data)

        # int array
        data = r.recvline()
        data_str = data.decode().strip()
        print("2 - ", data_str)
        int_array = ast.literal_eval(data_str)

        print(f"First element: {int_array[0]}")
        print(f"Length: {len(int_array)}")
        res = sum(int_array)
        print("Sum: ", res)

        # Array sum input
        data = r.recvuntil(b":")
        print("3 - ", data)

        r.sendline(str(res).encode())

    # Receive flag 
    data = r.recvline()
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
