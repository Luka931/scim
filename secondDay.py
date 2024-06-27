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


numbers = [35, 34, 59, 15, 128, 79, 143, 6, 92, 11, 148, 19, 48, 99, 73, 111, 149, 100, 60, 39, 124, 8, 116, 47, 90, 31, 139, 43, 143, 70, 9, 5, 84, 59, 129, 21, 82, 125, 85, 41, 145, 15, 87, 27, 8, 82, 121, 97, 64, 35, 74, 121, 54, 37, 34, 70, 57, 65, 39, 112, 27, 39, 111, 44, 52, 20, 88, 27, 71, 101, 43, 48, 85, 26, 129, 96, 18, 85, 43, 128, 7, 30, 105, 33, 85, 34, 20, 105, 100, 31, 112, 47, 22, 10, 60, 106, 40, 67, 69, 129]
sumNumbers = 0
length = 0
for number in numbers:
    length = length + 1
    sumNumbers = sumNumbers + number

print(sumNumbers)
print(sumNumbers/length)

age = 15
if age >= 18:
    print("You are allowed to drinl beer!")
else:
    print("You need to stay home!")

age = 18
if age >= 18:
    name = "John"
    print(f"You are allowed to drinl beer, {name}!")
else:
    name = "Marry"
    print(f"You need to stay home, {name}!")

age = 2
if age <= 3:
    print("You have to pay 3 euros for the ticket")
elif age <= 16:
    print("You have to pay 10 euros for the ticket")
else:
    print("You have to pay 15 euros for the ticket")

age = 2
if age <= 16:
    print("your ticket is 10 euros")
elif age <= 3:
    print("your ticket is 3 euros")
else:
    print("your ticket is 15 euros")

age = 15 
if age <= 3:
    print("price is 0 euros")
elif age <= 16:
    price = 5
    print(f"price is {price} euros")
elif age <= 65:
    print("price is 10 euros")
else:
    print("price is 8 euros")

age = 15 
if age <= 3:
    print("price is 0 euros")
elif age <= 16:
    price = 5
    print(f"price is {price} euros")
elif age <= 65:
    print("price is 10 euros")
elif age > 65:
    print("price is 8 euros")

score = 64
if score >= 50:
    print("Congratulation you passed")
else:
    print("Sorry you have not made it.")

if score < 50:
    print("F")
elif score < 60:
    print("E")
elif score < 70:
    print("D")
elif score < 80:
    print("C")
elif score < 90:
    print("B")
else:
    print("A")