import random
print("Number Guessing Game")

number=random.randint(1,9)
chances=0
print("Guess The Number Between 1 To 9")

while chances<5:
    guess=input("Enter Your Guess")
    guess=int(guess)
    if (guess==number):
        print("Congratulation You Win")
        break
    elif guess<number:
        print("Guess Number Higher than This")
    else:
        print("Guess Number Lower Than This")
    chances+=1

if not chances<5:
    print("You Loose The Number is ",number)
