class Game:
    def __init__(self, nome="", anoLancamento=0, multiplayer=False, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
        self.totalavaliacoes = 0
        self.avaliadores = 0


    def __str__(self): 
        return f"Game: {self.nome}"

    
    def ficha_tecnica(self):
        print("###Dados Ficha Técnica dos Games ####")
        print(f"Nome do jogo: {self.nome}")
        print(f"Ano de Lançamento: {self.anoLancamento}")
        print(f"Modo multiplayer: {self.multiplayer}")
        print(f"Avaliação do jogo: {self.nota}\n")

# Criar uma Classe que vai compor a classe Studio:

#Objetivo: Simular uma Empresa dos jogos que já produziu.

class GameStudio:
    def __init__(self, nome=""):
        self.nome = nome
        self.games = []
    
    def add_game(self, game):
        self.games.append(game)
    
    def  avaliar_qualidade_studio(self):
        total_notas = sum(game.nota for game in self.games)
        num_games = len(self.games)
        if num_games == 0:
            print(f"O estudio {self.nome} ainda não lançou os jogos")
        else:
            media_notas = total_notas / num_games
            print(f"Avaliação média dos jogos do estúdio {self.nome}: {media_notas:.2f}")    

game1 = Game("street fights", 2017,True, 9.5)
game2 = Game("mortal kombat 3", 2018,True, 8.5)
game3 = Game("the king of fights", 2002,True, 7.5)            

studio = GameStudio("Awesome Games")
studio.add_game(game1)
studio.add_game(game2)
studio.add_game(game3)

studio.avaliar_qualidade_studio()

for game in studio.games:
    game.ficha_tecnica()