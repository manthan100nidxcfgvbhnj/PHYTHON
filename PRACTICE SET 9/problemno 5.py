# Repeat program 4 for a list of such words to be censored.

words = ["donkey", "bad", "gande"]

with open("PRACTICE SET 9/donkfile.txt", "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word, "#" * len(word)) 

with open("PRACTICE SET 9/donkfile.txt", "w") as f:
    f.write(content)
