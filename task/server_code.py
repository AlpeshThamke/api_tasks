import socketserver
import sys

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

def serving(HOST,PORT):
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()


if __name__ == "__main__":
    HOST= "localhost"
    #PORT = int(sys.argv[1])
    serving(HOST,int(PORT))

    
