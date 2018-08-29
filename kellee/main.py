# hedy.kellee.main.py
from_spy.vitollino.main import Cena, Texto, Elemento
from_spy.vitollino.main import INVENTARIO as inv

HOMEMARANHA "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwjSmreJp5LdAhXDHZAKHY29A4cQjRx6BAgBEAU&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F574771971170218088%2F&psig=AOvVaw0zzyBdsssUOQiqUfvLLmSY&ust=1535633484620048"
YODA "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj3tf2eqJLdAhWBEJAKHXu8Cn4QjRx6BAgBEAU&url=https%3A%2F%2Fconversamos.wordpress.com%2F2013%2F08%2F11%2Fjedi-master-1-yoda%2F&psig=AOvVaw3YDKghW2pDPgsash3kWLKu&ust=1535633896213333"

TARZAN "https://www.google.com.br/imgres?imgurl=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fdisney%2Fimages%2Fe%2Fe2%2FTarzan_Character.png%2Frevision%2Flatest%3Fcb%3D20180126232838&imgrefurl=http%3A%2F%2Fdisney.wikia.com%2Fwiki%2FFile%3ATarzan_Character.png&docid=eBlujy3ukMGquM&tbnid=3rlbuyAmITmFHM%3A&vet=10ahUKEwiipPC7qJLdAhWGkZAKHX1nB8oQMwhBKAkwCQ..i&w=1236&h=2560&hl=pt-BR&safe=strict&bih=651&biw=1366&q=tarzan%20png&ved=0ahUKEwiipPC7qJLdAhWGkZAKHX1nB8oQMwhBKAkwCQ&iact=mrc&uact=8"
FLORESTA "https://www.google.com.br/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwivrYywp5LdAhUFUZAKHaz9D8QQjRx6BAgBEAU&url=https%3A%2F%2Fwww.elo7.com.br%2Fpainel-floresta-g-frete-gratis%2Fdp%2F6B7492&psig=AOvVaw23XqpjhQK5Bm0N70G7PxiH&ust=1535633667116683"

CASA "https://www.google.com.br/imgres?imgurl=https%3A%2F%2Fimg.elo7.com.br%2Fproduct%2Fzoom%2F161E881%2Fponto-cruz-em-pdf-rua-de-bruxelas-grafico-de-ponto-cruz.jpg&imgrefurl=https%3A%2F%2Fwww.elo7.com.br%2Fcasa-da-floresta-grafico-ponto-cruz%2Fdp%2F8C96B5&docid=oyHtiCnuRnMgNM&tbnid=RHvlj1iqfdqFhM%3A&vet=10ahUKEwibxYjLp5LdAhWHTJAKHX94AVoQMwieASgjMCM..i&w=1200&h=899&hl=pt-BR&safe=strict&bih=651&biw=1366&q=casa%20na%20floresta&ved=0ahUKEwibxYjLp5LdAhWHTJAKHX94AVoQMwieASgjMCM&iact=mrc&uact=8"
MESADECHA "https://www.google.com.br/imgres?imgurl=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fdisneyprincesas%2Fimages%2Fe%2Fef%2FAlice-in-wonderland-disneyscreencaps.com-5785.jpg%2Frevision%2Flatest%3Fcb%3D20140822145715%26path-prefix%3Dpt-br&imgrefurl=http%3A%2F%2Fpt-br.disneyprincesas.wikia.com%2Fwiki%2FChapeleiro_Maluco&docid=wohyaaDUoCexEM&tbnid=i1jPqPPI-c1P9M%3A&vet=10ahUKEwigucLoqJLdAhWBS5AKHTefDoIQMwhmKCYwJg..i&w=1424&h=1080&hl=pt-BR&safe=strict&bih=651&biw=1366&q=mesa%20de%20ch%C3%A1%20lebre%20%20png&ved=0ahUKEwigucLoqJLdAhWBS5AKHTefDoIQMwhmKCYwJg&iact=mrc&uact=8"

def criarcena():
    floresta = Cena(img=FLORESTA)
    casa = Cena(img=CASA)
    casa2 = Cena(img=CASA)
    mesadecha = Cena(img=MESADECHA)
    mesadecha2 = Cena(img=MESADECHA2)
    floresta.direita = casa
    casa.direita = casa2
    casa2.direita = mesadecha
    mesadecha.direita = mesadecha2
        
    homemaranha = Elemento(img=HOMEMARANHA, tit="Homem-Aranha", style=dict(left="100px", top="160px", width="60px", height="200px"))
    homemaranha.entra(floresta)
    ehomemaranha = Texto (floresta, "Finalmente um tempo pra mim!")
    homemaranha.vai = ehomemaranha.vai
    
    homemaranha = Elemento(img=HOMEMARANHA, tit="Homem-Aranha", style=dict(right="100px", top="160px", width="60px", height="200px"))
    homemaranha.entra(casa)
    ehomemaranha = Texto (casa, "Ohhh! Uma casa!!)
    homemaranha.vai = ehomemaranha.vai
    
    homemaranha = Elemento(img=HOMEMARANHA, tit="Homem-Aranha", style=dict(right="100px", top="160px", width="60px", height="200px"))
    homemaranha.entra(casa2)
    ehomemaranha = Texto (casa2, "Deve ser do Mestre Yoda! Mas ele não esta aqui... vou procurá-lo.")
    homemaranha.vai = ehomemaranha.vai
    
    homemaranha = Elemento(img=HOMEMARANHA, tit="Homem-Aranha", style=dict(right="100px", top="160px", width="60px", height="200px"))
    homemaranha.entra(mesadecha)
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(right="150px", top="160px", width="60px", height="200px"))
    tarzan.entra(mesadecha)
    etarzan = Texto (mesadecha, "Vai um chá ai?")
    tarzan.vai = etarzan.vai
    
    floresta.vai()
    
criarcenas()    
    
    
    homemaranha = Elemento(img=HOMEMARANHA, tit="Homem-Aranha", style=dict(right="100px", top="160px", width="60px", height="200px"))
    homemaranha.entra(mesadecha2)
    tarzan = Elemento(img=TARZAN, tit="Tarzan", style=dict(right="150px", top="160px", width="60px", height="200px"))
    tarzan.entra(mesadecha2)
    ehomemaranha = Texto (mesadecha2, "Não, só tomo Vodka! Obrigada!")
    homemaranha.vai = ehomemaranha.vai
   
    