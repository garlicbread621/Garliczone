HDpack = 10
Bunpack = 8

people = float(input("How many people will be in attendance? "))
servings = float(input("how many servings is everyone getting? "))

HDneeded = people*servings
Bunsneeded = HDneeded

HDpackagesneeded = HDneeded/HDpack
Bunpackagesneeded = Bunsneeded/Bunpack

Hotdogremainder = HDneeded%HDpack
Bunsremainder = Bunsneeded%Bunpack

if Hotdogremainder > 0:
  HDpackagesneeded = int(HDpackagesneeded + 1)
if Bunsremainder > 0:
  Bunpackagesneeded = int(Bunpackagesneeded + 1)

HDowned = HDpackagesneeded*HDpack
Bunsowned = Bunpackagesneeded*Bunpack

HDleftover = HDowned - HDneeded
Bunsleftover = Bunsowned - Bunsneeded



print("This cookout requires at least",HDpackagesneeded,"Hot dog packages and",Bunpackagesneeded,"Bun packages")
print("There will be",HDleftover,"Hotdogs leftover and", Bunsleftover,"Buns leftover")