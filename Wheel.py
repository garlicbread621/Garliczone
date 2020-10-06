bet = int(input("please enter a whole number between 0 and 36: "))

if bet < 0 or bet > 36:
  print("This number is not within 0 and 36")
else:
 if bet == 0:
  print('This is a green space')
 elif bet < 11:
   if bet % 2 == 0:
     print("this space is black")
   else:
      print("This space is red")
 elif bet>10 and bet<19:
    if bet % 2 == 0:
      print("This is a red space")
    else:
      print("This is a black space")
 elif bet > 19 and bet < 28:
    if bet%2 == 0:
      print("this space black")
    else:
      print("this pace red")
 elif bet >= 29:
   if bet%2 == 0:
     print("this space be red") 
   else: 
      print("this space be black")
    