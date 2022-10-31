import pygame
import random
import time
"""Ambiente """
ANCHO=1300
ALTO=700
NEGRO=[0,0,0]
ROJO=[255,0,0]
VERDE=[0,255,0]
AMARILLO=[255,255,0]
BLANCO=[255,255,255]

def mapa1(bloques):
    b=Bloque([385,400],385,35)
    bloques.add(b)
    b2=Bloque([924,246],231,35)
    bloques.add(b2)
    b3=Bloque([1694,323],231,35)
    bloques.add(b3)
    bl=Bloque([0,400],308,35, ROJO)
    bloques.add(bl)
    bl2=Bloque([770,477],924,154, ROJO)
    bloques.add(bl2)
    bl3=Bloque([1694,631],462,35, ROJO)
    bloques.add(bl3)
    bl4=Bloque([2233,785],231,35, ROJO)
    bloques.add(bl4)
    b5=Bloque([1925,939],539,154, ROJO)
    bloques.add(b5)
    b5=Bloque([1694,1093],231,35, ROJO)
    bloques.add(b5)
    b6=Bloque([1386,1247],231,35, ROJO)
    bloques.add(b6)
    b7=Bloque([1001,1324],231,35, ROJO)
    bloques.add(b7)
    b8=Bloque([692,1478],231,35, ROJO)
    bloques.add(b8)
    b9=Bloque([384,1623],308,35, ROJO)
    bloques.add(b9)
    b10=Bloque([924,1623],1001,35, ROJO)
    bloques.add(b10)
    b11=Bloque([2002,1478],231,35, ROJO)
    bloques.add(b11)
    b12=Bloque([2387,1623],693,35, ROJO)
    bloques.add(b12)
    b13=Bloque([3157,1478],231,35, ROJO)
    bloques.add(b13)
    b14=Bloque([3388,1324],154,35, ROJO)
    bloques.add(b14)
    b15=Bloque([3542,1170],308,154, ROJO)
    bloques.add(b15)
    b16=Bloque([3311,1016],231,35, ROJO)
    bloques.add(b16)
    b17=Bloque([2695,862],532,35, ROJO)
    bloques.add(b17)
    b18=Bloque([3080,631],231,35, ROJO)
    bloques.add(b18)
    b19=Bloque([3311,477],616,154, ROJO)
    bloques.add(b19)
    b20=Bloque([4004,400],231,154, ROJO)
    bloques.add(b20)
    b21=Bloque([4235,477],616,154, ROJO)
    bloques.add(b21)
    bV1=Bloque([2464,0],231,1456, ROJO)
    bloques.add(bV1)
    bV2=Bloque([3850,477],77,1523, ROJO)
    bloques.add(bV2)
    return bloques

ubicacionobjeto=[(694,334),(1397,415),(2057,566),
                 (1993,878),(1705,1031),(1425,1183),
                 (1049,1259),(1185,1569),(1673,1569),
                 (2185,1417),(2785,1569),(3321,1414),
                 (3491,1262),(3345,950),(2745,798),
                 (3057,798),(3257,566),(3761,421),
                 (4313,421),(1857,259)]


class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.a=a
        self.con=0
        self.dir=0
        self.image = self.a[self.dir][self.con]
        self.pausa = 0
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y= pos[1]
        self.velx=0
        self.vely=+9
        self.salto=0
        self.f_velx=0
        self.f_vely=0
        self.Direc=0
        self.vida=20
        self.aumen=1
        self.tipobala=1
        self.sanar=[0,0]
        self.escudo=False 
        self.bloques=None

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y - 20
        return [x,y]

    def update(self):
        if self.velx != 0:
            if self.pausa==2:
                if self.con < 3:
                    if self.salto == 0:
                        self.con+=1
                    self.pausa=0
                else:
                    self.con =0
                    self.pausa=0
            else:
                self.pausa+=1
        self.image = self.a[self.dir][self.con]
        self.rect.x+=self.velx
        ls_col=pygame.sprite.spritecollide(self,self.bloques, False)
        for b in ls_col:
            self.aux=True
            if self.velx>0:
                if self.rect.right > b.rect.left:
                    self.rect.right = b.rect.left
                    self.velx=0
                    self.salto=0
                    self.con=0
                    self.dir=0
            if self.velx<0:
                if self.rect.left < b.rect.right:
                    self.rect.left = b.rect.right
                    self.velx=0
                    self.salto=0
                    self.con=0
                    self.dir=0

        self.rect.y+=self.vely        
        ls_col=pygame.sprite.spritecollide(self,self.bloques, False)
        for b in ls_col:
            self.aux=True
            if self.vely>0:
                if self.rect.bottom > b.rect.top:
                    self.rect.bottom = b.rect.top
                    self.vely=0
                    self.salto=0
                    #2500*1800
            if self.vely<0:
                if self.rect.top < b.rect.bottom:
                    self.rect.top = b.rect.bottom
                    self.vely=0
                    self.salto=0
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely

