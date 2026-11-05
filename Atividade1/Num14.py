#14.	Classificação de idade
#Peça para o usuário inserir a idade e classifique como "Criança", "Adolescente", "Adulto" 
# ou "Idoso", de acordo com os seguintes critérios:
#a.	0 a 12 anos: Criança
#b.	13 a 17 anos: Adolescente
#c.	18 a 60 anos: Adulto
#d.	Acima de 60 anos: Idoso

idade = int(input("Digite sua idade: "))
if idade < 13:
    print ("Criança")
elif idade < 18:
    print ("Adolescente")
elif idade < 61:
    print ("Adulto")
else: print ("Idoso")