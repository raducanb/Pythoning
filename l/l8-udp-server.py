#2
import socket
import time
import binascii
import hashlib
import os

def udp_log(s):
    while True:
        data, address = s.recvfrom(1024)
        data = data.decode()
        hour_and_date = time.strftime("%H:%M, %Y.%m.%d", time.localtime())
        md5 = hashlib.md5(binascii.hexlify(data.encode())).hexdigest()
        sha256 = hashlib.sha256(binascii.hexlify(data.encode())).hexdigest()
        with open("logs_udp.txt", "a") as f:
            f.write(hour_and_date + " - " + address[0] + "- " + str(address[1]) + " - " + str(len(data)) + " - " + md5 + " - " + sha256 + "\n")

def udp_listen():
    s = socket.socket(type = socket.SOCK_DGRAM)
    s.bind(("127.0.0.1", 1234))
    udp_log(s)

udp_listen()