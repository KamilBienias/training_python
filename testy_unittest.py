import unittest

def plus_one(x):
    return x+1

def plus_x(num):
    def plus_inner(x):
        return x + num
    return plus_inner

class PlusTest(unittest.TestCase):
    def setUp(self):
        self.plus_three = plus_x(3)

    def test_plus_one(self):
        # self.assertEqual(plus_one(3), 4) # to przechodzi
        self.assertEqual(self.plus_three(3), 6)

unittest.main(argv=['first-arg-is-ignored'], exit=False)