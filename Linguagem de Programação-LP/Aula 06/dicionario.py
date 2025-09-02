pessoa= {
    "nome":"ingrid",
    "idade": "17",
    "peso": "47"
    
}
print(pessoa)
print(pessoa.keys()),
print(pessoa.values())

pessoa["altura"]= 1,56
print(pessoa)

pessoa["peso"] = 47
print(pessoa)

del pessoa ["idade"]
print(pessoa)

print ("idade" in pessoa)
print("nome" in pessoa)