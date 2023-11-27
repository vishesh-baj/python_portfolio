print("Welcome to Love Calculator")

name_one = input("Enter first Name: ")
name_two = input("Enter second Name: ")
concatenated_name_string = name_one.lower() + name_two.lower()

print(concatenated_name_string)

t = concatenated_name_string.count("t")
r = concatenated_name_string.count("r")
u = concatenated_name_string.count("u")
e = concatenated_name_string.count("e")

l = concatenated_name_string.count("l")
o = concatenated_name_string.count("o")
v = concatenated_name_string.count("v")

true = t + r + u + e
love = l + o + v + e

total_percentage_love = int(f"{true}{love}")

if total_percentage_love < 10 or total_percentage_love > 90:
    print(f"Your score is {total_percentage_love}, you go like coke and mentos")
elif 40 > total_percentage_love > 50:
    print(f"Your score is {total_percentage_love}, you are alright for each other")
else:
    print(f"Your score is {total_percentage_love}")


