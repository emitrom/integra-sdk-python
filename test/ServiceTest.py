import unittest
from RestTemplate import RestTemplate

class ServiceTest(unittest.TestCase):

    def setUp(self):
        RestTemplate().init('https://localhost:8443/rest', 'admin', 'integra')
        
if __name__ == "__main__":
    unittest.main()
