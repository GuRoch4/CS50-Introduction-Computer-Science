# TODO: input and loop

# TODO: this def do a fpr to print
def main():
    height = get_height()
    for i in range(height):
        print(" " * (height - (i + 1)), end="")
        print("#" * (i + 1))


# TODO: this def do a input validation
def get_height():
    while True:
        try:
            height = int(input("height: "))
            if height > 0 and height < 9:
                return height
            else:
                print("invalid")
        except ValueError:
            print("invalid")


main()