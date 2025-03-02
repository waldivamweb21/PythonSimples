# Metodo Principal - com o self consegue recuperar qualquer atributos da classe.
#Construtor Instanciado com variavel.

class Game:
    total_games = 0 #variavel de classe para contar o nº total de jogos.
    def __init__(self, nome="", anoLancamento=0, multiplayer=False, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
        Game.total_games += 1
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
        
    def avaliar(self, nota):
        self.totalavaliacoes += nota
        self.avaliadores += 1
        
    def media(self):
        print(f" A Média de avaliação do jogo {self.nome} é: {self.totalavaliacoes / self.avaliadores}")
        
        
        
game1 = Game("street fights", 2017,True, 9.5)
game2 = Game("mortal kombat 3", 2018,True, 8.5)
game3 = Game("the king of fights", 2002,True, 7.5)

game1.ficha_tecnica()
game2.ficha_tecnica()

game1.avaliar(9.0)
game1.avaliar(7.5)
game1.media()

game2.avaliar(6.5)
game2.avaliar(7.5)
game2.media()

# Exibindo o numero total de jogos criados da variavel acima.
print(f"Total de jogos criados: {Game.total_games}")