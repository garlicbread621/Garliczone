while 1 ==1:

  primarycolory1 = input("Enter a primary color: ")
  primarycolor2 = input("Enter a different primary color: ")
  
  if (primarycolory1 == "red" and primarycolor2 == "blue") or (primarycolory1 == "blue" and primarycolor2 == "red") :
    print ("These colors fused become purple")
  elif (primarycolory1 == "red" and primarycolor2 == "yellow") or (primarycolory1 == "yellow" and primarycolor2 == "red") :
    print("These colors fused become orange")
  elif (primarycolory1 == "blue" and primarycolor2 == "yellow") or (primarycolory1 == "yellow" and primarycolor2 == "blue") :
    print("These colors fused become green")
  elif (primarycolor2 == "exit") or (primarycolory1 == "exit"):
    break
  else :
    print("ERROR, try again.")