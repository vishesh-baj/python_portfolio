import  random
print("Welcome to coin toss script")


def toss_a_coin():
    randomized_choice = random.randint(0, 1)
    if randomized_choice == 0:
        print("Its a Heads")
    if randomized_choice == 1:
        print("Its a Tails")


toss_a_coin()

