import sys
import urllib.request
import urllib.parse
import urllib.error

def http_connect(url_inp,url_data,url_method,params,data_size):

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
            return f.read(data_size).decode('utf-8')

    except OSError as e:
        print(str(e))


if __name__ == '__main__':
    http_connect(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])