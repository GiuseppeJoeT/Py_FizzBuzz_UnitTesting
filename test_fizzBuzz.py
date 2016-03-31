import unittest
from fizzBuzz import

class test_fizzBuzz(unittest.TestCase):


    def test_is_this_thing_on(self):
        self.assertEquals(0, 0)

    def test_fizzBuzz(self):
        return 1

    def test_fizzBuzz_3_is_Fizz(self):
        self.assertEquals(self.fizzBuzz(3), "Fizz")

    def test_fizzBuzz_5_is_Buzz(self):
        self.assertEquals(self.fizzBuzz(5), "Buzz")

    def test_fizzBuzz_15_is_fizzBuzz(self):
        self.assertEquals(self.fizzBuzz(15), "FizzBuzz")

    def test_fizzBuzz_7(self):
        self.assertEquals(self.fizzBuzz(7), "")
