valorTotal = int(input("Escreva o valor total da compra: "))
valorComDesconto = valorTotal*0.9
print ("O valor final da compra a vista é: " , valorComDesconto)
valorCincoVezes = valorTotal/5
print ("O valor da compra parcelado em 5 vezes é " , valorCincoVezes , " por parcela")
valorDezVezes = (valorTotal+(valorTotal * 0.2))
valorParcelaDezVezes = valorDezVezes/10
print ("O valor da compra parcelado em 10 vezes com juros é " , valorParcelaDezVezes , " por parcela")