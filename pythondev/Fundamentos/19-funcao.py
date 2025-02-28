''' 
# Funcao: São reaproveitamento de codigos
para utilizar em outra parte do seu projeto.
'''

# 1 - Função para imprimir uma mensagem

def BemVindo():
    print("Seja bem vindo ao sistema de Musicas!")

#for i in range(10):    
 #   BemVindo()

# 2 - Uma funcao para calcular a média de notas:

def calculo_avaliacoes():
    num_notas = int(input("Digite quantas avaliacoes deseja fazer para a banda:\n"))
    total = 0
    for i in range(num_notas):
        nota = float(input("Digite a nota para banda:\n"))
        total += nota
    if num_notas  > 0:
        avaliacao = total / num_notas
    else:
         avaliacao = 0
    
    return avaliacao    

print(f"A média de avaliação é: {calculo_avaliacoes():.2f}")
      
      
      