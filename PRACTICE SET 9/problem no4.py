#  A file contains a word “Donkey” multiple times. You need to write a program which replaces this word with ##### by updating the same file.


word = "donkey"

with open("PRACTICE SET 9/donkfile.txt", "r") as f:
    content = f.read()

contentNew = content.replace("donkey", "#####") 

with open("PRACTICE SET 9/donkfile.txt", "w") as f:
    f.write(contentNew)