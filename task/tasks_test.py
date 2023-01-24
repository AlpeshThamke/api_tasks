import unittest
from range_ip import generate_ip
from HTTP_API import http_connect
from server_code_TCP import server_TCP,server_TCP_shutdown
from client_TCP import start_client
from TCP_server_code import start_server_TCP
from client_UDP import start_server_UDP

class range_test(unittest.TestCase):
    """
    Tests for generate_ip function
    """
    def setUp(self):
        self._random_CIDR = '123.45.67.89/27'

    def test_generate_ip_function_runs(self):
        """
        This will test if the generate_ip function runs or not
        """
        generate_ip(self._random_CIDR)
    
    def test_network_type(self):
        """
        This will test if the network type is returned correct or not
        """
        self.assertEqual(generate_ip(self._random_CIDR)[0],'IPv4 Network')
    
    def test_ip_count(self):
        """
        This will count the number of IP(s) returned
        """
        self.assertEqual(len(generate_ip(self._random_CIDR)[1]),30)

class http_connect_test(unittest.TestCase):
    """
    Tests for HTTP Connection
    """
    def setUp(self):
        """
        Setting up the parameters to be passed to call the function
        """
        self._url = "http://info.cern.ch"
        self._data = ''
        self._method = ''
        self._params = ''
        self._data_size = 100
    
    def test_http_function_runs(self):
        """
        This will check if the api_http_connect function runs or not
        """
        http_connect(self._url,self._data,self._method,self._params,self._data_size)
    
    def test_http_correct_data_size(self):
        """
        This will test if the size of data returned is correct or not
        """
        self.assertEqual(len(http_connect(self._url,self._data,self._method,self._params,self._data_size)),self._data_size)

    def test_http_correct_return_type(self):
        """
        This will test if the returned data is decoded or not
        """
        self.assertEqual(type(http_connect(self._url,self._data,self._method,self._params,self._data_size)),type('string'))
    
    def test_http_incorrect_url(self):
        """
        This will test if the function throw exception when incorrect url is provided
        """
        with self.assertRaises(ValueError):
            http_connect("incorrect_url",self._data,self._method,self._params,self._data_size)

class server_tcp_test(unittest.TestCase):
    """
    Test Cases for Server_TCP
    """
    def setUp(self):
        """
        Creating a list of commands to test server
        """
        self._list_cmd = ["ls",'chmod','python3','mkdir','vim -y main.py']
    
    def test_server_tcp_runs(self):
        """
        Testing whether start_server function runs or not
        """
        start_server_TCP(self._list_cmd)

    def test_server_tcp_return_data(self):
        """
        Test for the size of returned data
        """
        self.assertEqual(len(start_server_TCP(self._list_cmd)),len(self._list_cmd))

class server_udp_test(unittest.TestCase):
    """
    Test Cases for Server_UDP
    """
    def setUp(self):
        """
        Creating a command/data to send to server
        """
        self._cmd = "alpesh thamke"
    
    def test_server_udp_runs(self):
        """
        Testing whether start_server function runs or not
        """
        start_server_UDP(self._cmd)

    def test_server_udp_return_data(self):
        """
        Test for the correctness of returned data
        """
        self.assertEqual(start_server_UDP(self._cmd),self._cmd.upper())
    
    def test_server_udp_return_size(self):
        """
        Test for the correct size of the returned data
        """
        self.assertEqual(len(start_server_UDP(self._cmd)),len(self._cmd))


if __name__ == '__main__':
    unittest.main()