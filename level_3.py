import pygame
# from sys import exit

# pygame.init()

""" for diagnoal plat is vx=1 and vy=3 steep if vx=3 and vy=1 u get shallow """
game_width=1024
game_height=600
plat_size=32
start_x=68
start_y=518
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
    #start platform
    for i in range(2):
        plat=Plat((70+plat_size*i),550)
        platforms.append(plat)
    #platfrom 1
    for i in range(1):
        plat=Plat(300-(i*plat_size),500) 
        platforms.append(plat)
    #diagonal moving platform
    for i in range(3):
        plat=Plat(125+i*plat_size,300)
        plat.status.extend(["move_h","move_v"])
        plat.maxcount_x=40
        plat.vx=1
        plat.vy=3
        plat.maxcount_y=40
        platforms.append(plat)
    
    #vertical moving platform
    for i in range(3):
        plat=Plat(32+i*plat_size,250)
        platforms.append(plat)
    
    for i in range(3):
        plat=Plat(150+i*plat_size,128)
        plat.status.extend(["move_v","invis"])
        plat.maxcount_y=30
        platforms.append(plat)
    
    for i in range(3):
        plat=Plat(320+i*plat_size,128)
        plat.status.append("death")
        platforms.append(plat)
    
    for i in range(3):
        plat=Plat(320+i*plat_size,32)
        plat.status.append("invis")
        platforms.append(plat)
    
    for i in range(3):
        plat=Plat(32+i*plat_size,32)
        plat.maxcount_y=40
        plat.status.extend(["invis",'move_v'])
        platforms.append(plat)
    
    for i in range(1):
        plat=Plat(450,550)
        plat.status.append("invis")
        platforms.append(plat)

    #second half
    #done
    for i in range(2):
        plat=Plat(548+i*plat_size,550)
        plat.status.append("move_h")
        plat.maxcount_x=30
        platforms.append(plat)
    #done
    for i in range(3):
        plat=Plat(700+i*plat_size,500)
        platforms.append(plat)
    #done
    for i in range(3):
        plat=Plat(764,500-i*plat_size)
        platforms.append(plat)
    #done
    for i in range(3):
        plat=Plat(600+i*plat_size,400)
        platforms.append(plat)
    #done
    for i in range(3):
        plat=Plat(500+i*plat_size,250)
        plat.status.extend(["move_v","death"])
        plat.maxcount_y=50
        platforms.append(plat)
    
    #done
    for i in range(3):
        plat=Plat(900+i*plat_size,200)
        plat.status.append("death")
        platforms.append(plat)

    #done
    for i in range(3):
        plat=Plat(860+i*plat_size,350)
        platforms.append(plat)
    
    #done
    for i in range(3):
        plat=Plat(700+i*plat_size,220)
        plat.status.extend(["move_v","move_h"])
        plat.maxcount_x=30
        plat.maxcount_y=30
        platforms.append(plat)

    #done
    for i in range(3):
        plat=Plat(600+i*plat_size,180)
        platforms.append(plat)

    for i in range(3):
        plat=Plat(800+i*plat_size,100)
        platforms.append(plat)
    
    #win block
    for i in range(1):
        plat=Plat(450,50)
        plat.status.append("win")
        platforms.append(plat)
    
    for i in range(17):
        for j in range(19):
            plat=Plat(482+i*plat_size,0+j*plat_size)
            plat.status.append("cover")
            platforms.append(plat)
    
    return platforms

def relocate_win_3(plat):
    plat.x=950
    plat.y=32

def trick(player,plat):
    if plat.colliderect(plat.inflate(10,10))or player.colliderect(plat):
        relocate_win_3(plat)
        return False

