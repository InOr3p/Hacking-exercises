import struct

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

# Use struct to pack hex as Little Endian (<) Unsigned Integers (I)
def fix_endian(hex_list):
    res = b""
    for h in hex_list:
        # <I means Little Endian 4-byte integer
        res += struct.pack("<I", h)
    return res

key_words = [0xdcbd30b2, 0x7be17a10, 0xece23b2c, 0x9ff00199]
flag_words = [0xbbdc5cd4, 0x4ad31e6b, 0xdfd25e4a, 0x00007cac]

key_bytes = fix_endian(key_words)
flag_bytes = fix_endian(flag_words)

result = xor(key_bytes, flag_bytes)

print(f"Decoded Flag: {result}")
