#Import needed library
import scipy.stats as stats

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

