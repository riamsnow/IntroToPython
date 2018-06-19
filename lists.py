myinfo = ["Angela", "Fred", "Trudy", 3, 4, 5]
for name in myinfo:
    print(name)
 
print("My Shopping List:")    
myshoppinglist = ["hummus", "carrots", "gummy bears", "avocados" ]
for items in myshoppinglist:
    print(items)
myshoppinglist.append("milky way midnights")
print(myshoppinglist)
print(len(myshoppinglist))
colors = ["blue", "red", "green", "purple", "indigo"]
print(colors.index("green"))
colors.insert(2, "yellow")

print(colors)

weather = []
w = raw_input("What is the weather today?")
weather.append(w)
print(weather)


