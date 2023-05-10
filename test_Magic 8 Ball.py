Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... name = "John"
... question = "Will I win the lottery?"
... answer = ""
... random_number = random.randint(1,9)
... # print(random_number)
... 
... if random_number == 1:
...   answer = "Yes - definitely"
... elif random_number == 2:
...   answer = "It is decidedly so"
... elif random_number == 3:
...   answer = "Without a doubt"
... elif random_number == 4:
...   answer = "Reply hazy, try again"
... elif random_number == 5:
...   answer = "Ask again later"
... elif random_number == 6:
...   answer = "Better not tell you now"
... elif random_number == 7:
...   answer = "My sources say no"
... elif random_number == 8:
...   answer = "Outlook not so good"
... elif random_number == 9:
...   answer = "Very doubtful"
... else:
...   answer = "Error"
... if name == "":
...   print(question)
... else:
...   print(name, "asks:", question)
... if question == "":
...   print("We cannot proceed!")
... else:
