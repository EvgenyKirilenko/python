#program calculates the area of the given figure
#программа вычисляет площаль заданной фигуры
fg=input()
if fg == "треугольник":
    from math import sqrt
    a=int(input())
    b=int(input())
    c=int(input())
    p=float((a+b+c)/2)
    s=float(sqrt(p*(p-a)*(p-b)*(p-c)))
    print (s)
elif fg=="круг":
    r=int(input())
    s=3.14*r**2
    print (s)

elif fg=="прямоугольник":
    a=int(input())
    b=int(input())
    s=float(a*b)
    print(s)
