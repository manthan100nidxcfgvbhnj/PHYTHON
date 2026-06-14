# Write a program to find out whether a file is identical and matches the content of another file.

with open("PRACTICE SET 9/this.txt") as f:
    content1 = f.read()

with open("PRACTICE SET 9/poem.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("content are same in the list")
else:
    print("this is not same")