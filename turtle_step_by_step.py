import math

'''Remember I said we will solve this problem in 2 parts? Here is the part 1

Part 1:  Calculate the dimensions and angles of inclination of the triangle

In order to use turtle to draw a right angled triangle we must know the angles of the three  so therefore we will use Sine, Cosine and Tangent(SOHCAHTOA)
Step 1: Calculate the hypotenuse of the right angled triangle
Define Python variables'''
o = 2.5 #Where o is the opposite
h = 5  #Where h is the hypotenuse
a = o/h #Where a is the adjacemt
print(a)

'''
Step 2: Calculate theangle of inclinition using the SohCahToa
SOH
sin = o/h
baseangle = arcsine**-1 (o/h)
'''
base_angle = math.asin(a)
base_angle = math.degrees(base_angle)
print(base_angle)
'''
Step 3: Calculate the angle of inclination
angleofinclination = 180 - 90 - baseangle
angleofinclination  = 

Summary:
In this part one of the design a right angle triangle using python turtle, we have demonstrated how to use the mass module to do so.
'''
