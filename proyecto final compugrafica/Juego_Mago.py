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

def mapa2(bloques):
    b=Bloque([0,400],1770,35,ROJO)
    bloques.add(b)
    b2=Bloque([1848,631],693,35, ROJO)
    bloques.add(b2)
    b3=Bloque([1617,785],154,35, ROJO)
    bloques.add(b3)
    b4=Bloque([1848,939],770,35, ROJO)
    bloques.add(b4)
    b5=Bloque([1617,1093],154,35, ROJO)
    bloques.add(b5)
    b6=Bloque([1463,1324],1463,35, ROJO)
    bloques.add(b6)
    b7=Bloque([924,1247],385,35, ROJO)
    bloques.add(b7)
    b8=Bloque([457,1093],385,35, ROJO)
    bloques.add(b8)
    b9=Bloque([77,1247],154,35, ROJO)
    bloques.add(b9)
    b10=Bloque([77,1555],231,35, ROJO)
    bloques.add(b10)
    b11=Bloque([462,1709],154,35, ROJO)
    bloques.add(b11)
    b12=Bloque([770,1709],616,35, ROJO)
    bloques.add(b12)
    b13=Bloque([1616,1709],3003,35, ROJO)
    bloques.add(b13)
    b14=Bloque([3156,1478],539,231, ROJO)
    bloques.add(b14)
    b15=Bloque([3233,1093],385,35, ROJO)
    bloques.add(b15)
    b16=Bloque([3311,1093],231,385, ROJO)
    bloques.add(b16)
    b17=Bloque([2617,1093],154,35, ROJO)
    bloques.add(b17)
    b18=Bloque([3696,1247],385,35, ROJO)
    bloques.add(b18)
    b19=Bloque([4081,785],385,35, ROJO)
    bloques.add(b19)
    bv=Bloque([2001,0],231,1386, ROJO)
    bloques.add(bv)
    
    bv2=Bloque([1539,400],77,695, ROJO)
    bloques.add(bv2)
    
    return bloques

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



