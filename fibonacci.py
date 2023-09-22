n = 10
num1 = 0
num2 = 1
nxn = num2
count = 1

while count <= n:
    print(nxn,end=" ")
    count += 1 
    num1, num2 = num2, nxn
    nxn = num1 + num2
    print()