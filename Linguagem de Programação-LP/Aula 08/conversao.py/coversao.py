import operacoes
valor=float (input("digite um valor numerico:"))

print("\n resultados das conversoes:")
print(f"(valor)metros={operacoes.metros_para_cm(valor)}cm")
print(f"(valor)cm= {operacoes.cm_para_metros(valor)}metros")
print(f"(valor)km={operacoes.km_para_metros(valor)}metros")