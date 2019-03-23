from random import randint

win = False

number = randint(1,100)

while not win:
    your_shot = input("Podaj liczbę: ")
    try:
        your_shot = int(your_shot)
        if your_shot == number:
            win = True
            print("Brawo! Zgadłeś!")
        elif your_shot > number:
            print("Troszke mniej :)")
        elif your_shot < number:
            print("Ciutkę więcej :)")
    except ValueError:
        print("To nie jest liczba!")

