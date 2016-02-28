#! /usr/bin/python

#import socket module
import socket


host="www.avicoder.me"
port=80

#client is a socket object, AF_INET is saying we are going to use IPv4 address or hostname.
# SOCK_STREAM indicates that will be TCP client
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client.connect((host,port))

client.send("GET / HTTP/1.1\r\nHost: avicoder.me\r\n\r\n")

response=client.recv(4096)

print response


