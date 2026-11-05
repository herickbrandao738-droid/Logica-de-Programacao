#4.	A concessionária de veículos “CARANGO” está vendendo os seus veículos com desconto. 
# Faça um algoritmo que calcule e exiba o valor do desconto e o valor a ser pago pelo cliente. 
# O desconto deverá ser calculado sobre o valor do veículo de acordo com o combustível 
# (álcool – 25%, gasolina – 21% ou diesel –14%). 

valorCarro = float(input("Digite o valor do carro: "))
combustivel = str(input("Digite o tipo de combustivel: "))

if combustivel == "alcool":
    valorDescontoCarro = valorCarro - (valorCarro*0.25)
elif combustivel == "gasolina":
    valorDescontoCarro = valorCarro - (valorCarro*0.21)
else:
    valorDescontoCarro = valorCarro - (valorCarro*0.14)

valorDesconto = valorCarro - valorDescontoCarro

print ("O valor do desconto é " , valorDesconto)
print ("O valor do carro com o desconto aplicado é " , valorDescontoCarro)