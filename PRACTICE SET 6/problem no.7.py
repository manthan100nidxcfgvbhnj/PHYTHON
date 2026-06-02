# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("enter your post: ")

if("Harry" in post.lower()):
    print("this post is talking about harry")
else:
    print("this post is not talking about harry")
