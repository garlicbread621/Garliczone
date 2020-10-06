speed= int(input('how fast is the car moving: '))
hours= int(input('how long has the car been moving: '))

distance= speed*hours

stuff= 'in {} hours the car will have traveled {} miles'.format(hours, distance)
print(stuff)
input("Press ENTER to Exit")