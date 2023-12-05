print("00", end=", ")
for i in range(1, 100):
    print("{:02d}".format(i), end="")
    if i == 99:
        print()
    else:
        print(", ", end="")