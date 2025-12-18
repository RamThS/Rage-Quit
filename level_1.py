import pygame

game_width=512
game_height=512

plat_size=32
start_x=440
start_y=452
vx=2
vy=2
platforms=[]

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
    #start platform
    for i in range(4):
        plat=Plat((400+plat_size*i),480)
        platforms.append(plat)

    #platfrom 1
    for i in range(3):
        plat=Plat(300-(i*plat_size),428) 
        platforms.append(plat)
    #platform 2
    for i in range(3):
        plat=Plat(50+i*plat_size,368)
        platforms.append(plat)
    #horizontal moving platform
    for i in range(3):
        plat=Plat(160+i*plat_size,288)
        plat.status.append("move_h")
        plat.maxcount_x=40
        platforms.append(plat)
    #vertical moving platform
    for i in range(2):
        plat=Plat(350+i*plat_size,148)
        plat.status.append("move_v")
        plat.maxcount_y=40
        platforms.append(plat)

    for i in range(3):
        plat=Plat(150+i*plat_size,150)
        plat.status.append("invis")
        platforms.append(plat)

    #win block
    for i in range(1):
        plat=Plat(450,50)
        plat.status.append("win")
        platforms.append(plat)
    return platforms

def relocate_win(plat):
    plat.x=100
    plat.y=100

def trick1(player,plat):
    if player.colliderect(plat.inflate(10, 10)) or player.colliderect(plat): 
        relocate_win(plat)
        return False
        