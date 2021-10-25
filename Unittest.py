import unittest


class Test(unittest.TestCase):

    def test_add(self):
        a=15
        self.assertEqual(a,15)
        self.assertEqual(a,10)
if __name__ == '__main__':
    unittest.main()        
    

