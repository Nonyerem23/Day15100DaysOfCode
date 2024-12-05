while exit != "yes":
  animal = input("What animal do you want? ")
  if animal == "cow":
    print("A cow goes moo.")
  elif animal == "dog":
    print("A dog goes woof.")
  elif animal == "cat":
    print("A cat goes meow.")
  else:
    print("I don't know that animal.")
  exit = input("Do you want to exit? ")
