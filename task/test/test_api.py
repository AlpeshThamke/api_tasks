"""This module is exclusively testing for the unit test \
     of every functionality
"""
import unittest
import sys
sys.path.append("../")

from src.APITASK.ip_generator import generate_ip
from src.APITASK.http_api import http_connect
from src.APITASK.tcp_server_code import start_server_tcp
from src.APITASK.udp_client import start_server_udp
from src.APITASK.xmlrpc_client_code import xmlrpc_client

class RangeTest(unittest.TestCase):
    """Tests for generate_ip function
    """
    def setUp(self):
        self._random_cidr = '123.45.67.89/27'

    def test_generate_ip_function_runs(self):
        """This will test if the generate_ip function runs or not
        """
        generate_ip(self._random_cidr)

    def test_network_type(self):
        """This will test if the network type is returned correct or not
        """
        self.assertEqual(generate_ip(self._random_cidr)[0],'IPv4 Network')

    def test_ip_count(self):
        """This will count the number of IP(s) returned
        """
        self.assertEqual(len(generate_ip(self._random_cidr)[1]),30)

class HTTPConnectTest(unittest.TestCase):
    """Tests for HTTP Connection
    """
    def setUp(self):
        """Setting up the parameters to be passed to call the function
        """
        self._url = "http://info.cern.ch"
        self._data = ''
        self._method = ''
        self._params = ''
        self._data_size = 100

    def test_http_function_runs(self):
        """This will check if the api_http_connect function runs or not
        """
        http_connect(self._url,self._data,self._method,
            self._params,self._data_size)

    def test_http_correct_data_size(self):
        """This will test if the size of data returned is correct or not
        """
        self.assertEqual(len(http_connect(self._url,
            self._data,self._method,self._params,self._data_size)),
                self._data_size)

    def test_http_correct_return_type(self):
        """This will test if the returned data is decoded or not
        """
        self.assertEqual(type(http_connect(self._url,self._data,
            self._method,self._params,self._data_size)),type('string'))

    def test_http_incorrect_url(self):
        """This will test if the function throw exception when \
             incorrect url is provided
        """
        with self.assertRaises(ValueError):
            http_connect("incorrect_url",self._data,self._method,
                self._params,self._data_size)

class ServerTCPTest(unittest.TestCase):
    """Test Cases for Server_TCP
    """
    def setUp(self):
        """Creating a list of commands to test server
        """
        self._list_cmd = ["ls",'chmod','python3','mkdir','vim -y main.py']

    def test_server_tcp_runs(self):
        """Testing whether start_server function runs or not
        """
        start_server_tcp(self._list_cmd)

    def test_server_tcp_return_data(self):
        """Test for the size of returned data
        """
        self.assertEqual(len(start_server_tcp(self._list_cmd)),
            len(self._list_cmd))

class ServerUDPTest(unittest.TestCase):
    """Test Cases for Server_UDP
    """
    def setUp(self):
        """Creating a command/data to send to server
        """
        self._cmd = "alpesh thamke"

    def test_server_udp_runs(self):
        """Testing whether start_server function runs or not
        """
        start_server_udp(self._cmd)

    def test_server_udp_return_data(self):
        """Test for the correctness of returned data
        """
        self.assertEqual(start_server_udp(self._cmd),self._cmd.upper())

    def test_server_udp_return_size(self):
        """Test for the correct size of the returned data
        """
        self.assertEqual(len(start_server_udp(self._cmd)),len(self._cmd))

class XMLRPCTest(unittest.TestCase):
    """Tests for running python program on remote server
    """
    def setUp(self):
        """Setting up the input parameters for the xmlrpc_client function
        """
        self._data = [1,2,3,4,5,10,11]

    def test_xmlrpc_client_runs(self):
        """Test wether xmlrpc_client function runs or not
        """
        xmlrpc_client(self._data)

    def test_xmlrpc_client_output_size(self):
        """Test wether the returned output size is as expected or not
        """
        self.assertEqual(len(xmlrpc_client(self._data)),len(self._data))

    def test_xmlrpc_client_correct_output(self):
        """Test for the correctness of the output
        """
        self.assertEqual(xmlrpc_client(self._data)[6],
            '11 number in Fibonacci Series: 89')

if __name__ == '__main__':
    unittest.main()
