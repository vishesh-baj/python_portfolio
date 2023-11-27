print("Welcome to tip calculator.")


def individual_bill_amount():
    total_bill = float(input("What was the total bill? $"))
    total_people = int(input("How many people to split the bill? "))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

    bill_with_tip = round(((tip_percentage / total_bill) * 100) + total_bill, 2)
    individual_tip = round(bill_with_tip/total_people, 2)
    print(f"{individual_tip} amount per person for total bill of {bill_with_tip}")


individual_bill_amount()



