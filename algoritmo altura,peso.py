alt = float(input(f"digite sua altura:"))
sex = str (input(f"digite seu sexo:"))
masculino = (f"masculino")
feminino = (f"feminino")
if sex == masculino:
    p = (72.7*alt) - 58
    print (f"seu peso ideal para sua altura de {alt} é de {p}")
elif sex == feminino:
    p = (62.1*alt) - 44.7
    print (f"seu peso ideal para sua altura de {alt} é de {p}")
else:
    print (f"inválido vagabundo")