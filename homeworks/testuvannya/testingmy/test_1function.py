import unittest
import function1_for_testing as fft

class FunctionsTest(unittest.TestCase):


    def test_div(self):
        self.assertEqual(fft.div(5, 10), 0.5)
        self.assertNotEqual(fft.div(20, 5), 3)
        self.assertEqual(fft.div(200, 40), 5)
        self.assertEqual(fft.div(850, 25), 34)


