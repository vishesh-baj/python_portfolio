print('Welcome to pizza ordering script')


def get_pizza_amount(size, pepperoni, extra_cheese):
    amount = 0
    if size == "S":
        amount += 15
    if size == "M":
        amount += 20
    if size == "L":
        amount += 25
    if extra_cheese == "Y":
        amount += 1
    if pepperoni == "Y" and size == "M" or size == "L":
        amount += 3
    elif pepperoni == "Y" and size == "S":
        amount += 2
    print(f"Total Price of your pizza is {amount}")


pizza_size = input("Enter pizza size: ")
want_pepperoni = input("Do you want pepperoni?: ")
want_extra_cheese = input("Do you want extra cheese?: ")

get_pizza_amount(pizza_size, want_pepperoni, want_extra_cheese)
