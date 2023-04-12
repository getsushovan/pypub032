#Write a program to guess the number
 
import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Guessed low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Guessed high!")
        guess = int(input("Enter number again: "))
    else:
      break

print("You guessed it right, the number is %d"%(n))


