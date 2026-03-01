import string

enc_str = "607d2135370554002033714d180f3340010f2524755b1e7d2658791526124641157e32464d233c3a"
start_flag = "THM{"
xored = ""

enc_str = bytes.fromhex(enc_str)

for i in range(0,len(start_flag)):
    xored += chr(ord(start_flag[i]) ^ enc_str[i%len(enc_str)])

key_set = string.ascii_letters + string.digits

i = 0

for k in key_set:
    complete_flag = ""
    i += 1
    tmp_key = xored + k

    for j in range(0,len(enc_str)):
        complete_flag += chr(enc_str[j] ^ ord(tmp_key[j%len(tmp_key)]))

    if complete_flag.endswith("}"):
        print(f"Flag 1: {complete_flag}")
        print(f"Key: {tmp_key}")

"""
encryption key: 45lNG
FLAG 1: THM{p1alntExtAtt4ckcAnr3alLyhUrty0urxOr}
"""

