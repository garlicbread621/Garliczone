price = 99
packages = int(input("Please enter amount of packages you wish to purchase: "))
sale=price*packages
if packages < 10:
  discount=sale*0
elif 10 < packages and packages < 20:
  discount=sale*.10
elif 19 < packages and packages < 50:
  discount=sale*.20
elif 49 < packages and packages < 100:
  discount=sale*.30
elif packages > 99:
  discount=sale*.40
total = sale-discount

print("You purchased", packages,"orders for a price of",sale, " dollars, you have saved", discount) 
print("dollars which brings your total down to",total,"dollars")
