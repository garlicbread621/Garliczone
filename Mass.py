mass = float(input("Please enter this objects mass in kilograms: "))
gravity = 9.8
newtons = mass*gravity
if newtons < 100 : 
  print(" this object is too light")
elif newtons > 500 :
  print(" This object is too heavy")
else :
  print("this object weighs", newtons, "newtons.")
input("press ENTER to exit")  