num1 = int(input("Digite o primeiro nome:\n"))
num2 = int(input("Digite o segundo nome:\n"))

# Operadores Arimeticos
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
mode = num1 %  num2
expoente = num1 ** num2 

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)

print(f"Potencia do numero {num1} por {num2} é: {expoente}")
print(f"O resto da divisao de {num1} por {num2} é: {mode}")

# Comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
different = num1 != num2 
bigger_equal = num1 >= num2 
smaller_equal = num1 <= num2 


print(f"Os numeros {num1} por {num2} são iguais?  {equal}")
print(f"O numero {num1} é maior ou igual a {num2}? são iguais: {bigger_equal}")

#Operadores de Atribuições

num1 += 1 #num1 = num1 + 1
num1 -= 1#num1 = num1 - 1
num1 *= 1#num1 = num1 * 1
num1 /= 1#num1 = num1 / 1
 