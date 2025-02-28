# Funcao para cadastrar um filme:

def criacao_banda():
    nome = input("Digite o nome da banda:\n")
    anoDelancamento = int(input("Digite o ano de lançamento da banda:\n"))
    precoBanda = float(input("Digite o preço da banda:\n"))
    

    print(f"{nome} ({anoDelancamento}) - R$ {precoBanda:.3f}")
    
criacao_banda()