# Write a program to mine a log file and find out whether it contains ‘python’.

with open("PRACTICE SET 9/log.txt") as f:
    content = f.read()

if("pyhton" in content):
    print("yes python is present")
else:
    print("python is not present")