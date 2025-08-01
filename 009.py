import random

"""
<rule>
Roll Two Dice until They Match.
Please push Enter.

<result>
Trying count: {}
"""

def game():
    print("<rule>")
    print("Roll Two Dice until They Match.")
    input("Please push Enter.")

    dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print("")
    
    if dice1 == dice2:
        return True
    else:
        return False

def main():
    count = 0
    while True:
        count += 1
        if game():
            print("success!")
            break
    
    print("<result>")
    print(f"Trying count: {count}")

main()