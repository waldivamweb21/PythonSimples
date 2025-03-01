# A Tupla: So tem o valor. e utiliza o par de parenteses ().

#tupla: não ordena os itens...
musicaLista = ("Vou te levar", "nega jurema", "aonde quer que vá", "sonifera  ilha", "vencedor")


# I - Buscar os dois primeiros itens da lista
print(musicaLista[:2])

# II - Buscar ultimo item da lista
print(musicaLista[-1])

# III - Buscar musica até uma determinada posição
print(musicaLista[:3])

# IV - Buscar musica de uma posição em diante
print(musicaLista[2:])

# 2 - Recuperar um item da Tupla pelo nome
print(musicaLista.index("vencedor"))