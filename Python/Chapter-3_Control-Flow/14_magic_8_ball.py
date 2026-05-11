import random

Question  = input("Question: ")

random_num = random.randint(1,9)
if random_num == 1:
  result = "Yes-definitely"
elif random_num == 2:
  result = "It is decidedly so"
elif random_num == 3:
  result = "Without a doubt"
elif random_num == 4:
  result = "Reply hazy,try again"
elif random_num == 5:
  result = "Ask again later"
elif random_num == 6:
  result = "Better not tell you now"
elif random_num == 7:
  result = "My sources say no"
elif random_num == 8:
  result = "Outlook not so good"
elif random_num == 9:
  result = "Very doubtful"
else:
  result = "error"
print("Magic Ball 8 : "+result)