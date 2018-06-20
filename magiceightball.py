#ans1 = "You're a coding rockstar!"
#ans2 = "You will win Oregon Trail!"
#ans3 = "You'll find a pot of gold."
#ans4 = "You'll drown in Oregon Trail."
ans = raw_input("Would you like to know your fortune? Y or N")
choice = raw_input("Pick a number between 1-4")
if choice == 1:
    print("You're a coding rockstar!")
elif choice == 2:
    print("You will win Oregon Trail!")
elif choice == 3:
    print("You'll find a pot of gold.")
elif choice == 4:
    print("You'll drown in Oregon Trail.")
else:
    print("Please make sure your number is between one and four!")
