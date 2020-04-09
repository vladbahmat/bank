#!/usr/bin/env python3
import socket
import time

host = "127.0.0.1"
port = 6500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
#print(s.recv(1024).decode('utf8'))

while True:
    buf = input()
    s.send(buf.encode('utf8'))
    result = s.recv(1024)
    print(result.decode('utf8'))
    #print('Ответ сервера: ', result.decode('utf8'))
    #if buf == "exit":
      #  break
s.close()

time.sleep(10)