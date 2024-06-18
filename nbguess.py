import random

n = random.randint(1, 10)
print("Guess the number between 1 and 20. I'll give you 3 guesses")

for i in range(3):
    a = int(input(f"Guess #{i+1}: "))
    if abs(n - a) == 1:
        print("So close")
    elif n == a:
        print("You're right!")
        break
    else:
        print("Far off")
else:
    print("Out of guesses. The correct number was:", n)
