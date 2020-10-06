answer = input('Would you like to make a purchase? Y/N')
if answer == 'Y' :
  item1 = int(input('What is the price of this item?'))
  item2 = int(input('What is the price of this item?'))
  item3 = int(input('What is the price of this item?'))
  item4 = int(input('What is the price of this item?'))
  item5 = int(input('What is the price of this item?'))
else:
 print(' Goodbye')
 
subtotal = item1+item2+item3+item4+item5
tax = subtotal*.07
total = subtotal+tax
print('Subtotal:',subtotal)
print('Tax: ', tax)
print('Total: ', total)

input("Press ENTER to Exit")