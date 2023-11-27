print("Welcome to BMI calculator")


def get_bmi():
    weights_classification = ["underweight", "normal weight", "overweight", "obese", "clinically obese"]
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    bmi = round(round(weight, 2) / round(height ** 2, 2), 2)
    if bmi <= 18.5:
        print(f"Your bmi is {bmi}, you are {weights_classification[0]} ")
    elif 18.5 < bmi < 25:
        print(f"Your bmi is {bmi}, you are {weights_classification[1]}")
    elif 25 < bmi < 30:
        print(f"Your bmi is {bmi}, you are {weights_classification[2]}")
    elif 30 < bmi < 35:
        print(f"Your bmi is {bmi}, you are {weights_classification[3]}")
    else:
        print(f"Your bmi is {bmi}, you are {weights_classification[4]}")


get_bmi()


