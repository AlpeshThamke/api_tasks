"""This is a experimentation code"""
import unittest

class TrialTests(unittest.TestCase):
    """This is me writing the unit tests for a normal check"""
    def test_super(self):
        """Check wether the test cases checks for super"""
        self.assertEqual("foo".upper(),"FOO")

    def test_split(self):
        """This checks for the error"""
        s = "hello world"
        self.assertEqual(s.split(),['hello','world'])

        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
