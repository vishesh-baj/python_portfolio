print("Welcome to ticket counter of roller coaster")

# check the height
height = int(input("Enter your height: "))
if height >= 120:
    print("You have minimum height to ride the roller coaster")
    age = int(input("Enter your age: "))
    # check the age
    if age >= 18:
        print("You are charged 18$ for the ticket")
    else:
        print("You are charged 7$ for the ticket")

else:
    print("You  dont have minimum height to enter the roller coaster, grow your height")
