l1 = float(input("qual a medida do primeiro lado do triângulo"))
l2 = float(input("qual a medida do segundo lado do triângulo"))
l3 = float(input("qual a medida do derceiro lado do triângulo"))
if l1 == l2 and l2 == l3 and l1 == l3:
    print ("o triângulo é equilatero")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print ("o triângulo é isóceles")
else:
    print ("o triãngulo é escaleno")