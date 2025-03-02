# condicao em python.

nome  = input("Digite o nome da banda:\n")
musica  = input("Digite o nome da musica:\n")
anoDeLancamento = int(input("Digite o ano de lancamento:\n"))
nota = float(input("Digite a nota de avaliacao da banda e a musica:\n"))

#Verifica se a banda e a musica são recomendados

if nota > 8.0 and anoDeLancamento > 2015:
    print(f'A banda: {nome} e a musica: {musica}, são muito boas recomendo ouvi-las.')
else:
    print(f'A banda: {nome} e a musica: {musica}, ainda não atingiram boas notas.')    
    