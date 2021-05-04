# PART 1
# name = input("What is your name?")
# print(f"How is it going {name}?")

#PART 2
# name = input("What is your name?")
# if name == "Kris":
#     print("Hey, thats's my name too!")
# else: 
#     print(f"Your name is: {name}")

#PART 3
names_given = []
for name_num in range(10):
    name = input("What is your name?")
    names_given.append(name)
print("It was nice to meet all of you")
print("Names are:")

for names in names_given:
    print("- " + names)
