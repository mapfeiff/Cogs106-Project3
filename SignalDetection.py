#Import needed library
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

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
        #Check for Corruption
        if(self.hits < 0 or self.misses < 0):
            raise ValueError("Hits or Misses cannot be negative!")
        return self.hits / (self.hits + self.misses)

    #class method to get the false alarm rate: false alarms/total noise trials
    def falseAlarm_rate(self):
        #Check for Corruption
        if(self.falseAlarms < 0 or self.correctRejections < 0):
            raise ValueError("False Alarms or Correct Rejections cannot be negative!")
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

    #Plot the signal detection theory plot for the given object
    def plot_sdt(self):
        x = np.arange(-5, 5, 0.01)
        x_d_prime_line = np.arange(0, self.d_prime(), 0.01)
        #noise curve
        plt.plot(x, stats.norm.pdf(x, 0, 1))
        plt.annotate("Noise Curve", xy = (x[400], stats.norm.pdf(x[400], 0, 1)), 
                     xytext = (x[400]-3, stats.norm.pdf(x[400], 0, 1)+0.1), 
                     arrowprops=dict(facecolor='black', shrink=0.05), 
                     fontsize=15)
        #signal curve
        plt.plot(x, stats.norm.pdf(x, self.d_prime(), 1))
        annotate_index = round(999*(0.55 + self.d_prime()/10))
        plt.annotate("Signal Curve", xy = (x[annotate_index], stats.norm.pdf(x[annotate_index], self.d_prime(), 1)), 
                     xytext = (x[annotate_index]+0.5, stats.norm.pdf(x[annotate_index], self.d_prime(), 1)+0.05), 
                     arrowprops=dict(facecolor='black', shrink=0.05), 
                     fontsize=15)
        #Threshold line
        top_of_c = max(stats.norm.pdf(self.d_prime()/2 + self.criterion(), 0, 1), stats.norm.pdf(self.d_prime()/2 + self.criterion(), self.d_prime(), 1))
        plt.plot([self.d_prime()/2 + self.criterion(), self.d_prime()/2 + self.criterion()], [0, top_of_c], '-', color = "red")
        plt.annotate("threshold", xy = (self.d_prime()/2 + self.criterion()+0.05, top_of_c/4), fontsize = 15)
        #d' line
        plt.plot([0, self.d_prime()], [0.4, 0.4], '-', color = "green")
        plt.annotate("d'", xy=(self.d_prime()/2, 0.41), fontsize = 15)
        
        plt.xlabel("Decision Label")
        plt.ylabel("Probability")
        plt.title("Signal Detection Theory Plot")
        plt.ylim(0, 0.5)
        plt.show()

#sd = SignalDetection(75, 10, 55, 25)
#sd.plot_sdt()