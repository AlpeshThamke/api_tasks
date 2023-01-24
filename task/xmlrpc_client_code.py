import xmlrpc.client

def xmlrpc_client(data):
    res = []
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        for items in data:
            res.append("{} number in Fibonacci Series: {}".format(items,str(proxy.fib(items))))
        return res

if __name__ == '__main__':
    data = []
    xmlrpc_client(data)