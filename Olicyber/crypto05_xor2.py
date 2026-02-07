
ciphertext = "104e137f425954137f74107f525511457f5468134d7f146c4c"
cipher_bytes = bytes.fromhex(ciphertext)

def xor_with_key(data, key):
    return bytes(b ^ key for b in data)

for key in range(256):
    plaintext = xor_with_key(cipher_bytes, key)
    print(plaintext)