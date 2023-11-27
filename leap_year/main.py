print("Welcome to leap year checker")


def check_leap_year():
    year = int(input("Enter a year to check if its a leap year: "))
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f"{year} is a leap year")
            else:
                print(f"{year} is not a leap year")
        else:
            print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year.")


check_leap_year()
