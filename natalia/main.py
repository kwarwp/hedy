# hedy.natalia.main.zpy
from kathryn.main import Rodada
from lisa.main import Partida
from ruzwana.main import Ficar
from ruzwana.main import Turno
from kathryn.main import Joias
from lisa.main import Morrer

"""
kathryn - Baralho - Joias - Rodada
callie - Perigo - Perder - Tesouro
ruzwana - Ficar - Turno - Sair 
natalia - Mesa - Iniciar - Jogador 
lisa - Decisao - Morrer - Partida
meredith - Universo 
"""


class Iniciar: 
    def __init__(self):
        print("Iniciar __init__")
        self.rodada = Rodada()
    def inicie(self):
        self.rodada.inicie()
        
class Jogador:
    def __init__(self):
        self.ficar = Ficar()
    
        self.sair = Sair()
        
class Mesa: 
    def __init__(self): 
        self.partida = Partida()
        self.jogador = Jogador()
        self.turno = Turno()
        self.joias = Joias()
        self.morrer = Morrer()
        
if __natalia__ == "__main__": 
    iniciar = Iniciar()
    iniciar.inicie()


