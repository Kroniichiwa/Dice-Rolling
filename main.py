import random

def roll_dice(num_dice, num_sides):
    #Roll num_dice dice with num_sides sides each and return the total score
    return sum(random.randint(1, num_sides) for _ in range(num_dice))

def main():
    while True  :

        try :
            num_dice = int(input("How many dice? : "))
            num_sides = int(input("How many sides? : "))

            if num_dice <= 0 or num_sides <= 0:
                print("Please enter positive values for the number of dice and sides")
                continue

            #each sides always start from 1 ... num_sides

            else :
                score = roll_dice(num_dice, num_sides)
                print("You scored", score)

            play_again = input("Do you want to play again? (Y/N)").upper()
            if play_again == "N":
                print("Good bye!")
                break

        except ValueError:
            print("Please only type number!")


if __name__ == '__main__':
    main()