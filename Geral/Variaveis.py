num1 = 11
num2 = 15.57
nome = "antonio"
sobrenome = "carlos"
nome_completo = " " +nome+ " " +sobrenome+ " "
teste = True
soma = num1+num2
idade = 41

print(num1)
print(type(num1))
print((num2))
print(type(num2))
print((nome))
print(type(nome))
print((teste))
print(type(teste))
print("Contatenar string = " + nome_completo.title())

print("A soma entre %.2f e %.2f é: %.2f" %(num1, num2, soma))

print("Contatenar str com number = "+"'"+ nome_completo +"'" ", tenho "+ str(idade) + " anos")

# Eliminar os espaços
print("Remover espaço = "+nome_completo.strip())