programa {
  funcao inicio() {
    
  //area das variaveis.:  ==   tipo VARIAVEIS 
  real  numero, antercessor, sucessor 


    // area da entrada == TODA INGORMAÇÃO QUE PRECISA SER LIDA 'LEIA(VARIAVEL)'
  escreva("digite um numero")
  leia(numero)
    
    // AREA DE PROCESSAMENTO == TODAS AS CONTAS
    antercessor= numero -1
    sucessor = numero + 1

 


    // AREA DA SAIDA == SÓ ESCREVA - NUNCA USO LEIA
    escreva("O antercessor de ", numero , "e" , sucessor , "\n")
    escreva("O sucessor de ", numero , "e" , antercessor ,"\n")

   
  }
}
