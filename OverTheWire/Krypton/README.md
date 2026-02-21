# Krypton

## Level 0 -> Level 1

- SSH password in base64: S1JZUFRPTklTR1JFQVQ= (KRYPTONISGREAT)


## Level 1 -> Level 2

**Description:**
The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns. This file has kept the plain text word boundaries and carried them to the cipher text.

Encrypted password: YRIRY GJB CNFFJBEQ EBGGRA
Decrypted password: LEVEL TWO PASSWORD ROTTEN

## Level 2 -> Level 3

**Description**:
The password for level 3 is in the file krypton3. It is in 5 letter group ciphertext. It is encrypted with a Caesar Cipher. Without any further information, this cipher text may be difficult to break. You do not have direct access to the key, however you do have access to a program that will encrypt anything you wish to give it using the key. If you think logically, this is completely easy.

PT: UBUNTU
CT: GNGZFG

Caesar Cipher ROT14!!

Password:   AYCQYPGQCYQW
Decrypted:  OMQEMDUEQMEK
Decrypted2: CAESARISEASY
          
## Level 3 -> Level 4

- Decrypt by bruteforcing the password (check `krypton34.py` script). WELL DONE THE LEVEL FOUR PASSWORD IS BRUTE 

## Level 4 -> Level 5

**Description**: This level is a Vigenère Cipher. You have intercepted two longer, english language messages (American English). You also have a key piece of information. You know the key length!

For this exercise, the key length is 6. The password to level five is in the usual place, encrypted with the 6 letter key.