class Rival_E(pygame.sprite.Sprite):
    def __init__(self, pos, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=0
        self.f_vely=0
        self.vida_T=5
        self.tmp=random.randrange(40,90)
    
    def update(self):
        self.tmp -= 1
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
        
class Maquina_1(pygame.sprite.Sprite):
    def __init__(self, pos, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=0
        self.velx=1
        self.f_vely=0
        self.vida_M1=100
        #self.tmp=random.randrange(40,90)

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y 
        return [x,y]
    
    def update(self):
        #self.tmp -= 1
        self.rect.x+=self.velx
        self.rect.x+=self.f_velx
        self.rect.y+=self.f_vely

class Maquina_2(pygame.sprite.Sprite):
    def __init__(self, pos, imagen):
        pygame.sprite.Sprite.__init__(self)
        self.image=imagen
        self.rect=self.image.get_rect()
        self.rect.x=pos[0]
        self.rect.y=pos[1]
        self.f_velx=0
        self.vely=1
        self.f_vely=0
        self.vida_M2=100
        self.tmp=random.randrange(40,90)

    def RetPos(self):
        x=self.rect.x
        y=self.rect.y 
        return [x,y]
    
    def update(self):
        self.tmp -= 1
        self.rect.y+=self.vely
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


if __name__ == '__main__':
    pygame.init()
    #Definicion de variables
    ventana=pygame.display.set_mode([ANCHO,ALTO])
    prin=pygame.image.load("wizar1t.png")
    prin2=pygame.image.load("wizar2t.png")
    prin3=pygame.image.load("wizar3t.png")
    prin4=pygame.image.load("wizar4t.png")
    prin5=pygame.image.load("wizar5t.png")
    prin6=pygame.image.load("wizar6t.png")
    
    cala=pygame.image.load("balaw.png")
    Cañon=pygame.image.load("cañon.png")
    info2=pygame.image.load("vida.png")
    escu=pygame.image.load("escudo.png")
    oscuridad=pygame.image.load("oscuridad.png")
    oscuridad2=pygame.image.load("oscuridad2.png")
    JugadorA = pygame.image.load('animaciones.png')
    cubrir=pygame.mixer.Sound("Cubrir.wav")
    disp=pygame.mixer.Sound("disp.wav")
    fuente_J=pygame.font.Font(None,32)
    fuente_K=pygame.font.Font(None,64)
    jugadores=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    bloques_2=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    balas_r=pygame.sprite.Group()
    balas_M=pygame.sprite.Group()
    chalecos=pygame.sprite.Group()

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
                    while f_key < 6 :
                        if f_key==0:
                            ventana.blit(prin,[0,0])
                            pygame.display.flip()
                        if f_key==1:
                            ventana.blit(prin2,[0,0])
                            pygame.display.flip()
                        if f_key==2:
                            ventana.blit(prin3,[0,0])
                            pygame.display.flip()
                        if f_key==3:
                            ventana.blit(prin4,[0,0])
                            pygame.display.flip()
                        if f_key==4:
                            ventana.blit(prin5,[0,0])
                            pygame.display.flip()
                        if f_key==5:
                            ventana.blit(prin6,[0,0])
                            pygame.display.flip()
                        time.sleep(7)
                        f_key+=1
                    fin_prev=True
                    aux=int (0)
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
            ivan="Ivan Dario Gallego Grisales"
            jhon="Jhon Alberto Garcia"
            riaño="Daniel Antonio Riaño"
            profesor="Carlos Andres Lopes " 
            utp=" UTP "
            municion=fuente_J.render(mun,True,BLANCO)
            ventana.blit(municion,[620,100])
            municion=fuente_J.render(ivan,True,BLANCO)
            ventana.blit(municion,[540,200])
            municion=fuente_J.render(jhon,True,BLANCO)
            ventana.blit(municion,[590,300])
            municion=fuente_J.render(riaño,True,BLANCO)
            ventana.blit(municion,[580,400])
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
    msc=pygame.mixer.Sound("castle.wav")
    maqu=pygame.image.load("Rival2.png")
    fondo=pygame.image.load("mapa1.png")
    oscuridad=pygame.image.load("oscuridad.png")
    torres=pygame.sprite.Group()
    maquina_1=pygame.sprite.Group()
    bloques=mapa1(bloques)
    j.bloques=bloques
    t=Rival_E([924,169],Cañon)
    torres.add(t)
    t2=Rival_E([1324,400],Cañon)
    torres.add(t2)
    t3=Rival_E([1324,1538],Cañon)
    torres.add(t3)
    t4=Rival_E([2362,696],Cañon)
    torres.add(t4)
    t5=Rival_E([3210,540],Cañon)
    torres.add(t5)
    c=Chaleco([369,1480],escu)
    chalecos.add(c)
    aux=20
    M=Maquina_1([3311,377],maqu)
    maquina_1.add(M)
    
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
                    b=Bala([p[0]-25,p[1]],cala)
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
        for c in maquina_1:
            c.f_velx=f_velx
            c.f_vely=f_vely


            
        #Colision
        
        

                
        #manejo de Torres primer enemigo estatico         
        for b in torres:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    torres.remove(b)
                    
            if b.tmp < 0:
                pos=[b.rect.x,b.rect.y]
                s=Bala(pos,cala)
                s.velx=-10
                balas_r.add(s)
                b.tmp=random.randrange(20,90)
        #manejo de la maquina
                
        for b in maquina_1:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_M1-=1
                if b.vida_M1==0:
                    maquina_1.remove(b)
                    fin_Nivel_1=True
                    msc.stop()
                    j.vida=20
            if (b.rect.x<=3311+f_posx):
                b.velx=4
            if (b.rect.x>=3893+f_posx):
                b.velx=-4
            
                
        #Limpieza de memoria
        for b in balas:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, bloques, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas.remove(b)
            for r in ls_colision:
                balas.remove(b)
                
        for b in balas_r:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, jugadores, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas_r.remove(b)
            for r in ls_colision:
                j.vida-=2
                balas_r.remove(b)
                
        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, chalecos, True)
        for e in ls_colision:
            j.aumen=2

        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, maquina_1, False)
        for e in ls_colision:
            j.vida-=2


        # fin de juego

        for j in jugadores:
            if j.vida < 1:
                fin_Nivel_1= True
                fin_Nivel_2= True
                
    
       
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
        chalecos.update()
        balas.update()
        balas_r.update()
        torres.update()
        maquina_1.update()
        ventana.blit(fondo,[f_posx,f_posy])
        if(j.escudo==True):
           ventana.blit(escu,[j.rect.x-60,j.rect.y-70])
           cubrir.play()
        

        n=M.rect.x
        for i in range(M.vida_M1):
            ventana.blit(info2,[n-M.vida_M1,M.rect.y-20])
            n=n+2
            
        jugadores.draw(ventana)
        balas.draw(ventana)
        ventana.blit(municion,[620,3])
        ventana.blit(nivel,[1000,3])
        balas_r.draw(ventana)
        chalecos.draw(ventana)
        maquina_1.draw(ventana)
        #bloques.draw(ventana)
        torres.draw(ventana)
        ventana.blit(oscuridad,[0,0])
        x=10
        for i in range(j.vida):
            ventana.blit(info2,[x,10])
            x=x+20
        pygame.display.flip()
        reloj.tick(40)
