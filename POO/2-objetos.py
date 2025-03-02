class Game:
    nome = ""
    anoLancamento = 0
    multiplayer = False
    nota = 0
    
# Primeiro jogo

game1 = Game()
game1.nome = "The king of fights"
game1.anoLancamento = 2017
game1.multiplayer = False
game1.nota = 9.5

# OBS:. Só é instanciar e chamar o segundo game.

# Segundo Jogo

game2 = Game()
game2.nome = "The Coutry Strikes"
game2.anoLancamento = 2010
game2.multiplayer = True
game2.nota = 10.0

# Terceiro Jogo

game3 = Game()
game3.nome = "Mortal kombat"
game3.anoLancamento = 1997
game3.multiplayer = True
game3.nota = 7.0

# Quarto Jogo

game4 = Game()
game4.nome = "Street Fights"
game4.anoLancamento = 2000
game4.multiplayer = True
game4.nota = 8.5


print("###Dados do Game ####")
print(f'\nNome do jogo: {game1.nome}\nAno de Lançamento: {game1.anoLancamento}')
print(f'\nNome do jogo: {game2.nome}\nAno de Lançamento: {game2.anoLancamento}')
print(f'\nNome do jogo: {game3.nome}\nAno de Lançamento: {game3.anoLancamento}')
print(f'\nNome do jogo: {game4.nome}\nAno de Lançamento: {game4.anoLancamento}')