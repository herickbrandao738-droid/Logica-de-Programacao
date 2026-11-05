#15.	Verificar se o número é divisível por 3 ou 5
#Solicite um número e imprima "Sim" se ele for divisível por 3 ou por 5, e "Não" caso contrário.

num = int(input("Digite um número: "))

if num % 3 == 0 and num % 5 == 0:
    print ("Sim")
else: 
    print ("Não")