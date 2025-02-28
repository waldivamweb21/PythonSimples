#Lista de Musicas

'''
musicaLista = ["Vou te levar", "nega jurema", "aonde quer que vá", "sonifera  ilha", "vencedor"]

# 1 - Iterando valores de uma lista
for musica in musicaLista:
    print(musica)
  
print("====================================================")  

# Encerrar a laço de repetição quando chegar em determinada musica.

for musica in musicaLista:
    if musica == "sonifera ilha":
        break
    print(musica)
    
 
print("====================================================")  
    
 # 3 - Qnd a cond for atd, o loop vai para prox iteracao.
 
for musica in musicaLista:
   if musica == "sonifera ilha":
       continue
   print(musica)     
   
 
print("====================================================")  

'''
# 4 - Avaliacao dos CDs.

nomeDasBandas = ["Cbjr", "Raimundos", "Paralamas", "Titas", "Los hermanos"]

nomeDasBandas = input("Digite o nome da banda:\n")
NotaParaBanda = int(input("Digite quantas notas voce quer avaliar para a banda:\n"))

total = 0
for i in range(NotaParaBanda):
    nota = float(input("Digite a nota para a banda: \n"))
    total += nota

if NotaParaBanda > 0:
    avaliacao = total/NotaParaBanda
else:
    avaliacao = 0
    
print(f"A média de avaliação da banda {nomeDasBandas} é: {avaliacao:.2f}")           

     
    