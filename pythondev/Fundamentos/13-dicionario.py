# O dicionario trabalha com a propriedade Chave, Valor.

musicaLista = {
    "musica" : "Vou te levar", 
     "Ano de Lançamento ": "1999", 
    "nota da musica" : 9.0, 
    "Genero" : ["rock", "pop", "blues", "jazz", "house"], 
    
}

print(musicaLista)
print(len(musicaLista))
print(type(musicaLista))

# 1 - Recuperar um elemento do dicionário
print(musicaLista["Genero"])
print(musicaLista.get("nota da musica"))

# 2- Buscar apenas as chaves do dicionario
print(musicaLista.keys())

# 3 - Buscar apenas valores do dicionario
print(musicaLista.values())

# 4 - Buscar itens do dicionario com chave e valor
print(musicaLista.items())

# 5 - adicionar itens no dicionario
musicaLista["produtor"] = "Rick Bonadio"
print(musicaLista)

# 6 - atualizar itens no dicionario
musicaLista.update({"nota da musica" : 10.0})
print(musicaLista)

# 7 - Remover item no dicionario
musicaLista.pop("produtor")
print(musicaLista)

