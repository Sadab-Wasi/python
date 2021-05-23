import unittest
import unittest
from exercise2 import lottery

class TestExercise2(unittest.TestCase):
    
    def test_lottery(self):
        result = lottery(10)

        # check if size of list is 10
        self.assertEqual( len(result),10 )

        # check if the list starts from number more than 0
        self.assertGreater( result[0],0 )
        
        # check if the list is in assecding order
        for i in range(9):
            self.assertGreater( result[i+1],result[i] )
        
        # check if the list ends from number less than 50
        self.assertLess( result[9],50 )

if __name__ == '__main__':
    unittest.main()