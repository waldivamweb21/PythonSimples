num1 = float(input("Digite o primeiro numero:\n "))
num2 = float(input("Digite o segundo numero:\n"))
operacao = input("Digite a operacao a ser realizada: (+ - * /)\n")

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2   

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2          
    else:
        print("Erro: divisao por zero")
        resultado = 0
else:
    print("Opereracao inválida")
    resulto = 0

print(f'Resultado da operacao é: {resultado:.2f}')


