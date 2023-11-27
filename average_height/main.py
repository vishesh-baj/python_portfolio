print("Welcome to average height script")

students_heights_string = input("Enter Students height separated by a space")
students_height_list_as_strings = students_heights_string.split(" ")
length_of_students_list = len(students_height_list_as_strings)
total_heights = 0

for height in students_height_list_as_strings:
    total_heights += int(height)

height_average = total_heights/length_of_students_list
print(f"{height_average} is the average height among all student heights")


