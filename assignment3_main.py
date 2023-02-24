#Import needed library
import scipy.stats as stats
#Plot
import matplotlib.pyplot as plt
import sklearn.metrics as metrics

import numpy as np
from scipy.optimize import curve_fit

#Implement class based on signal detection theory
class SignalDetection:
    #Class constructor
    def __init__(self, hits, misses, falseAlarms, correctRejections):
        #signal detection theory variables
        self.hits = hits 
        self.misses = misses
        self.falseAlarms = falseAlarms
        self.correctRejections = correctRejections
        
    #class method to get the hit rate: hits/total signal trials
    def hit_rate(self):
        return self.hits / (self.hits + self.misses)

    #class method to get the false alarm rate: false alarms/total noise trials
    def falseAlarm_rate(self):
        return self.falseAlarms / (self.falseAlarms + self.correctRejections)

    #class method to calculate d': Z(H) - Z(FA), Z = stats.norm.ppf
    def d_prime(self):
        #get z values
        z_hit = stats.norm.ppf(self.hit_rate()) 
        z_falseAlarm = stats.norm.ppf(self.falseAlarm_rate())
        #return d'
        return z_hit-z_falseAlarm

    #class method to get the criterion: -0.5*(Z(H) + Z(FA)), Z = stats.norm.ppf
    def criterion(self):
        #get Z values
        z_hit = stats.norm.ppf(self.hit_rate())
        z_falseAlarm = stats.norm.ppf(self.falseAlarm_rate())
        #return criterion
        return -0.5*(z_hit + z_falseAlarm)
        
    def __add__(self, other):
        return SignalDetection(self.hits + other.hits, self.misses + other.misses, self.falseAlarms + other.falseAlarms, self.correctRejections + other.correctRejections)

    def __mul__(self, scalar):
        return SignalDetection(self.hits * scalar, self.misses * scalar, self.falseAlarms * scalar, self.correctRejections * scalar)

    def plot_roc(self):
        x = np.array([0, self.falseAlarm_rate(), 1])
        y = np.array([0, self.hit_rate(), 1])
        plt.plot(x, y, 'o', label='Original points')
        plt.plot(x, y, '-')
        plt.title('Receiver Operating Characteristic')
        plt.xlim([0, 1])
        plt.ylim([0, 1])
        plt.ylabel('Hit Rate')
        plt.xlabel('False Alarm Rate')
        plt.show()
        
        #def fun(x, a, b, c):
            #return a * np.cosh(b * x )+ c
        #coef,_ = curve_fit(fun, x, y)
        #plt.plot(np.linspace(x[0],x[-1]), fun(np.linspace(x[0],x[-1]), *coef))
        #plt.plot(self.falseAlarm_rate(), self.hit_rate())
        #plt.plot([0, 1], ls="--")
        #plt.plot([0, 0], [1, 1] , c=".7")
        #plt.plot([1, 1] , c=".7")

    #def plot_roc(self):
        #roc_auc = metrics.auc(self.falseAlarm_rate(), self.hit_rate())
        #plt.title('Receiver Operating Characteristic')
        #plt.plot(self.falseAlarm_rate(), self.hit_rate(), 'b', label = 'AUC = %0.2f' % roc_auc)
        #plt.legend(loc = 'lower right')
        #plt.plot([0, 1], [0, 1],'r--')
        #plt.xlim([0, 1])
        #plt.ylim([0, 1])
        #plt.ylabel('True Positive Rate')
        #plt.xlabel('False Positive Rate')
        #plt.show()


#plots
sd = SignalDetection(15, 10, 15, 5)
sd.plot_roc()


    #def plot_sdt(SignalDetection):


#!/usr/bin/python3.8

import unittest
#from SignalDetection import SignalDetection

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

    #NEW!!
    def test_corruption(self):
        sd   = SignalDetection(15, 5, 15, 5)
        obtained_1 = sd.d_prime()
        sd.hits = 16
        obtained_2 = sd.d_prime()
        # Compare calculated and expected d-prime
        self.assertNotEqual(obtained_1, obtained_2)

if __name__ == '__main__':
    unittest.main()


