from xmlrpc.server import SimpleXMLRPCServer

def fib(n):
    if n==1 or n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def xmlrpc_server():
    server = SimpleXMLRPCServer(("localhost", 8000))
    print("Listening on port 8000...")
    server.register_function(fib, "fib")
    server.serve_forever()

if __name__ == '__main__':
    xmlrpc_server()