print("FOR CONSENT INQUIRY")
a = int(input("enter your age: "))
# IF ELSE  if ELIF LADDER
if(a>=18):
    print("you are above the age of consent")
    print("good for you")
elif(a<0):
     print("you are entering the invaild age")

elif(a==0):
     print("you are entering the zero which is  invaild age")
else:
     print("you are below the age of consent")

print("END OF THE INQUIRY")