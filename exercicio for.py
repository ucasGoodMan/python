media = 0.0
nota = 0.0
for i in range(0,3):
    nota = float(input("digite a nota="))
    media = media+nota
media = media/3
print (f"a média é {media}")
if media == 10:
    print(f"aprovado com nota maxima nerdola!!!")
if media < 7:
    print(f"reprovado otario hahah")
else:
    print(f"aprovado mais o menos macaco")