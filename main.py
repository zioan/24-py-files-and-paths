
file = open("my_file2.txt")
content = file.read()
print(content)
file.close()

# OR

with open("my_file2.txt") as file:
    content = file.read()
    print(content)

# absolute path to read a file from desktop
with open("C:/Users/raw/Desktop/my_file.txt") as file:
    content = file.read()
    print(content)

# relative path to read a file from desktop
# with open("../../Desktop/my_file.txt") as file:
#     content = file.read()
#     print(content)


# with open("my_file.txt", 'a') as file:
#     file.write("Another text here.")

# with open("my_file.txt", 'a') as file:
#     file.write("\nAnother line of text here.")
