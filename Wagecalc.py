wage = input('Enter your wage: ',)

w = int(wage)

hours = input('Enter your hours:',)

h = int(hours)

overtimewage = (h-40)*w*1.5

if h>40:
    pay = 40*w+overtimewage
else:
    pay = h*w
print('your pay is:', pay)
input("Press ENTER to Exit")