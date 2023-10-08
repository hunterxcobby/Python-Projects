#!/usr/bin/python3

"""Calculate BMI (m = height, kg = weight)"""

# define the function
def bmi_calc(weight, height):
    bmi = weight // (height ** 2)
    return (bmi)

# call the function
ami = bmi_calc(55, 1.76)
cobby = bmi_calc(55, 1.60)

if ami > cobby:
    print("Ami's bmi is heavier than Cobby's")
else:
    print("Cobby's bmi is heavier than Ami's")
