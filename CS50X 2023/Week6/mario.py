def get_height():
    while True:
        n = int(input("Height: "))
        if n > 0:
            return n


n = get_height()

for i in range(n):
    for j in range(n):
        print("# ", end="")
    print()


