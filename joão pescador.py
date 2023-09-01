p = int(input("quantos quilos de peixe você pescou?:"))
e = p-50
m = e*4
if e>0:
    print(f"você teve um excesso de {e} quilos e deverá pagar uma multa de R${m},00")
elif e == 0 or e<0:
    print("você não teve excesso de peso")