#This file contains the python code for tasks assigned

import urllib.request
import urllib.parse
import urllib.error
import socket
import sys

from server_code import *

HOST = 'localhost'
PORT = 8088


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

def server_start_TCP():
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()



class MyUDPHandler(socketserver.BaseRequestHandler):
    """
    This class works similar to the TCP handler class, except that
    self.request consists of a pair of data and client socket, and since
    there is no connection the client address must be given explicitly
    when sending data back via sendto().
    """

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        print("{} wrote:".format(self.client_address[0]))
        print(data)
        socket.sendto(data.upper(), self.client_address)

def server_start_UDP():
    with socketserver.UDPServer((HOST,PORT),MyUDPHandler) as server:
        server.serve_forever()


def api_http_connect():
    url_inp = input("Please provide a url: ")
    url_data = input("Would you like to send additional data? If yes, type data and if not press enter: ")
    url_method = input("Type the name of method you would like to use else press enter: ")
    params = {}

    url_params_inp =  input("To enter params type 'params_enter' else press enter: ")
    if url_params_inp == 'params_enter':
        flag = 1
        while flag == 1:
            key = input("Key: ")
            value = input("Value: ")

            if key in params:
                raise ValueError("Key already present")

            val = input("to continue entering key-value pairs type 'y'  or to stop enter 'n': ")
            if val!='y':
                flag = 0

            params[key]=value

    if len(url_inp)==0:
        url_inp = None

    if len(url_data)==0:
        url_data = None
    else:
        url_data = url_data.encode('utf-8')

    if len(url_method)==0:
        url_method = None

    if len(params)!=0:
        params = urllib.parse.urlencode(params)
        url_inp = url_inp+params
    try:
        req = urllib.request.Request(url=url_inp,data=url_data,method=url_method)
        with urllib.request.urlopen(req) as f:
             print(f.read().decode('utf-8'))
    except OSError as e:
        print(str(e))

def main():
    while True:
        print("1 for API to access various services via HTTP")
        print("2 for Server with TCP IP")
        print("3 for Server with UDP IP")
        inp = int(input())

        if inp == 1:
            api_http_connect()
            
        if inp == 2:
            server_start_TCP()

        if inp == 3:
            server_start_UDP()
        




if __name__ == '__main__':
    main()
