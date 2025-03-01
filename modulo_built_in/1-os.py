import os

# 1 - Retornar a pasta atual
print(os.getcwd())

# 2 - Listar arquivos e pastas 

print(os.listdir())


# 3 - Ver a Versão do sistema S.O. (windows)
os.system("ver")

# 4 - Ver a configuração da maquina (windows)
os.system("systeminfo")

# 5 - Limpar a tela do terminal
os.system("cls")

# 6 - Desligar o computador
#os.system("shotdown /s")
#os.system("shotdown /s /t 0")

#os.system("shotdown /a")

# 7 - criando um script para desligar o pc em hs/min
# 3600 seg = 1h
# 1800  segg = 30 min

def turn_off_one_hour():
    os.system('shutdown /s /t 3600')

def turn_off_one_hour():
    os.system('shutdown /s /t 1800')    
    
def turn_off_one_hour():
    os.system('shutdown /a ')  
    
cancel_shutdown()   