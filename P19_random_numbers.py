import random

def main():
    x =random.randint(1,3)
    print(x)
    y = random.random()
    print(y)
    my_list = ["paper", "scissor", "rock"]
    random_choice = random.choice(my_list)
    print(random_choice)
    cards = ["A", "B", "C", 1,2,3,4,5]
    print("before", cards)
    random.shuffle(cards)
    print("after",cards)

if __name__ == '__main__':
    main()