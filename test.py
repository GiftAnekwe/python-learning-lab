#Pythagorean theorem
a = float(input("Give 'a' a number: "))
b = float(input("Give 'b' a number: "))
c = ((a**2 + b**2))**0.5
print("Working with the Pythagorean theorem, c =", c)
print('                                ')

print("Now, let's calculate another... hehehe")
#Quadratic formula
A = float(input("Give 'A' a number: "))
B = float(input("Give 'B' a number: "))
C = float(input("Give 'C' a number: "))
x_plus = (-B + ((B**2) - (4*A*C)))/2*A
x_minus = (-B - ((B**2) - (4*A*C)))/2*A
print('Using the Quadratic formula, X = ', x_plus, 'or', x_minus)
print('                                ')

print("Experimenting our acquired skills in currency exchange...")
#Currency exchange
pesos = float(input('How much worth of pesos remains? '))
pesos_usd = pesos*0.00027
soles = float(input('How much worth of soles remains? '))
soles_usd = soles*0.30
reais = float(input('How much worth of reais remains? '))
reais_usd = reais*0.19
USD_Total = int(pesos_usd + soles_usd + reais_usd)
print("Your total amount of leftover cash is approximately",USD_Total,"USD.")
print("                                  ")

#Debugging demo
'''
butterflies = 10
beetles = 12
ladybugs = 20
print('I caught ' + butterflies + ' 🦋 butterflies!')
print('I caught ' + beetles + ' 🪲 beetles!')
print('I caught ' + ladybug + ' 🐞 ladybugs!)
print('I caught ' + str(total) + ' total bugs!'
'''

#Debugged version
butterflies = 10
beetles = 12
ladybugs = 20
print('I caught ' + str(butterflies) + ' 🦋 butterflies!')
print('I caught ' + str(beetles) + ' 🪲 beetles!')
print('I caught ' + str(ladybugs) + ' 🐞 ladybugs!')
total = butterflies + beetles + ladybugs
print('I caught ' + str(total) + ' bugs in total!')
