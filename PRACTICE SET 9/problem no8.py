# Write a program to make a copy of a text file “this.txt”.

with open("PRACTICE SET 9/this.txt") as f:
    content = f.read()

with open("PRACTICE SET 9/this_copy.txt", "w") as f:
    f.write(content)