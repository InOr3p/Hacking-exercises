from base64 import b64decode

flag1 = "ZmxhZ3t3NDF0XzF0c19hbGxfYjE="
flag2 = 664813035583918006462745898431981286737635929725

flag1_decoded = b64decode(flag1)
# length is the minimum number of BYTES we can use to represent the integer flag2
# bit_length() is the minimum number of BIT we can use to represent the integer flag2
# + 7) // 8 is used to convert the bits to bytes
length = (flag2.bit_length() + 7) // 8
print(length)
flag2_decoded = flag2.to_bytes(length, 'big')

print(flag1_decoded + flag2_decoded)