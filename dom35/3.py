var=int(input("Введите число: "))
x=0
while x <= var:
    if x % 2 == 0:
        print(x, "Number is EVEN")
        x=x+1
    else:
        print(x, "Number is ODD")
        x=x+1