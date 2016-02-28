#! /usr/bin/python
import socket

host="127.0.0.1"

#port should be integer
port=80

#SOCK_DGRAM indicates a UDP client.
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Because UDP is connectionless there is no connect() method needed.
client.sendto("Avicoder is Best",(host,port))

data, addr = client.recvfrom(4096)

print data
print addr

