programa {
  funcao inicio() {
   real largura, altura, area, litros,metros  

   //entrada
   escreva("qual a altura da parede?")
   leia (largura)

   escreva("qual a largura da parede?")
   leia (altura)

   //contas

   area=altura*largura 
   litros=area/2

   //saida

   escreva("para pintar uma area de",area,"metros será necessario",litros,"de tinta")
  }
}
