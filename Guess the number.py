import random
a=random.randrange(1,100)

c=input("Enter how many tries you want: ")

for tries in range(0,int(c)):

    guess = int(input("Guess the number:"))

    if guess == a:
        print("Congratulations your guess is right")
        break

    elif guess > a and guess <= a + 5:
        print("It's a little bit higher")
    elif guess < a and guess >= a - 5:
        print("It's a little bit lower")
    elif guess > a and guess <= a + 15:
        print("It's close but still high")
    elif guess < a and guess >= a - 15:
        print("It's close but still low")
    elif guess > a + 15:
        print("It's very high")
    elif guess < a - 15:
        print("It's very low")

if guess!=a:
    print("Sorry. Better luck next time")
