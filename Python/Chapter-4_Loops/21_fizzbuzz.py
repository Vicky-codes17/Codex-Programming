for i in range(1,100):
  if i%3 ==0 and i%5==0:
    print("FizzBuzz")
  elif i%3==0:
    print("Fizz")
  elif i%5==0:
    print("Buzz")
  else:
    print(i)

### For multiples of 3, print "Fizz" instead of the number.
##  For multiples of 5, print "Buzz" instead of the number.
#   Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".