import unittest
from package import module1

class TestModule1(unittest.TestCase):
    def test_sum(self):
        test_list = [1, 2, 3]
        self.assertEqual(module1.sum_list(test_list), sum([1, 2, 3]), 'Should equal 6')

if __name__ == '__main__':
    unittest.main()