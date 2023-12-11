# TODO: Calculate the number of coins needed to give change
def main():
    coins = 0
    money = get_money()
    # TODO: convert money to cents
    coin = [25, 10, 5, 1]
    cents = money * 100
    for i in coin:
        while cents >= i:
            cents -= i
            coins += 1
    print(coins)


# TODO: this def do a input validation
def get_money():
    money = 0
    while True:
        try:
            money = float(input("Change owed: "))
            if money > 0:
                return money
            else:
                print("Invalid")
        except ValueError:
            print("Invalid")


main()