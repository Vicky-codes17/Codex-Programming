ph = int(input("Enter the value of ph between (0-14) :"))

if ph > 7:
  print("Basic")
elif ph < 7:
  print("Acidic")
else:
  print("Neutral")