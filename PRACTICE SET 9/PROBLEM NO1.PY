# 1. Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

f = open("PRACTICE SET 9\poem.txt")
content = f.read()
if("twinkle " in content):
    print("the word is presennt is the content")
else:
     print("the word is NOT presennt is the content")
f.close()