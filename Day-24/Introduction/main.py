# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

# mode= "r" --> read only.
#       "w" --> write.
#       "a" --> append.

with open("new_file.txt", mode="w") as file:
    file.write("\nAlso My nickname is Bajrangi.")
