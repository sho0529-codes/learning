import random

def game(num):
    count = 0
    while True:
        count += 1
        for i in range(num):
            x = random.randint(1, 2)
            if x == 1:
                continue
            else:
                break
        if i == num - 1:
            return count
        else:
            continue

def main():
    num = 10
    result = game(num)
    print(f"Trying count: {result}")
    print(f"Score: {1 - result / (2 ** num):.4f}")

main()