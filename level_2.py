import pygame
import random

game_width=512
game_height=512

plat_size=32
start_x=512/2 -16
start_y=448
vx=2
vy=2

class Plat(pygame.Rect):
    def __init__(self,x,y):
        pygame.Rect.__init__(self,x,y,plat_size,plat_size)
        self.status=[]
        self.counter=0
        self.maxcount_x=0
        self.maxcount_y=0
        self.vx=vx
        self.vy=vy

def create_map():
    platforms=[]
    #start platform-done
    for i in range(2):
        plat=Plat((224+plat_size*i),480)
        platforms.append(plat)

    #above start 
    for i in range(2):
        plat=Plat(224+(i*plat_size),390) 
        platforms.append(plat)

    #first jump-done
    for i in range(2):
        plat=Plat(0+i*plat_size,390)
        platforms.append(plat)
        plat=Plat(448+i*plat_size,390)
        platforms.append(plat)

    #second jump-done
    for i in range(4):
        plat=Plat(192+i*plat_size,310)
        platforms.append(plat)

    #third jump
    for i in range(2):
        plat=Plat(0+i*plat_size,270)
        platforms.append(plat)
        plat=Plat(448+i*plat_size,270)
        platforms.append(plat)

    #fourth jump
    for i in range(4):
        plat=Plat(192+i*plat_size,200)
        platforms.append(plat)

    #fifth jump
    for i in range(2):
        plat=Plat(0+i*plat_size,150)
        platforms.append(plat)
        plat=Plat(448+i*plat_size,150)
        platforms.append(plat)
    
    #seperation wall
    for i in range(2):
        for j in range(9):
            plat=Plat(224+(i*plat_size),300-(j*plat_size)) 
            platforms.append(plat)
    
    #invis
    for i in range(20):
        plat=Plat(0+i*plat_size,32)
        plat.status.append("invis")
        platforms.append(plat)

    #win block
    for i in range(2):
        plat=Plat(224+i*plat_size,0)
        plat.status.append("win")
        platforms.append(plat)

    for i in range(1):
        plat=Plat(0+i*plat_size,512)
        plat.status.append('invis')
        platforms.append(plat)
    
    return platforms

coord1=[(0,358),(0,238),(0,118)]
coord2=[(480,358),(480,238),(480,118)]
def trick(player):
    if (player.x,player.y) in coord1:
        num=random.randint(0,2)
        player.x=coord2[num][0]+1
        player.y=coord2[num][1]

    if (player.x,player.y) in coord2:
        num=random.randint(0,2)
        player.x=coord1[num][0]+1
        player.y=coord1[num][1]
        
    if player.x==0 and player.y==480:
        player.x=0
        player.y=0
