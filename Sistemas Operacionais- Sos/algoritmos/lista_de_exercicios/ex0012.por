programa {
  funcao inicio() {
   real preco, desconto, promo

   //entrada
   escreva("digite o preco do  produto:")
   leia(preco) 

   //conta
   desconto=(preco*0.05)
   promo=preco - desconto
   //saida
   escreva("o preco promocional do produto é :",promo)
  }
}
