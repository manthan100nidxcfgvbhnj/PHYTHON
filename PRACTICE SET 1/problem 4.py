# Write a python program to print the contents of a directory using the os module. Search online for the function which does that.
# 5. Label the program written in problem 4 with comments.
import os
# select the directory whose content you want to list
path = "."

# use the os module to the directory content
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)