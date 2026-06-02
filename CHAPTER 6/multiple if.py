print("FOR CONSENT INQUIRY")
a = int(input("enter your age: "))

if(a%2==0):
#     statement no 1
     print("a is even")
if(a>=18):
    # statement no 2
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
     print("you are entering the invaild age")
elif(a==0):
     print("you are entering the zero which is  invaild age")
else:
     print("you are below the age of consent")

print("END OF THE INQUIRY")