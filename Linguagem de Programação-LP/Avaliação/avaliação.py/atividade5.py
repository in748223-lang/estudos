try:
    A = int (input("numerador:"))
    B = int (input("denominador:"))
    D = A/B

except ZeroDivisionError:
  print ("Nao é possivel dividir por zero:")

except ValueError:
  print("voce digitou um valor invalido")
else:
  print(f"O resultado e :{D}")

finally:
 print("seu programa foi execultado")