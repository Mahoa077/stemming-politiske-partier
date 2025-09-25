with open("my_file.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line")

with open("my_file.txt", "a") as file:
    file.write("\nThis line is appended.")