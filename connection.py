from socket import socket, AF_INET, SOCK_STREAM
import sys,pickle

def setConnection(data_list):
    HOST = '192.168.43.185'
    PORT = 50001
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((HOST, PORT))
    data_bytes = pickle.dumps(data_list)
    s.send(data_bytes)
    recv_data = s.recv(4096)
    result = pickle.loads(recv_data)
    return result
    