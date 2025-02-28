
musicaLista = ["Vou te levar", "nega jurema", "aonde quer que vá", "sonifera  ilha", "vencedor"]


# 1 - Tamanho da lista
print(len(musicaLista))

# 2 - Recuperar um item da lista pelo nome
print(musicaLista.index("vencedor"))

# 3 - Adicionar um item no  final da lista 
musicaLista.append("pescador de ilusoes")
print(musicaLista)

# 4 - Ordenar a lista
musicaLista.sort()
print(musicaLista)

# 5 - Copiar os itens de uma lista para outra
musicaCopy = musicaLista.copy()
musicaCopy.remove("pescador de ilusoes")
print(musicaCopy)

# 6 - Remove todos os itens da lista
musicaLista.clear()
print(musicaLista)