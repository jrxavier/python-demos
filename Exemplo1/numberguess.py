__author__ = 'zerix'

#Exemplo de numeros randomicos

import random

def main():
    smaller = int(input("Enter a small number: "))
    larger = int(input("Enter a gig number: "))

    myNumber = random.randint(smaller, larger)

    count = 0
    while True:
        count+=1
        userNumber = int (input("Enter you guess: "))
        if userNumber < myNumber:
            print("Too small")
        elif userNumber > myNumber:
            print("Too bigg")
        else:
            print("You've got it in ", count, " tries")
            break


if __name__ == "__main__":
    main()


