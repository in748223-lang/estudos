programa {
  funcao inicio() {
    real km_percorridos
    inteiro dias 
    real valor_km, valor_dias, total

    escreva("digite os km percorridos:")
    leia(km_percorridos)

    escreva("digite os dias percorridos:")
    leia (dias)

    valor_dias = dias * 90
    valor_km =  km_percorridos*0.20
    total = valor_dias + valor_km

    escreva("o preco total a pagar e :",total)




  }
}
