import random

print("Welcome to the Number Guessing game!")
low = int(input("Please enter your lower range: "))
high = int(input("Please enter your upper range: "))
print("You will get ten chances to guess the random number")

number = random.randint(low, high)
lim = 10
ges = 0

while ges < lim:
    ges += 1
    guess = int(input("Your Guess Number is: "))
    
    if guess == number:
        print(f"Congrats! You have guessed the number correctly.The number is {number}.")
        break
    elif guess > number:
        print("Your guess is far off to higher end.Go for a lower number")
    elif guess < number:
        print("Your guess is far off to lower end.Go for a higher number.")

if guess != number:
    print(f"You have used all your guesses. The number is {number}. Better luck next time!")
    