class Rival(pygame.sprite.Sprite):
    def __init__(self, pos,m):
        pygame.sprite.Sprite.__init__(self)
        self.m=m
        self.siguiente=0
        self.pause = 0
        self.image= self.m[self.siguiente]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y= pos[1]
        self.velx=0
        self.f_velx=0
        self.f_vely=0
        self.vely=0
        self.vida=2
        self.parar=random.randrange(0,70)
        self.tmp=random.randrange(40,90)

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y - 20
        return [x,y]

    def update(self):
        cont=0
        self.tmp -= 1
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        if self.pause == 1:
            if self.siguiente<3:
                self.siguiente+=1
            else:
                self.siguiente2=0
            self.pause =0
        if self.parar==0:
            self.velx=0
        if self.parar!=0:
            self.parar-=1
            

        self.image=self.m[self.siguiente]
        self.pause+=1
        self.rect.y+=self.vely
        self.rect.x+=self.velx
        self.rect.x += self.f_velx
        self.rect.y += self.f_vely


class Rival2(pygame.sprite.Sprite):
    def __init__(self, pos,m2):
        pygame.sprite.Sprite.__init__(self)
        self.m2=m2
        self.siguiente2=0
        self.pause=0
        self.image= self.m2[self.siguiente2]
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=0
        self.vely=0
        self.vida=2
        self.f_velx=0
        self.f_vely=0
        self.tmp=random.randrange(40,90)

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y - 20
        return [x,y]

    def update(self):
        self.tmp -= 1
        self.rect.x+=self.velx
        self.rect.y+=self.vely
        if self.pause == 1:
            if self.siguiente2<3:
                self.siguiente2+=1
            else:
                self.siguiente2=0
            self.pause =0

        self.image=self.m2[self.siguiente2]
        self.pause+=1
        self.rect.y+=self.vely
        self.rect.x+=self.velx
        self.rect.x += self.f_velx
        self.rect.y += self.f_vely







class Bloque(pygame.sprite.Sprite):
    def __init__(self, pos, d_an , d_al , cl=VERDE):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([d_an,d_al])
        self.image.fill(cl)
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=0
        self.f_vely=0
    def update(self):
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely




