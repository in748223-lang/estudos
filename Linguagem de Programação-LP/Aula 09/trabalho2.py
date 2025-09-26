n = input("qual seu nome?") 
i = input("qual a sua idade?")
with open("dados.txt","w") as arquivo:
    arquivo.write(n)
    arquivo.write(f"\n{i}")
