import random

option = {
    1: "✊",
    2: "✋",
    3: "✌️",
    4: "🦎",
    5: "🖖"
}

combinations = {
    1: [3, 4],
    2: [1, 5],
    3: [2, 4],
    4: [2, 5],
    5: [3, 1]
}

print("1) ✊")
print("2) ✋")
print("3) ✌️")
print("4) 🦎")
print("5) 🖖")

player = int(input("Pick a number: "))
cpu = random.randint(1, 3)

if player not in option:
    print("Invalid number, pick a number between 1 and 5.")
else:
    print(f"CPU chose {option[cpu]}")

    if player == cpu:
        print("Draw!")
    elif cpu in combinations[player]:
        print("YOU WIN!")
    else:
        print("CPU WINS!")