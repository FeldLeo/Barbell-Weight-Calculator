def weight_to_plate(): # Calculates which plates to add to reach x amount of lbs
  weight = int(input("\nEnter the total weight in pounds")
  bar = weight - 45
  gross = bar / 45
  plates = bar // 45
  if plates % 2 = 0:
    fortyFives = plates
    print("\nAdd " + str(plates / 2) +  " 45lbs plate(s) on each side of a 45lbs bar.")
  else:
    fortyFives = plates - 1
    print("\nAdd " str(fortyFives / 2) + " 45lbs plate(s) on each side of a 45lbs bar.")
  newGross = (gross * 45) - (plates * 45)
  
  
  
  
