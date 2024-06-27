from random import randint

numberOfPeople = 20

birthdays = []
for i in range(numberOfPeople):
    birthdays.append(randint(1,365))

doTwoPeopleHaveSameBirthdays = False
for birthday in birthdays:
    if birthdays.count(birthday) > 1:
        doTwoPeopleHaveSameBirthdays = True

if doTwoPeopleHaveSameBirthdays:
    print("Two Persons have same birthday!")
else:
    print("Everyone is born on different date")
