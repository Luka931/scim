from random import randint

statistics = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
numberOfThrows = 1000000 

for i in range(numberOfThrows):
    dieOne = randint(1,6)
    dieTwo = randint(1,6)
    statistics[dieOne + dieTwo - 1] = statistics[dieOne + dieTwo - 1] + 1

percentages = []
for i in statistics:
    percentages.append(i/numberOfThrows*100)

print(percentages)