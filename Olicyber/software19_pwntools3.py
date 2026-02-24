#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *


def run_script(r, exe):
    # first intro msg
    data = r.recvuntil(b" ...")
    r.sendline(b"X")
    print("0 - ", data)

    for i in range(20):
        data = r.recvuntil(b": ").decode()
        print("1 - ", data)

        re_groups = re.search(r"\-\> (.+)\:", data)
        sym_value = re_groups.group(1)
        hex_value = hex(exe.sym[sym_value])
        print(sym_value, " - ", hex_value)

        r.sendline(hex_value)

    data = r.recvline().decode()
    print(data)
    return data


def main():
    '''
    remote(hostname, port) apre una socket e ritorna un object
    che può essere usato per inviare e ricevere dati sulla socket  
    '''
    exe = ELF("./sw-19")

    if args.REMOTE:
        r = remote("software-19.challs.olicyber.it", 13002)    
    else:
        r = process([exe.path])
    
    res = run_script(r, exe)

    r.close()


if __name__ == "__main__":
    main()
