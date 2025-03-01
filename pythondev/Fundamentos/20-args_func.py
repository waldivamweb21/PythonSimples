# Paramentos são valores adicionado dentro dos parenteses.

# 1 - Função para imprimir um nome completo

def nome_completo(primeiro_nome, sobre_nome):
    print(f"Nome é: {primeiro_nome}  sobrenome: {sobre_nome}")
    
nome_completo("Wal", "silva")
nome_completo("sonia", "alburqueque")

# 2 funcao para somar dois numeros.    

def somar_numeros(a, b):
    return a + b
print(f"A Soma é:  {somar_numeros(10, 50)}")

# 3 funcao com parametros padrao.  
#obs: Não precisa passar o valor no retorno da funcao,
# pois já está passando o valor padrao no parametro. 

def endereco(cidade="Gravatá"):
    print(f"eu moro em: {cidade}")

endereco() 
endereco("Recife")

# 4 - funcao para avaliar a banda

def nota_banda(num_nota, nome_banda):
    total = 0
    for i in range(num_nota):
        nota = float(input("Digite a nota para banda:\n"))
        total = nota + nota
    
    if num_nota > 0:
        avaliacao = total / num_nota
    else:
        avaliacao = 0
    
    print(f"A Média da avaliação da banda: {nome_banda} é: {avaliacao:.2f}")

nota_banda(2, "cbjr")    

