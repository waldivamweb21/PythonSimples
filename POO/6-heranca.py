# Metodo Principal - com o self consegue recuperar qualquer atributos da classe.
#Construtor Instanciado com variavel.

#CLASSE PAI (Super Classe) - Generalista.
class Game:
    total_games = 0  # Variável de classe para contar o nº total de jogos.

    def __init__(self, nome="", anoLancamento=0, multiplayer=False, nota=0):
        self.nome = nome
        self.anoLancamento = anoLancamento
        self.multiplayer = multiplayer
        self.nota = nota
        Game.total_games += 1
        self.total_avaliacoes = 0
        self.avaliadores = 0

    def __str__(self):
        return f"Game: {self.nome}"

    def ficha_tecnica(self):
        print("### Dados Ficha Técnica do Game ####")
        print(f"Nome do jogo: {self.nome}")
        print(f"Ano de Lançamento: {self.anoLancamento}")
        print(f"Modo multiplayer: {'Sim' if self.multiplayer else 'Não'}")
        print(f"Avaliação do jogo: {self.nota}\n")

    def avaliar(self, nota):
        self.total_avaliacoes += nota
        self.avaliadores += 1

    def media(self):
        if self.avaliadores > 0:
            media = self.total_avaliacoes / self.avaliadores
            print(f"A média de avaliação do jogo {self.nome} é: {media:.2f}")
        else:
            print(f"O jogo {self.nome} ainda não tem avaliações.")


# Classe derivada (SubClasse) - Especialista.
class SinglePlayerGame(Game):
    def __init__(self, nome="", anoLancamento=0, nota=0, enredo=""):
        super().__init__(nome, anoLancamento, multiplayer=False, nota=nota)
        self.enredo = enredo

#Utilizou Polimorfismo. Add Alteracao na funcao.

    def ficha_tecnica(self):
        super().ficha_tecnica()
        print(f"Enredo: {self.enredo}\n")


# Criando instâncias para testar
mult_game = Game("Counter-Strike", 1999, True, 8.0)
mult_game.ficha_tecnica()

sing_game = SinglePlayerGame("Crash Bandicoot", 2021, 9.5, "Emocionante jogo de aventura e desafios na selva.")
sing_game.ficha_tecnica()

#Testando avaliações
sing_game.avaliar(9)
sing_game.avaliar(10)
sing_game.media()

