myfavoriteicecream = raw_input("What is your favorite ice cream?")
if myfavoriteicecream == "Honey Lavender":
    print("That is my favorite too!")
    
elif myfavoriteicecream in["Vanilla", "Blackberry", "Watermelon Sherbert"]:
    print("I like that flavor too!")    
else:
    print("Yuck, you have horrible taste!")
    
myname = raw_input("What is your name?")
myinfo = ["Angela", "Fred", "Trudy" ]
myinfo.append(myname)
for name in myinfo:
    if myname == name:
        print("True")
    else:
        print("False")
x = int(raw_input("Please imput a whole number:"))        