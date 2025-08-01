import random

"""
<rule>
Please input your choice.
[Rock:     1]
[Scissors: 2]
[Paper:    3]

<result>
win:  {}
lose: {}
draw: {}
"""



def game():
    lst = ["ROCK", "SCISSORS", "PAPER"]
    print("<rule>")
    print("Please input your choice.")
    print("[Rock:     1]")
    print("[Scissors: 2]")
    print("[Paper:    3]")
    your = input("Your number:  ")
    npc = random.randint(1, 3)

    if not your.isdigit():
        print("Please input your choice as a number.")
        return "lose"
    else:
        your = int(your)
        if your < 1 or your > 3:
            print("Please input a number between 1 and 3.")
            return "lose"
        else:
            print(f"Your choice:  {lst[your - 1]}")
            print(f"NPC's choice: {lst[npc - 1]}")

            if your == npc:
                print("You and NPC draw!\n")
                return "draw"
            elif (your == 1 and npc == 2) or (your == 2 and npc == 3) or (your == 3 and npc == 1):
                print("You win!\n")
                return "win"
            else:
                print("You lose!\n")
                return "lose"

def main():
    win, lose, draw = 0, 0, 0

    for i in range(10):
        print(f"Round {i + 1}")
        result = game()
        if result == "win":
            win += 1
        elif result == "lose":
            lose += 1
        elif result == "draw":
            draw += 1

    print(f"<result>")
    print(f"win:  {win}")
    print(f"lose: {lose}")
    print(f"draw: {draw}")

main()
