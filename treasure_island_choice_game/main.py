print("Welcome to treasure island game, where your choices decide your fate")
print("Welcome!, Your mission is to find the treasure, where do you wanna go? 'left' or 'right' ")
first_decision = input("").lower()
if first_decision == "right" or first_decision != "left":
    print("Fall into a hole, Game over")
else:
    print("Swim or Wait?")
    second_decision = input("").lower()
    if second_decision == "swim" or second_decision != "wait":
        print("Attacked by trout, Game Over")
    else:
        print("Which Door? Red, Blue or Yellow:  ")
        third_decision = input("").lower()
        if third_decision == "red":
            print("Burnt By Fire, Game Over")
        elif third_decision == "blue":
            print("Eaten By Beasts, Game Over")
        elif third_decision == "yellow":
            print("You Found the chest, You Win!")
        else:
            print("INVALID ENTRY, GAME OVER")


