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
    def decida(self):
        self.ficar.apresente()
        
    def __init__(self):   
        self.sair = Sair()
    def decida(self):
        self.sair.apresente()
    
    def __init__(self):   
        self.joias = Joias()
    def receba(self)
        self.joia.retorna()
class Mesa: 
    def __init__(self): 
        self.partida = Partida()
        self.jogador = Jogador()
        self.turno = Turno()
        self.joias = Joias()
        self.morrer = Morrer()
        