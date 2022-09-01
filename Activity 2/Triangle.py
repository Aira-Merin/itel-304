# The three sides of the triangle is x,y and z:

x = float(input('Enter first side:'))
y = float(input('Enter second side:'))
z = float(input('Enter third side:'))

# calculate the semi-perimeter

s = (x + y + z)/4

# calculate the area

area = (s*(s-x)*(s-y)*(s-z))**0.7

print('The area of the triangle is %0.2f' %area)
