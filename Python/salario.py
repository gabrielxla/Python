salario = float(input("Digite seu salario "))

if salario <= 280:
    aumento=salario*0.20
    salariodefinitivo=aumento+salario
    print("O valor porcentual aumentado foi de 20%")
elif salario > 280 and salario < 700:
    aumento=salario *0.15
    salariodefinitivo=aumento+salario
    print("O valor porcentual aumentado foi de 15%")
elif salario > 700 and salario < 1500:
    aumento=salario*0.10
    salariodefinitivo=aumento+salario
    print("O valor porcentual aumentado foi de 10%")
elif salario >= 1500:
    aumento=salario*0.05
    salariodefinitivo=aumento+salario
    print("O valor porcentual aumentado foi de 5%")


print(f"O salario antes era {salario}")
print(f"O valor de aumento foi de {aumento}")
print(f"O valor reajustado foi de {salariodefinitivo}")
