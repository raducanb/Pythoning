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

#3
import os
def listen_show_contents():
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 1234))
    while True:
        s.listen(1)
        (conn, address) = s.accept()
        conn.sendall(contents_current_dir().encode())
        conn.shutdown(socket.SHUT_RDWR)

def contents_current_dir():
    contents = ""
    for name in os.listdir():
        contents += name + "\n"
    return contents

listen_show_contents()