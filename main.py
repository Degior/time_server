import socket
import time
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(('127.0.0.1', 123))

with open('config.txt', 'r') as f:
    offset = float(f.readline().strip())


def modify_time(current_time):
    if random.random() < 0.5:
        modified_time = current_time + offset
    else:
        modified_time = current_time - offset

    return modified_time


while True:
    data, addr = sock.recvfrom(1024)

    current_time = time.time()

    modified_time = modify_time(current_time)

    sock.sendto(str(modified_time).encode(), addr)
