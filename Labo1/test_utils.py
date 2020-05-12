import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(4), 24)
        self.assertEqual(utils.fact(0), 1)
        
        with self.assertRaises(ValueError):
            utils.fact(-1)
        with self.assertRaises(TypeError):    
            utils.fact("k")
    
    def test_roots(self):
        self.assertEqual(utils.roots(4,1,2), "No roots")
        self.assertEqual(utils.roots(1,2,1), -1)
        self.assertEqual(utils.roots(2,5,2), (-1/2,-2))
        with self.assertRaises(TypeError):    
            utils.roots("a",2,"c")
              
    def test_integrate(self):
        # À compléter...
        pass

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
