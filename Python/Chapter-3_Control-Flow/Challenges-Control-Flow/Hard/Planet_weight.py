earth_weight = float(input('Enter your weight: '))

print("Choose a plant by its number")
print("1.Mercury\n2.Venus\n3.Mars\n4.Jupiter\n5.Saturn\n6.Uranus\n7.Neptune")
planet = int(input('Enter the planet number: '))

if planet == 1:
  relative_gravity = 0.38
elif planet == 2:
  relative_gravity = 0.91
elif planet == 3:
  relative_gravity = 0.38
elif planet == 4:
  relative_gravity = 2.53
elif planet == 5:
  relative_gravity = 1.07
elif planet == 6:
  relative_gravity = 0.89
elif planet == 7:
  relative_gravity = 1.14
else:
  print("Error! Inavlid planet number Choose in between 1 to 7")

destination_weight = earth_weight * 0.38

print(f"Your weight on the choosen planet is  :{destination_weight:.2f}kg")
