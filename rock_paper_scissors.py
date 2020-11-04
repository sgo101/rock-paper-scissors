import random

shapes = ["Rock", "Paper", "Scissors"]


# hand of the computer radomly choosen by the computer
computer = random.choice(shapes)
print("computer hand is", computer)

# player must choose one of the shpaes
for i, shape in enumerate(shapes, 1):
    print(f"{i}. {shape}")

player = input("Enter [1, 2 or 3]\n> ")

print("player hand", player)
