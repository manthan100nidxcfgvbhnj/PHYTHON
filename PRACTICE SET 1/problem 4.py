import os
# select the directory whose content you want to list
path = "."

# use the os module to the directory content
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)