class Bala(pygame.sprite.Sprite):
    def __init__(self, pos , imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=(pos[1]+50)
        self.velx=0
    def update(self):
        self.rect.x+=self.velx

class Bala2(pygame.sprite.Sprite):
    def __init__(self, pos , imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=(pos[1]+50)
        self.velx=0
    def update(self):
        self.rect.x+=self.velx
        

class M_vida (pygame.sprite.Sprite):
    def __init__(self, pos ):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("vida.png")
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.velx=-10
        self.vely=0
        
    def update(self):
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely


class Chaleco(pygame.sprite.Sprite):
    def __init__(self, pos,imagenx):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagenx
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=-10
        self.f_vely=0
    
    def update(self):
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely

class CambioBala(pygame.sprite.Sprite):
    def __init__(self, pos,imagenx):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagenx
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=-10
        self.f_vely=0
    
    def update(self):
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely


class End(pygame.sprite.Sprite):
    def __init__(self, pos,imagenx):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagenx
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=-10
        self.f_vely=0
    
    def update(self):
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely



class Generador(pygame.sprite.Sprite):
    def __init__(self, pos, cl):
        pygame.sprite.Sprite.__init__(self)
        self.image=cl
        self.cantidad=0
        self.vida_T=3
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=-10
        self.f_vely=0
        self.temp=random.randrange(200)

    def update(self):
        self.temp-=1
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely

class ObjetoColicionable(pygame.sprite.Sprite):
    def __init__(self, pos, cl):
        pygame.sprite.Sprite.__init__(self)
        self.image=cl
        self.vida_T=3
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=-10
        self.f_vely=0

    def update(self):
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely



if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    cala=pygame.image.load("balaw.png")
    cala2=pygame.image.load("bala2.png")
    mago=pygame.image.load("final.png")
    cañon=pygame.image.load("cañon2.png")
    gen2=pygame.image.load("generador.png")
    info2=pygame.image.load("vida.png")
    escu=pygame.image.load("escudo.png")
    icono=pygame.image.load("Escudoicono.png")
    oscuridad=pygame.image.load("oscuridad.png")
    JugadorA = pygame.image.load('animaciones.png')
    cubrir=pygame.mixer.Sound("Cubrir.wav")
    disp=pygame.mixer.Sound("disp.wav")
    fuente_J=pygame.font.Font(None,32)
    fuente_K=pygame.font.Font(None,64)
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    cambiobala=pygame.sprite.Group()
    bloques_2=pygame.sprite.Group()
    generadores=pygame.sprite.Group()
    generadores2=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas2=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    balas_M=pygame.sprite.Group()
    chalecos=pygame.sprite.Group()
    m_vida=pygame.sprite.Group()
    rivales2=pygame.sprite.Group()
    rivales=pygame.sprite.Group()
    ends=pygame.sprite.Group()
    objetoscolicionables=pygame.sprite.Group()
    

    a=[]
    for j in range(4):
        colj=[]
        for i in range(4):
            anima = JugadorA.subsurface(70*i,70*j,70,70)
            colj.append(anima)
        a.append(colj)    
    j=Jugador([10,30])
    jugadores.add(j)
    
    f_key=0
    f_posx=0
    f_velx=0
    f_posy=0
    f_vely=0
    limv_an=ANCHO
    limv_alt=ALTO
    reloj=pygame.time.Clock()
    fin=False
    fin_prev=False
    fin_Nivel_1=False
    fin_Nivel_2=False
    evento=0
    #inicio del juego
    instrucciones=pygame.image.load("instruccione.png")
    inicio=pygame.mixer.Sound("inicio.wav")
    fondo=pygame.image.load("fondo.jpg")
    info=fondo.get_rect()
    inicio.play(1)
    while (not fin ) and (not fin_prev) and (not fin_Nivel_1) :
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    evento=0
            if event.type==pygame.MOUSEBUTTONDOWN and evento==0:
                click=event.pos
                if (click[0]>620 and click[0]<700 and click[1]>300 and click[1]<332):
                    fin_prev=True
                    inicio.stop()
                if (click[0]>585 and click[0]<732 and click[1]>300 and click[1]<432):
                    evento=1
                if (click[0]>525 and click[0]<864 and click[1]>500 and click[1]<532):
                    evento=2
            
                
        if evento==0:
            ventana.blit(fondo,[0,0])
            mun=" La Maldicion Del Mago " 
            municion=fuente_K.render(mun,True,ROJO)
            ventana.blit(municion,[400,100])
            mun=" PLAY " 
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[620,300])
            mun=" CREDITOS " 
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[585,400])
            mun="INTRUCCIONES DE JUEGO" 
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[525,500])

        if evento==1:
            ventana.blit(fondo,[0,0])
            mun=" Creditos"
            cristian="Cristian Orlando Ramirez Naranjo"
            profesor="Carlos Andres Lopes " 
            utp=" UTP "
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[620,100])
            municion=fuente_J.render(cristian,True,BLANCO)
            ventana.blit(municion,[540,200])
            municion=fuente_J.render(profesor,True,BLANCO)
            ventana.blit(municion,[580,500])
            municion=fuente_K.render(utp,True,ROJO)
            ventana.blit(municion,[640,600])
            
            
            
        if evento==2:
            ventana.fill(NEGRO)
            ventana.blit(fondo,[0,0])
            ventana.blit(instrucciones,[100,100])

        pygame.display.flip()
                
    #primer nivel
    limy=100
    limy2=300
    msc=pygame.mixer.Sound("castle.wav")
    maqu=pygame.image.load("Rival2.png")
    Enemigos2 = pygame.image.load('enemy3.png')
    col2 = []
    for i2 in range(4):
        Cuadro2 = Enemigos2.subsurface(179*i2,0,179,128)
        col2.append(Cuadro2)
    Enemigos= pygame.image.load('enemy.png')
    col=[]
    for i2 in range(4):
        Cuadro= Enemigos.subsurface(130*i2,0,130,110)
        col.append(Cuadro)
        
    fondo=pygame.image.load("mapa1.png")
    hoyo=pygame.image.load("nido.png")
    oscuridad=pygame.image.load("oscuridad.png")
    torres=pygame.sprite.Group()
    maquina_1=pygame.sprite.Group()
    bloques=mapa1(bloques)
    j.bloques=bloques
    c=Chaleco(ubicacionobjeto[random.randrange(0,19)],icono)
    chalecos.add(c)
    n=M_vida(ubicacionobjeto[random.randrange(0,19)])
    m_vida.add(n)

    n=CambioBala(ubicacionobjeto[random.randrange(0,19)],cala2)
    cambiobala.add(n)
    
    g=Generador([1709,233], hoyo)
    generadores.add(g)
    g=Generador([3641,1112], hoyo)
    generadores.add(g)

    g=Generador([1322,1460], gen2)
    generadores2.add(g)

    g=Generador([3646,313], gen2)
    generadores2.add(g)    
    
    g=End([4435,283], mago)
    ends.add(g)

    for numero in range(0,20):
        g=ObjetoColicionable(ubicacionobjeto[numero], cañon)
        objetoscolicionables.add(g)
    
    aux=20
    msc.play(1)
    while (not fin) and (not fin_Nivel_1):
        tiempo=int (pygame.time.get_ticks()/1000)
        if aux== tiempo:
            aux+=1
        #Gestion eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if j.salto == 0:
                        j.dir=1
                    j.Direc=1
                    j.vely=9
                    j.velx=5
                    
                if event.key == pygame.K_LEFT:
                    if j.salto == 0:
                        j.dir=3
                    j.Direc=0
                    j.vely=9
                    j.velx= -5
                if event.key == pygame.K_UP and j.salto ==0:
                    j.salto+=1
                    j.vely= -18
                    if j.Direc==1:
                        j.dir = 0
                        j.con = 1
                    if j.Direc==0:
                        j.dir = 2
                        j.con = 1

                if event.key == pygame.K_d and j.vely==0 and j.velx==0:
                    j.velx=0
                
                    if f_posx<=-3350:
                        f_velx=0
                    else:
                        f_velx=-5
                if event.key == pygame.K_a and j.vely==0 and j.velx==0:
                    j.velx=0
                    if f_posx>=0:
                        f_velx=0
                    else:
                        f_velx=5
                if event.key == pygame.K_w and j.vely==0 and j.velx==0:
                    j.vely=0
                    if f_posy>=0:
                        f_vely=0
                    else:
                        f_vely=5
                        
                if event.key == pygame.K_q and j.aumen==2:
                    j.escudo=True
                    aux=j.vida
                        
                if event.key == pygame.K_s and j.vely==0 and j.velx==0:
                    j.vely=0
                    if f_posy<=-1200:
                        f_vely=0
                    else:
                        f_vely=-5
                if event.key == pygame.K_e:
                    p=j.RetPos()
                    if j.tipobala==1:
                        b=Bala([p[0],p[1]],cala)
                        if j.Direc==1:
                            b.velx= 10
                            balas.add(b)
                        if j.Direc==0:
                            b.velx= -10
                            balas.add(b)
                        if j.Direc==1:
                            if j.salto == 1:
                                j.dir = 0
                                j.con =3
                            else:
                                j.dir = 0
                                j.con = 2
                        if j.Direc==0:
                            if j.salto ==1:
                                j.dir = 2
                                j.con = 3
                            else:
                                j.dir = 2
                                j.con = 2
                    if j.tipobala==2:
                        b=Bala2([p[0],p[1]],cala2)
                        if j.Direc==1:
                            b.velx= 10
                            balas2.add(b)
                        if j.Direc==0:
                            b.velx= -10
                            balas2.add(b)
                        if j.Direc==1:
                            if j.salto == 1:
                                j.dir = 0
                                j.con =3
                            else:
                                j.dir = 0
                                j.con = 2
                        if j.Direc==0:
                            if j.salto ==1:
                                j.dir = 2
                                j.con = 3
                            else:
                                j.dir = 2
                                j.con = 2
                    disp.play()   
            
            if event.type == pygame.KEYUP:
                j.escudo=False
                j.vely=9
                j.velx=0
                f_velx=0
                f_vely=0
                if event.key == pygame.K_q and j.aumen==2:
                    j.vida=aux

                        
                
        #Control de pantalla       
        if j.rect.x > limv_an:
            fin_Nivel_1=True
            fin_Nivel_2=True
            j.vida=0
            
        if j.rect.y > limv_alt:
            fin_Nivel_1=True
            fin_Nivel_2=True
            j.vida=0
            
        if j.rect.x < 0:
            fin_Nivel_1=True
            fin_Nivel_2=True
            j.vida=0
            
        if j.rect.y < 0:
            fin_Nivel_1=True
            fin_Nivel_2=True
            j.vida=0
            
        for b in bloques:
            b.f_velx=f_velx
            b.f_vely=f_vely
            
        for j in jugadores:
            j.f_velx=f_velx
            j.f_vely=f_vely
            
        for t in torres:
            t.f_velx=f_velx
            t.f_vely=f_vely

        for c in chalecos:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in m_vida:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in generadores:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in generadores2:
            c.f_velx=f_velx
            c.f_vely=f_vely

        for c in rivales2:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in rivales:
            c.f_velx=f_velx
            c.f_vely=f_vely

        for c in maquina_1:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in ends:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in objetoscolicionables:
            c.f_velx=f_velx
            c.f_vely=f_vely
            
        for c in cambiobala:
            c.f_velx=f_velx
            c.f_vely=f_vely

            

        #generadores      
        for g2 in generadores:
            if g2.temp <= 0:
                g2.temp=random.randrange(20,100)
                r2=Rival2([g2.rect.x,g2.rect.y],col2)
                
                if j.RetPos()<r2.RetPos():
                    r2.velx=-2    
                    rivales2.add(r2)
                else:
                    r2.velx=2
                    rivales2.add(r2)
        
        for g in generadores2:
            if g.temp <= 0 and g.cantidad < 3 and g.rect.y > 0 and g.rect.y < ALTO:
                g.cantidad+=1
                g.temp=random.randrange(20,100)
                r=Rival([g.rect.x,g.rect.y+60],col)
                
                if j.RetPos()<r.RetPos():
                    r.velx=-2    
                    rivales.add(r)
                    if g.rect.x-100==r.RetPos()[0]:
                        r.velx=0       
                else:
                    r.velx=2
                    rivales.add(r)
                    if g.rect.x+100==r.RetPos()[0]:
                        r.velx=0
            
                
        for r in rivales:
            if r.tmp < 0:
                pos=r.RetPos()
                b=Bala(pos,cala)
                disp.play()
                b.velx=-10
                balas_r.add(b)
                r.tmp=random.randrange(20,90)
        #Comentario
                
        #Limpieza de memoria
        for b in balas:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, bloques, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas.remove(b)
            for r in ls_colision:
                balas.remove(b)
                
        for b in balas2:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, bloques, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas2.remove(b)
            for r in ls_colision:
                balas2.remove(b)
                
                
        for b in balas_r:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, jugadores, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas_r.remove(b)
            for r in ls_colision:
                j.vida-=2
                balas_r.remove(b)
                
        for b in balas:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, rivales2, True)
            for e in ls_colision:
                balas.remove(b)
                if(j.sanar[0]==1 and j.vida<=19):
                    if(j.sanar[1]==3):
                        j.vida+=1
                        j.sanar[1]=1
                    else:
                        j.sanar[1]+=1
                
        for b in balas2:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, rivales2, True)

                

        #Enemigos generadores 2
        for b in balas:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, rivales, True)
            for e in ls_colision:
                balas.remove(b)
                for g in generadores2:
                    g.cantidad-=1
                    
        for b in balas2:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, rivales, True)
            for e in ls_colision:
                balas2.remove(b)
                for g in generadores2:
                    g.cantidad-=1
    
        #golpe a generadoser

        for b in generadores:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    generadores.remove(b)
                    
        for b in generadores2:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    generadores2.remove(b)

        for b in objetoscolicionables:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    objetoscolicionables.remove(b)

        for b in generadores:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas2, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    generadores.remove(b)
                    
        for b in generadores2:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas2, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    generadores2.remove(b)

        for b in objetoscolicionables:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas2, True)
            for r in ls_colision:
                b.vida_T-=3
                if b.vida_T==0:
                    objetoscolicionables.remove(b)


        
        
        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, chalecos, True)
        for e in ls_colision:
            j.aumen=2
            
        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, cambiobala, True)
        for e in ls_colision:
            j.tipobala=2

        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, m_vida, True)
        for e in ls_colision:
            j.sanar[0]=1

        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, maquina_1, False)
        for e in ls_colision:
            j.vida-=2



        ls_col=pygame.sprite.spritecollide(j, rivales2, True)
        for e in ls_col:
            j.vida-=1

            

        #limpieza de memoria para los rivales 1        
        for r in rivales:
            if r.rect.y <-50 or r.rect.y > ALTO+30:
                rivales.remove(r)
        for r in rivales:
            if r.rect.x <-50 or r.rect.x > ANCHO+30:
                rivales.remove(r)
            
        
            
        # fin de juego
        ls_col=pygame.sprite.spritecollide(j, ends, True)
        for e in ls_col:
            fin_Nivel_1= True

        for j in jugadores:
            if j.vida < 1:
                fin_Nivel_1= True
                
    
       
        #Refresco
       
        
        
        #ventana.fill(NEGRO)
        f_posx += f_velx
        f_posy += f_vely
        bloques.update()
        mun=" " + str(tiempo)
        municion=fuente_J.render(mun,True,BLANCO)

        Nivel=" Nivel 1"
        nivel=fuente_J.render(Nivel,True,ROJO)
        jugadores.update()
        cambiobala.update()
        generadores.update()
        generadores2.update()
        objetoscolicionables.update()
        chalecos.update()
        rivales2.update()
        rivales.update()
        m_vida.update()
        ends.update()
        balas.update()
        balas2.update()
        balas_r.update()
        torres.update()
        maquina_1.update()
        ventana.blit(fondo,[f_posx,f_posy])
        if(j.escudo==True):
           ventana.blit(escu,[j.rect.x-60,j.rect.y-70])
           cubrir.play()
            
        jugadores.draw(ventana)
        balas.draw(ventana)
        balas2.draw(ventana)
        ventana.blit(municion,[620,3])
        ventana.blit(nivel,[1000,3])
        balas_r.draw(ventana)
        chalecos.draw(ventana)
        rivales2.draw(ventana)
        m_vida.draw(ventana)
        objetoscolicionables.draw(ventana)
        generadores.draw(ventana)
        generadores2.draw(ventana)
        rivales.draw(ventana)
        
        maquina_1.draw(ventana)
        #bloques.draw(ventana)
        torres.draw(ventana)
        ends.draw(ventana)
        ventana.blit(oscuridad,[0,0])
        x=10
        for i in range(j.vida):
            ventana.blit(info2,[x,10])
            x=x+20
        if(j.tipobala==1):
            ventana.blit(cala,[20,40])
            
        if(j.tipobala==2):
            ventana.blit(cala2,[20,40])
            
        if(j.aumen==2):
            ventana.blit(icono,[60,40])
        if(j.sanar[0]==1):
            ventana.blit(info2,[100,40])
            
        pygame.display.flip()
        reloj.tick(40)
            

        
        
        
                
#Final del juego
    msc.stop()
    aux=0
    if aux==0:
        aux=tiempo
    fondo=pygame.image.load("game_over.jpg")
    while (not fin)and fin_Nivel_1==True:
        #Gestion de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
            
        if (j.vida>=1):
            ventana.fill(NEGRO)
            ventana.blit(fondo,[0,0])
            mun=" VICTORIA "
            municion=fuente_K.render(mun,True,BLANCO)
            ventana.blit(municion,[520,400])
            mun="El tiempo jugado es de "+ str(aux)+" segundos"
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[475,450])

        else:
            ventana.fill(ROJO)
            ventana.blit(fondo,[0,0])
            mun=" GAME OVER "
            municion=fuente_K.render(mun,True,BLANCO)
            ventana.blit(municion,[520,400])
            mun="El tiempo jugado es de "+ str(aux)+" segundos"
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[475,450])


                
        pygame.display.flip()
        
        

