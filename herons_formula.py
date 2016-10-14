#this code calculates the area of triangle by the length of the given sides
#by the Heron's formula

from math import sqrt

a=int(input("Enter side A:"))
b=int(input("Enter side B:"))
c=int(input("Enter side C:"))

p=float((a+b+c)/2)
s=float(sqrt(p*(p-a)*(p-b)*(p-c)))
print ("Area of the triangle is : ",s)
