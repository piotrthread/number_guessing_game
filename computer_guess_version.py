print("Think about a number in range 1-1000, and i'll guess it in no more than 10 rounds :)")

min = 0
max = 1000
win = False
counter = 1

while not win and counter <=10:
    guess = int((max - min) / 2) + min
    print(f"Guessing: {guess}")
    user_msg = input("ok? more? less? ")
    if user_msg == "ok":
        win = True
        print("One more victory!")
    elif user_msg == "less":
        max = guess
    elif user_msg == "more":
        min = guess
    else:
        print("Hey! You're cheating!")
    counter += 1