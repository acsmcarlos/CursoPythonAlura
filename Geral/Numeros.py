num1 = 9
num2 = 2

soma = num1 + num2
subt = soma - num2
mult = num1 * num2
div = num1 / num2
expo = num1 ** num2


print("Num1: " + str(num1))
print("Num2: " + str(num2))

print("SOMA:  %i + %i = " % (num1, num2) + str(soma))
print("SUBT: %i - %i = " % (soma, num2) + str(subt))
print("MULT:  %i * %i = " % (num1, num2) + str(mult))
print("DIVI:  %i ÷ %i = " % (num1, num2) + str(div))
print("EXPO:  %i ^ %i = " % (num1, num2) + str(expo))
