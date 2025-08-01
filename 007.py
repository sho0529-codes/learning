import random

"""
<result>
Max count of trying:     {}
Min count of trying:     {}
Average count of trying: {}
"""

def game():
    answer = random.randint(1, 100)
    count = 0

    print("Please input a number between 1 and 100.")
    # print(f"debaug: answer is {answer}")  # デバッグ用の出力
    while True:
        guess = input("guess: ")
        count += 1
        if not guess.isdigit():  # .isdigit()で数字か確認
            print("Please input a number.")
        else:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("Not in range 1-100.")
                continue
            elif guess < answer:
                print("More big.")
            elif guess > answer:
                print("More small.")
            elif guess == answer:
                print("Correct!")
                break
    return count

def main():
    try_count = []

    for i in range(10):
        print(f"Round {i + 1}")

        count = game()
        try_count.append(count)
        print(f"Count of trying: {count}\n")
        

    print(f"Max count of trying:     {max(try_count)}")
    print(f"Min count of trying:     {min(try_count)}")
    print(f"Average count of trying: {sum(try_count) / len(try_count)}")

main()