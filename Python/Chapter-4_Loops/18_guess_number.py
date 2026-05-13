guess = 0
tries = 0

while guess != 6 and tries < 5:
    guess = int(input("Enter the number : "))
    tries += 1
print("You got it!!")