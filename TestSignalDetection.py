#!/usr/bin/python3.8

import unittest
from SignalDetection import SignalDetection

class TestSignalDetection(unittest.TestCase):

    def test_d_prime_zero(self):
        sd   = SignalDetection(15, 5, 15, 5)
        expected = 0
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_d_prime_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        expected = -0.421142647060282
        obtained = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_criterion_zero(self):
        sd   = SignalDetection(5, 5, 5, 5)
        # Calculate expected criterion
        expected = 0
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_criterion_nonzero(self):
        sd   = SignalDetection(15, 10, 15, 5)
        # Calculate expected criterion
        expected = -0.463918426665941
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertAlmostEqual(obtained, expected, places=10)

    def test_addition(self):
        sd = SignalDetection(1, 1, 2, 1) + SignalDetection(2, 1, 1, 3)
        expected = SignalDetection(3, 2, 3, 4).criterion()
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertEqual(obtained, expected)

    def test_multiplication(self):
        sd = SignalDetection(1, 2, 3, 1) * 4
        expected = SignalDetection(4, 8, 12, 4).criterion()
        obtained = sd.criterion()
        # Compare calculated and expected criterion
        self.assertEqual(obtained, expected)

    def test_corruption_hits(self):
        sd = SignalDetection(1,2,3,4)
        sd.hits = -1
        #ensure error is raised in all methods where "hits" is used
        with self.assertRaises(ValueError):
            sd.hit_rate()
        with self.assertRaises(ValueError):
            sd.d_prime()
        with self.assertRaises(ValueError):
            sd.criterion()
        with self.assertRaises(ValueError):
            sd.plot_roc()
        with self.assertRaises(ValueError):
            sd.plot_sdt()

    
    def test_corruption_misses(self):
        sd = SignalDetection(1,2,3,4)
        sd.misses = -1
        #ensure error is raised in all methods where "misses" is used
        with self.assertRaises(ValueError):
            sd.hit_rate()
        with self.assertRaises(ValueError):
            sd.d_prime()
        with self.assertRaises(ValueError):
            sd.criterion()
        with self.assertRaises(ValueError):
            sd.plot_roc()
        with self.assertRaises(ValueError):
            sd.plot_sdt()

    def test_corruption_falseAlarms(self):
        sd = SignalDetection(1,2,3,4)
        sd.falseAlarms = -1
        #ensure error is raised in all methods where "falseAlarms" is used
        with self.assertRaises(ValueError):
            sd.falseAlarm_rate()
        with self.assertRaises(ValueError):
            sd.d_prime()
        with self.assertRaises(ValueError):
            sd.criterion()
        with self.assertRaises(ValueError):
            sd.plot_roc()
        with self.assertRaises(ValueError):
            sd.plot_sdt()

    def test_corruption_correctRejections(self):
        sd = SignalDetection(1,2,3,4)
        sd.correctRejections = -1
        #ensure error is raised in all methods where "correctRejections" is used
        with self.assertRaises(ValueError):
            sd.falseAlarm_rate()
        with self.assertRaises(ValueError):
            sd.d_prime()
        with self.assertRaises(ValueError):
            sd.criterion()
        with self.assertRaises(ValueError):
            sd.plot_roc()
        with self.assertRaises(ValueError):
            sd.plot_sdt()

    def test_corruption(self):
        sd   = SignalDetection(15, 5, 15, 5)
        obtained_1_d_prime = sd.d_prime()
        obtained_1_criterion = sd.criterion()
        sd.hits = 16
        obtained_2_d_prime = sd.d_prime()
        obtained_2_criterion = sd.criterion()
        # Compare calculated and expected d-prime and criterion to enure they are not equal (i.e., check if change to sd was saved)
        self.assertNotEqual(obtained_1_d_prime, obtained_2_d_prime)
        self.assertNotEqual(obtained_1_criterion, obtained_2_criterion)

if __name__ == '__main__':
    unittest.main()