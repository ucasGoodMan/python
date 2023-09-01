import math
a = int(input("Qual o valor de a?:"))
b = int(input("Qual o valor de b?:"))
c = int(input("Qual o valor de c?:"))
d = b** - 4*a*c
x1 = (-b + math.sqrt(d))/2*a
x2 = (-b - math.sqrt(d))/2*a
print(f'Os valores possiveis de x são: {x1} e {x2}')