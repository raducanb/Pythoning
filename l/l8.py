#1
import socket
import time

def listen_log(s):
    s.listen(1)
    (connection, address) = s.accept()
    current_time = time.asctime()
    with open("connections.txt", "a") as f:
        f.write(current_time + " " + str(address[0]) + " " + str(address[1]) + "\n")
    connection.close()

def start_listen_log():
    s = socket.socket()
    s.bind(("127.0.0.1", 1234))
    while True:
        listen_log(s)

# start_listen_log()