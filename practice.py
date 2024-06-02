a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = int(input("Enter d: "))

if a > b:
    if a > c:
        if a > d:
            print("a is leargest")
        else:
            print("d is leargest")
    else:
        if c > d:
            print("c is leargest")
        else:
            print("d is leargest")
else:
    if b > c:
        if b > d:
            print("b is leargest")
        else:
            print("d is leargest")
    else:
        if c > d:
            print("c is leargest")
        else:
            print("d is leargest")