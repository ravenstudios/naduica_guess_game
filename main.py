import random

rand_num = random.randint(1, 101)
# print(rand_num)
running = True
score = 0


def check_guess(num):
    global running, rand_num, score

    if num > rand_num:
        print("Too high")
        score += 1

    if num < rand_num:
        print("Too low")
        score += 1

    if num == rand_num:
        print(f"Guessed right, it took {score} guesses")
        running = False


while running == True:
    guess = 0
    try:
        guess = int(input("Enter a number from 1-100\n"))
    except Exception as e:
        print("Must enter a number between 1 and 100 not any letters")

    if 0 < guess < 101:
        check_guess(guess)
    else:
        print("Must enter a number between 1 and 100 not any letters")



print("asdfjasdjsdf")
