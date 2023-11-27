print("Welcome to treasure map")

row1 = ["()", "()", "()"]
row2 = ["()", "()", "()"]
row3 = ["()", "()", "()"]

map = [row1, row2, row3]

position = input("Where do you want to put the treasure? ")
selected_row = int(position[0])
selected_column = int(position[1])
map[selected_row][selected_column] = "X"
print(f"{row1}\n{row2}\n{row3}")
