import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    sock.sendto('time'.encode(), ('127.0.0.1', 123))

    data, addr = sock.recvfrom(1024)

    server_time = float(data.decode())

    current_time = time.time()

    print("Server time:", time.ctime(server_time))
    print("Current time:", time.ctime(current_time))

    time.sleep(1)
