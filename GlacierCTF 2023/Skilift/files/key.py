tmp4=0x5443474D489DFDD3
tmp4=int(tmp4)
tmp3=tmp4+12345678
print(tmp3)
print(hex(tmp3))
tmp2 = tmp3 ^ int.from_bytes("HACKERS!".encode(), 'big')
print(tmp2)
tmp1 = tmp2 >> 5
print(tmp1)
# tmp1=hex(tmp1)
key = tmp1 & 0XF0F0F0F0F0F0F0F0
print(hex(key))
