#importando o modulo nativo do python
import pprint

musicaDict = {
    "banda 1":{ 
        "nome da banda": "Cbjr",
        "Ano de Lançamento ": "1991", 
        "nota da banda" : 9.0, 
        "Genero" : ["rock", "reggae", "ska", "maracatu", "house"]
    },
    "banda 2":{ 
        "nome da banda": "raimundos",
        "Ano de Lançamento ": "1994", 
        "nota da banda": 8.0, 
        "Genero": ["rock", "forro-core", "harcore", "punk"]
    },
    "banda 3" : { 
        "nome da banda": "O rappa",
        "Ano de Lançamento ": "2001", 
        "nota da banda" : 7.0, 
        "Genero" : ["rock", "pop", "reggae", "rap"]
    },
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(musicaDict)

# 1 - Buscar uma informação dentro de um dicionario aninhado.
print(musicaDict["banda 1"]["Genero"])

# 2 - buscar novo item
musicaDict["banda 1"]["produtor"] = "Rick Bonadio"
print(musicaDict["banda 1"])

# 3- deletar um dicionario
del musicaDict["banda 3"]
pp.pprint(musicaDict)