#nivel 2
    msc=pygame.mixer.Sound("segundo.wav")
    f_posx=0
    f_velx=0
    f_posy=0
    f_vely=0
    j.rect.x=20
    j.rect.y=20
    maqu=pygame.image.load("maquina_2.png")
    maquina_2=pygame.sprite.Group()
    M2=Maquina_2([3311,154],maqu)
    maquina_2.add(M2)
    fondo=pygame.image.load("mapa3.png")
    bloques=mapa2(bloques_2)
    j.bloques=bloques
    msc.play(1)
    while (not fin)and fin_Nivel_1==True and (not fin_Nivel_2):
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
                if event.key == pygame.K_q and j.aumen==2:
                    j.escudo=True
                    aux=j.vida
                    
                if event.key == pygame.K_w and j.vely==0 and j.velx==0:
                    j.vely=0
                    if f_posy>=0:
                        f_vely=0
                    else:
                        f_vely=5
                        
                if event.key == pygame.K_s and j.vely==0 and j.velx==0:
                    j.vely=0
                    if f_posy<=-1200:
                        f_vely=0
                    else:
                        f_vely=-5
                if event.key == pygame.K_e:
                    p=j.RetPos()
                    b=Bala([p[0]-25,p[1]],cala)
                    if j.Direc==1:
                        b.velx= 10
                        balas.add(b)
                    if j.Direc==0:
                        b.velx= -10
                        balas.add(b)
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
            fin_Nivel_2=True
            j.vida=0
            
        if j.rect.y > limv_alt:
            fin_Nivel_2=True
            j.vida=0
            
        if j.rect.x < 0:
            fin_Nivel_2=True
            j.vida=0
            
        if j.rect.y < 0:
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
            
        for c in maquina_2:
            c.f_velx=f_velx
            c.f_vely=f_vely
                
        #manejo de Torres primer enemigo estatico         
        for b in torres:
            
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_T-=1
                if b.vida_T==0:
                    torres.remove(b)
                    
            if b.tmp < 0:
                pos=[b.rect.x,b.rect.y]
                s=Bala(pos,cala)
                s.velx=-10
                balas_r.add(s)
                disp.play()
                b.tmp=random.randrange(20,90)
        #manejo de maquina
        for b in maquina_2:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, balas, True)
            for r in ls_colision:
                b.vida_M2-=1
                if b.vida_M2==0:
                    maquina_2.remove(b)
                    fin_Nivel_2=True
                    msc.stop()
                    
            if (b.rect.y<=154+f_posy):
                b.vely=1
            if (b.rect.y>=800+f_posy):
                b.vely=-1

            if b.tmp < 0:
                pos=[b.rect.x,b.rect.y]
                s=Bala(pos,cala)
                s.velx=-10
                balas_M.add(s)
                b.tmp=random.randrange(20,90)
            

            
                
        #Limpieza de memoria
        for b in balas:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, bloques, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas.remove(b)
            for r in ls_colision:
                balas.remove(b)
                
        for b in balas_r:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, jugadores, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas_r.remove(b)
            for r in ls_colision:
                j.vida-=2
                balas_r.remove(b)
                
        for b in balas_M:
            ls_colision=pygame.sprite.pygame.sprite.spritecollide(b, jugadores, False)
            if b.rect.x > ANCHO+2 or b.rect.x <-2:
                balas_M.remove(b)
            for r in ls_colision:
                j.vida-=2
                balas_M.remove(b)
                
        ls_colision=pygame.sprite.pygame.sprite.spritecollide(j, chalecos, True)
        for e in ls_colision:
            j.aumen=2

        # fin de juego

        for j in jugadores:
            if j.vida < 1:
                fin_Nivel_2= True
                msc.stop()
    
       
        #Refresco
       
        
        
        #ventana.fill(NEGRO)
        f_posx += f_velx
        f_posy += f_vely
        bloques.update()
        mun=" " + str(tiempo)
        municion=fuente_J.render(mun,True,BLANCO)
        Nivel=" Nivel 2"
        nivel=fuente_J.render(Nivel,True,ROJO)
        jugadores.update()
        chalecos.update()
        balas.update()
        balas_r.update()
        balas_M.update()
        torres.update()
        maquina_2.update()
        ventana.blit(fondo,[f_posx,f_posy])
        
        if(j.escudo==True):
           ventana.blit(escu,[j.rect.x-60,j.rect.y-70])
           cubrir.play()
        
        

        n=M2.rect.x
        for i in range(M2.vida_M2):
            ventana.blit(info2,[n-10,M2.rect.y-20])
            n=n+2
            
        maquina_2.draw(ventana)
        jugadores.draw(ventana)
        balas.draw(ventana)
        ventana.blit(municion,[620,3])
        balas_r.draw(ventana)
        balas_M.draw(ventana)
        chalecos.draw(ventana)
        #bloques.draw(ventana)
        torres.draw(ventana)
        ventana.blit(oscuridad2,[0,0])
        x=10
        ventana.blit(nivel,[1000,3])
        for i in range(j.vida):
            ventana.blit(info2,[x,10])
            x=x+20
        pygame.display.flip()
        reloj.tick(40)
                
#Final del juego
    msc.stop()
    aux=0
    if aux==0:
        aux=tiempo
    fondo=pygame.image.load("game_over.jpg")
    while (not fin)and fin_Nivel_1==True and fin_Nivel_2==True:
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
        
        

