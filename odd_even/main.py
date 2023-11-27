user_entered_number = int(input("Enter a number: "))


def check_odd_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


if check_odd_even(user_entered_number):
    print("Number is even")
else:
    print("Number is odd")

