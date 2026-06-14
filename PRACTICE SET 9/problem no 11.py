# Write a python program to rename a file to “renamed_by_python.txt”.

with open("PRACTICE SET 9/old.txt", "r") as f:
    content = f.read()

with open("PRACTICE SET 9/rename_by_python.txt", "w") as f:
    f.write(content)