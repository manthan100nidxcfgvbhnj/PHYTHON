# f = open("CHAPTER 9/file.txt")

# print(f.read())
# f.close()

# THE SAME CAN BE WRITTEN USING WITH LIKE THESE:

with open("CHAPTER 9/file.txt") as f:
    print(f.read())


#you dont have to explicitly close the file