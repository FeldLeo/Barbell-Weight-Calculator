def weight_to_plate(): # Calculates which plates to add to reach x amount of lbs
  weight = int(input("\nEnter the total weight in pounds: "))
  bar = weight - 45
  gross = bar / 45
  plates = bar // 45
  if plates % 2 == 0:
    fortyFives = plates
    print("\nAdd " + str(fortyFives / 2) +  " 45lbs plate(s) on each side of a 45lbs bar.")
  else:
    fortyFives = plates - 1
    print("\nAdd " + str(fortyFives / 2) + " 45lbs plate(s) on each side of a 45lbs bar.")
  
  secondGross = (gross * 45) - (fortyFives * 45)
  thirtyFives = secondGross // 35
  if thirtyFives % 2 == 0:  
    thirtyFivesBar = thirtyFives
    print("\nAdd " + str(thirtyFivesBar / 2) +  " 35lbs plate(s) on each side of a 45lbs bar.")
  else:
    thirtyFivesBar = thirtyFives - 1
    print("\nAdd " + str(thirtyFivesBar / 2) +  " 35lbs plate(s) on each side of a 45lbs bar.")
  
  thirdGross = (secondGross) - (thirtyFivesBar * 35)
  twentyFives = thirdGross // 25
  if twentyFives % 2 == 0:
    twentyFivesBar = twentyFives
    print("\nAdd " + str(twentyFivesBar / 2) +  " 25lbs plate(s) on each side of a 45lbs bar.")
  else:
    twentyFivesBar = twentyFives - 1
    print("\nAdd " + str(twentyFivesBar / 2) +  " 25lbs plate(s) on each side of a 45lbs bar.")

  fourthGross = (thirdGross) - (twentyFivesBar * 25)
  tens = fourthGross // 10
  if tens % 2 == 0:
    tensBar = tens
    print("\nAdd " + str(tensBar / 2) +  " 10lbs plate(s) on each side of a 45lbs bar.")
  else:
    tensBar = tens - 1
    print("\nAdd " + str(tensBar / 2) +  " 10lbs plate(s) on each side of a 45lbs bar.")

  fifthGross = (fourthGross) - (tensBar * 10)
  fives = fifthGross // 5
  if fives % 2 == 0:
    fivesBar = fives
    print("\nAdd " + str(fivesBar / 2) +  " 5lbs plate(s) on each side of a 45lbs bar.")
  else:
    fivesBar = fives - 1
    print("\nAdd " + str(fivesBar / 2) +  " 5lbs plate(s) on each side of a 45lbs bar.")

  sixthGross = (fifthGross) - (fivesBar * 5)
  halfFives = sixthGross // 2.5
  if halfFives % 2 == 0:
    halfFivesBar = halfFives
    print("\nAdd " + str(halfFivesBar / 2) +  " 2.5lbs plate(s) on each side of a 45lbs bar.")
  else:
    halfFivesBar = halfFives - 1
    print("\nAdd " + str(halfFivesBar / 2) +  " 2.5lbs plate(s) on each side of a 45lbs bar.")


weight_to_plate()
  
  
  
  
