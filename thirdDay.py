result = []
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        result.append("FizzBuzz")
    elif i%3 ==0 :
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    else:
        result.append(i)

print(result)

number = 5
for i in range(3):
    guess = int(input("What is your guess? "))
    if guess == number:
        print("VICTORY")
    elif guess > number:
        print("HIGH")
    else:
        print("LOW") 