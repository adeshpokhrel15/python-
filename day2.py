import random 
rand_num=random.randint(0,10)
print(rand_num        )
chances=3
while chances>0:
    guess=int(input("Enter the number:"))
    if rand_num == guess:
        print("Correct Guess")
    else:
        print("Incorrect guess")
        chances -= 1

#string methods
title="This is a python class"
len(title)

title.capitalize()