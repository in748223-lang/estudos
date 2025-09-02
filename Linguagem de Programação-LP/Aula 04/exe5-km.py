# entrada de dados 
km= float(input("digite a quantidade de km percorridos:"))
dias= int(input("digite a quantidade de dias de aluguel:"))
#calculo
preco=(dias *60)+(km*0.15)
#saida
print(f"o valor a pagar e R${preco:2f}")

#atividade 2
l= [5,7,2,9,4,1,3]
# a) tamanho da lista
print("tamanho da lista:",len(l))
# b) maior da lista
print("maior valor da lista:",max(l))
# c) menor valor da lista
print("menor numero da lista:",min (l)) 
# d) soma de todos os elementos
print("soma de todos os numeros da lista:",sum (l))
# e) lista em ordem crescente
print("lista em ordem crescente:",sorted (l))
# f)lista em ordem decrescente
print("lista em ordem decrescente:",sorted (l))


