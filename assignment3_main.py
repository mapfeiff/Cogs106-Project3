import unittest
from TestSignalDetection import TestSignalDetection
from SignalDetection import SignalDetection

def main():
    #Show example output
    print("Example output for different uses of the class:")
    #Show first sd subject in use
    sd1 = SignalDetection(75, 25, 10, 90)
    print("sd1 data:")
    print(f"\tHits = {sd1.hits}")
    print(f"\tMisses = {sd1.misses}")
    print(f"\tFalse Alarms = {sd1.falseAlarms}")
    print(f"\tCorrect Rejections = {sd1.correctRejections}")
    print(f"\tHit Rate = {sd1.hit_rate()}")
    print(f"\tFalse Alarm Rate = {sd1.falseAlarm_rate()}")
    print(f"\td' = {sd1.d_prime()}")
    print(f"\tCriterion Bias = {sd1.criterion()}")
    print(f"\tPrinting SDT plot...")
    sd1.plot_sdt()
    print(f"\tPrinting ROC plot...")
    sd1.plot_roc()

    #Second sd subject
    sd2 = SignalDetection(65, 35, 45, 55)
    print("\nsd2 data:")
    print(f"\tHits = {sd2.hits}")
    print(f"\tMisses = {sd2.misses}")
    print(f"\tFalse Alarms = {sd2.falseAlarms}")
    print(f"\tCorrect Rejections = {sd2.correctRejections}")
    print(f"\tHit Rate = {sd2.hit_rate()}")
    print(f"\tFalse Alarm Rate = {sd2.falseAlarm_rate()}")
    print(f"\td' = {sd2.d_prime()}")
    print(f"\tCriterion Bias = {sd2.criterion()}")
    print(f"\tPrinting SDT plot...")
    sd2.plot_sdt()
    print(f"\tPrinting ROC plot...")
    sd2.plot_roc()

    #Sum of sd1 and sd2 subject
    sd_sum = sd1 + sd2
    print("\nsd1 + sd2 data:")
    print(f"\tHits = {sd_sum.hits}")
    print(f"\tMisses = {sd_sum.misses}")
    print(f"\tFalse Alarms = {sd_sum.falseAlarms}")
    print(f"\tCorrect Rejections = {sd_sum.correctRejections}")
    print(f"\tHit Rate = {sd_sum.hit_rate()}")
    print(f"\tFalse Alarm Rate = {sd_sum.falseAlarm_rate()}")
    print(f"\td' = {sd_sum.d_prime()}")
    print(f"\tCriterion Bias = {sd_sum.criterion()}")
    print(f"\tPrinting SDT plot...")
    sd_sum.plot_sdt()
    print(f"\tPrinting ROC plot...")
    sd_sum.plot_roc()

    #Product of sd1 and 5 subject
    sd_prod = sd1 * 5
    print("\nsd1 * 5 data:")
    print(f"\tHits = {sd_prod.hits}")
    print(f"\tMisses = {sd_prod.misses}")
    print(f"\tFalse Alarms = {sd_prod.falseAlarms}")
    print(f"\tCorrect Rejections = {sd_prod.correctRejections}")
    print(f"\tHit Rate = {sd_prod.hit_rate()}")
    print(f"\tFalse Alarm Rate = {sd_prod.falseAlarm_rate()}")
    print(f"\td' = {sd_prod.d_prime()}")
    print(f"\tCriterion Bias = {sd_prod.criterion()}")
    print(f"\tPrinting SDT plot...")
    sd_prod.plot_sdt()
    print(f"\tPrinting ROC plot...")
    sd_prod.plot_roc()

    #run the unit tests
    print("\nNow Running Unit Tests...")
    unittest.main()

if(__name__ == "__main__"):
    main()