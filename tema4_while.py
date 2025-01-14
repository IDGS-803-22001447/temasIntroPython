x=0;
while x<=10:
    print(x)
    x=x+1
    


print("Dame un número para su tabla:")
num1 = input("Numero: ")
x = 0
while x <= 10:
    res = int(num1) * x
    print(" {} x {} = {}".format(num1, x, res))
    x += 1

