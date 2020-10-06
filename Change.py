pennies = int(input("Please enter amount of pennies you want: "))
nickels = int(input("Please enter amount of nickels you want: "))
dimes = int(input("Please enter amount of dimes you want: "))
quarters = int(input("Please enter amount of quarters you want: "))
halfdollar = int(input("Please enter amount of half dollars you want: "))

pennies = pennies*.01
nickels = nickels*.05
dimes = dimes*.10
quarters = quarters*.25
halfdollar = halfdollar*.5

total = pennies + nickels + dimes + quarters + halfdollar
if total == 1.00:
 print("you win! all the coins add up to 1 dollar.")
elif total < 1.00:
  print("not enough chump change, chump. Total: ", total)
elif total > 1.00:
  print("too much change chump. Total: ",total)


