from range_ip import generate_ip
from HTTP_API import http_connect
from server_code_TCP import server_TCP
from server_code_UDP import server_UDP

HOST = 'localhost'
PORT = 8088

def main():
    while True:
        print("1 for API to access various services via HTTP")
        print("2 for Server with TCP IP")
        print("3 for Server with UDP IP")
        print("4 for creating a range of IP Addresses")
        inp = int(input())
        if inp == 1:
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
            print(http_connect(url_inp,url_data,url_method,params,100))
        if inp == 2:
            server_TCP()
        if inp == 3:
            server_UDP()
        if inp == 4:
            inp_ip = input("Enter CIDR network: ")
            network_type,list_ip = generate_ip(inp_ip)
            print(network_type)
            for x in list_ip:
                print(x)



if __name__ == '__main__':
    main()
