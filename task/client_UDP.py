import socket
import sys


HOST, PORT = "localhost", 8088
data = " ".join(sys.argv[1:])

def start_server_UDP(data):
    # SOCK_DGRAM is the socket type to use for UDP sockets
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # As you can see, there is no connect() call; UDP has no connections.
    # Instead, data is directly sent to the recipient via sendto().
    sock.sendto(bytes(data + "\n", "utf-8"), (HOST, PORT))
    received = str(sock.recv(1024), "utf-8")

    print("Sent:     {}".format(data))
    print("Received: {}".format(received))
    return received

if __name__ == '__main__':
    start_server_UDP(data)
