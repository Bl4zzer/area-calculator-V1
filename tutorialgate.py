import math
import cmath
def arithmetic_operations():
    num1=float(input('first number: '))
    num2=float(input('first second: '))
    print(f'the sum :{num1+num2}')
    print(f'the difference :{num1-num2}')
    print(f'the product :{num1*num2}')
    print(f'the remainder :{num1/num2}')
    print(f'the quotient :{num1%num2}')
    print(f'the raised form :{num1**num2}')

def calendar():
    import calendar
    year=int(input('enter the year: '))
    month=int(input('enter the month: '))
    print(calendar.month(year,month))
def area():
    import math
    shape=input('Enter the shape: ').lower()
    if shape=='square':
        num1=float(input('enter the side the square: '))
        print('the area of the square is '+str(num1*num1)+' sq units')
    elif shape=='rectangle':
        num1=float(input('enter the length the square: '))
        num2=float(input('enter the breath the square: '))
        print('the are of the rectangle is '+str(num1*num2)+' sq units')
    elif shape=='triangle':
        num1 = float(input('enter the first side the square: '))
        num2 = float(input('enter the second side the square: '))
        num3= float(input('enter the third side the square: '))
        s=(num1+num2+num3)/2
        result2=(s*(s-num1)*(s-num2)*(s-num3)) ** 0.5
        print('the area of the triangle is '+str(result2)+' sq units')
    elif shape=='circle':
        unit=input('Are you going to enter the value in radius or diameter?: ' ).lower()
        if unit=='radius':
            r=float(input('enter the radius: '))
            area=math.pi*(r*r)
            print('the area of the circle is '+str(area)+' sq units')
        else:
            d=float(input('enter the diameter: '))
            area=(math.pi*0.25)*(d*d)
            print('the area of the circle is '+str(area)+' sq units')
def swap():
    num1 = float(input('enter a number: '))
    num2 = float(input('enter a number: '))
    num1,num2=num2,num1
    print(f'The swapped value is {num1} and {num2}')

def random():
    import random
    print(random.randint(1,3))
def posnegzero():
    num1 = float(input('enter a number: '))
    if num1>=0:
        if num1==0:
            print('the number you entered is equal to zero')
        else:
            print('it is an positive number')
    else:
        print('it is an negative number')
def oddeven():
    num1 = float(input('enter a number: '))
    if num1%2==0:
        print('it is an even number')
    else:
        print('it is an odd number')








