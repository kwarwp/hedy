# hedy.roxanne.main.py
from _spy.vitollino.main import Cena,Elemento
from _spy.vitollino.main import INVENTARIO as inv
PRAIA="https://img.freepik.com/fotos-gratis/praia-e-no-ceu-uma-bela-ilha-tropical_36076-482.jpg?size=626&ext=jpg"
SOL="https://imagensemoldes.com.br/wp-content/uploads/2018/06/Imagem-Sol-Sol-Brilhando-4-PNG.png"
BANHISTA="http://s2.glbimg.com/O9sJ4PnmZfJRxC1-A9t8hYoWIjI=/620x0/top/s.glbimg.com/jo/eg/f/original/2013/11/04/mg_6079.jpg"
class praiouuu():
    praia= Cena(img=PRAIA)
    sol= Elemento(img=SOL)
    banhista= Elemento(img=BANHISTA)
    sol.entra(praia)
    banhista.entra.sul(praia)
    praia.vai()
praiouuu() 