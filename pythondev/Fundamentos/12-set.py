# O SET: So tem o valor. e utiliza o par de chaves {}
musicaLista = {"Vou te levar", "nega jurema", "aonde quer que vá", "sonifera  ilha", "vencedor"}

print(type(musicaLista))

# 1 - Buscar o tamanho do set
print(len(musicaLista))

# 2 - True e 1 são considerados o mesmo valor
exemploSet = {"vencedor", True, 1, 8.8}
print(exemploSet)

# 3 - Adicionar item de outro set
musicaLista.update(exemploSet)
print(musicaLista)

# 4 - Remover um item no set
musicaLista.remove(True)
musicaLista.remove(8.8)
print(musicaLista)



