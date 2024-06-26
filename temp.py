age = 19
name = "Nick"

print(f"{name} is {age + 5} years old.")

name = "Bottle"
surname = "Opener"
print("{name} {surname}")

print((1 + 2) * 3 == 9.0)

names = ["Andrija", "Amira", "Verona"]
print(f"{names[0]}, welcome to SCIM")
print(f"{names[1]}, welcome to SCIM")
print(f"{names[2]}, welcome to SCIM")

names[0] = "Luka"
print("New names")
print(f"{names[0]}, welcome to SCIM")
print(f"{names[1]}, welcome to SCIM")
print(f"{names[2]}, welcome to SCIM")

names.insert(1, 100)
print(names)
names.append(True)
print(names)

names.remove("Luka")
print(names)
names.pop(3)
print(names)

names = ["Andrija", "Amira", "Verona"]
names.append("Csenge")
names.remove("Amira")
names.insert(2, "Sara")
names[0] = "Ganta"

print(f"{names[0]}, you are invited to my birthday!")
print(f"{names[1]}, you are invited to my birthday!")
print(f"{names[2]}, you are invited to my birthday!")
print(f"{names[3]}, you are invited to my birthday!")

print("This is done with a fore loop")
print()
for i in names:
    upperCase = i.upper()
    print(f"{upperCase}, you are invited to my birthday!")
    print("----------------------")

for i in names:
    print(f"{i.upper()}, you are invited to my birthday!")
    print("----------------------")
