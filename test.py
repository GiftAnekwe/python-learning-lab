#Pythagorean Theorem

a = int(input("Give 'a' a number: "))
b = int(input("Give 'b' a number: "))
c = ((a**2 + b**2))**0.5
print("Working with the Pythagorean theorem, c =", c)
print('Another calc incoming.... hehehe')
print('                                ')


#Quadratic Formula
A = int(input("Give 'A' a number: "))
B = int(input("Give 'B' a number: "))
C = int(input("Give 'C' a number: "))
x_plus = (-B + ((B**2) - (4*A*C)))/2*A
x_minus = (-B - ((B**2) - (4*A*C)))/2*A
print('Using the Quadratic formula, X = ', x_plus, 'or', x_minus)
