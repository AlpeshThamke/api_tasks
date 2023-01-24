import unittest
from range_ip import generate_ip

class range_test(unittest.TestCase):
    """
    Tests for generate_ip function
    """
    def setUp(self):
        self._random_CIDR = '123.45.67.89/27'

    def test_function_runs(self):
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


if __name__ == '__main__':
    unittest.main()