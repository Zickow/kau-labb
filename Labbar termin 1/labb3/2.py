count = 0

while True:
    ch = input("enter a character ( or ? to stop): ")

    if ch == "?":
        break
    if ch.isupper():
        count = count + 1

        print("Number of capital letters:", count)