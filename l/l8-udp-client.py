import socket

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(b"Hello world", ("127.0.0.1", 1234))