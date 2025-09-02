import operacoes
print("== quadrada==")
print("1 somar")
print("2 subtrair")
print("3 multiplicar")
print("4 dividir")
opcao= int (input("escolha a operacao"))
a= float(input("digite o primeiro numero:"))
b= float(input ("digite o segundo numero:")) 
if opcao == 1:
     print (" resultado:",operacoes.soma (a,b))
elif opcao == 2 :
     print ("resultado:",operacoes.sub (a,b))
elif opcao == 3 :
     print ("resultado:",operacoes.multiplicacao (a,b))
elif opcao == 4 :
     print ("resultado:",operacoes.dividir (a,b))
else:
     print ("opcao invalida")

