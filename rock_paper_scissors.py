import random


def who_win(player, computer):
    if player == computer:
        return "TIE, Playe Again."
    elif player == "Rock" and computer == "Paper":
        return "Computer Win!!"
    elif player == "Paper" and computer == "Scissors":
        return "Computer Win!!"
    elif player == "Scissors" and computer == "Rock":
        return "Computer Win!!"
    else:
        return "You win!!!!!!!!!:-0"  # I am not sure this logic is right!!


def play():
    shapes = {"1": "Rock", "2": "Paper", "3": "Scissors"}

    # hand of the computer radomly choosen by the computer
    computer_hand = random.choice(list(shapes.values()))
    print(computer_hand.upper())

    # player must choose one of the shpaes
    for number, shape in shapes.items():
        print(f"{number}. {shape}")

    player_choice = input("Enter [1, 2 or 3]\n> ")
    player_hand = shapes.get(player_choice)

    print("Computer hand is", computer_hand)
    print("Player hand is", player_hand)

    print(f"{computer_hand} VS {player_hand}")

    # decide how win
    result = who_win(player_hand, computer_hand)
    print(result)


if __name__ == "__main__":
    play()