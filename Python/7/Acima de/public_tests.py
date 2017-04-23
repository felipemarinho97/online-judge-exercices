import unittest
import sys

undertest = __import__(sys.argv[-1].split(".py")[0])
acima_de = getattr(undertest, 'acima_de', None)

class PublicTests(unittest.TestCase):

   def test_1(self):
       assert acima_de(2, [1,0,2,6,9,-1]) == [3,4]
        
if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner()
    runner.run(loader.loadTestsFromModule(sys.modules[__name__]))
