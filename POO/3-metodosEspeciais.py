# Metodo Principal - com o self consegue recuperar qualquer atributos da classe.
#Construtor.

class Game:
    def __init__(self, nome="", anoLancamento=0, multiplayer=False, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota

    def __str__(self): 
        return f"Game: {self.nome}"

# Criando um jogo
game1 = Game("street fights", 2017, True, 9.5)
print(game1)

print("### Dados do Game ####")
print(f'Nome do jogo: {game1.nome}')
print(f'Ano de Lançamento: {game1.anoLancamento}')
print(f'Multiplayer: {"Sim" if game1.multiplayer else "Não"}')
print(f'Nota: {game1.nota}')


# print(f'\nNome do jogo: {game2.nome}\nAno de Lançamento: {game2.anoLancamento}')
# print(f'\nNome do jogo: {game3.nome}\nAno de Lançamento: {game3.anoLancamento}')
# print(f'\nNome do jogo: {game4.nome}\nAno de Lançamento: {game4.anoLancamento}')

