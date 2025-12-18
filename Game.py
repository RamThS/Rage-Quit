def run_game():
    import pygame
    from sys import exit#terminates the program
    import level_1
    import level_2
    import level_3

    pygame.init()#starts the game

    level=[level_1,level_2,level_3]
    level_count=0
    level_clear=False
    level_trick=True
    cover_rem=False


    player_X=98
    player_Y=416
    player_width=32
    player_height=32
    player_distance=5
    player_dead=False

    player_velocity_y=-10
    player_velocity_x=5
    gravity=0.5
    friction=0.5

    plat_size=32
    platform_velocity_x=2

    player_img=pygame.image.load("square-and-circle.png")#loads image
    player_img=pygame.transform.scale(player_img,(player_width,player_height))#scale images 

    window=pygame.display.set_mode((level[level_count].game_width,level[level_count].game_height))#setting size of window

    pygame.display.set_caption("Rage Quit")#setting title
    clock=pygame.time.Clock()#for frame rate

    class Player(pygame.Rect):
        def __init__(self):
            pygame.Rect.__init__(self,player_X,player_Y,player_width,player_height)
            self.velocity_y=0
            self.velocity_x=0
            self.jumping=False
            self.direction="right"
            self.image=player_img

    def check_collision():
        for plat in platforms:
            if player.colliderect(plat):    
                return plat
        return None

    def check_collision_x():
        plat=check_collision()
        if plat is not None:
            nonlocal level_trick,level_clear,player_dead
            if "win" in plat.status:
                if level[level_count]==level_1 :
                    if  level_trick:
                        level_trick=False
                        level_clear=level_1.trick1(player,plat)
                        return
                    else :
                        level_clear=True
                        return
                if level[level_count]==level_3:
                    if level_trick:
                        level_trick=False
                        level_clear=level_3.trick(player,plat)
                        return
                    else:
                        level_clear=True
                        return
                level_clear=True

            if "death" in plat.status:
                player_dead=True  

            if player.velocity_x<0:
                player.x=plat.x+plat.width
            elif player.velocity_x>0:
                player.x=plat.x-player.width
            player.velocity_x=0

    def check_collision_y():
        plat=check_collision()
        if plat is not None:
            nonlocal level_trick,level_clear,player_dead
            if "win" in plat.status:
                if level[level_count]==level_1:
                    if  level_trick:
                        level_trick=False
                        level_clear=level_1.trick1(player,plat)
                        return
                    else:
                        level_clear=True
                        return
                if level[level_count]==level_3:
                    if level_trick:
                        level_trick=False
                        level_clear=level_3.trick(player,plat)
                        return
                    else:
                        level_clear=True
                        return
                level_clear=True

            if "death" in plat.status:
                player_dead=True

            if player.velocity_y<0:
                player.y=plat.y+plat.height
            elif player.velocity_y>0:
                player.y=plat.y-player.height
                player.jumping=False
            player.velocity_y=0
        
    def load_level(i):
        player.x=level[i].start_x
        player.y=level[i].start_y
        player.velocity_x=0
        player.velocity_y=0
        window=pygame.display.set_mode((level[level_count].game_width,level[level_count].game_height))
        return level[i].create_map()

    def move():
        #X movement
        if player.direction=="left" and player.velocity_x<0:
            player.velocity_x+=friction
        elif player.direction=="right" and player.velocity_x>0:
            player.velocity_x-=friction
        else:
            player.velocity_x=0

        player.x+=player.velocity_x
        if player.x<0:
            player.x=0
        elif player.x+player.width>level[level_count].game_width:
            player.x=level[level_count].game_width-player.width
        
        check_collision_x()

        #Y movement
        player.velocity_y+=gravity
        player.y+=player.velocity_y
        check_collision_y()

    def vertical_platform_movement():
        plat=check_collision()
        if plat is not None:
            if "move_v" in plat.status:
                player.y+=plat.vy

    def draw():
        window.fill((100,100,100))#setting bg as black 
        window.blit(player.image,player)
        for plat in platforms:
            if "win" in plat.status and "cover" not in plat.status:
                pygame.draw.rect(window,(255, 215, 0),plat)
                continue
            if 'invis' in plat.status and "cover" not in plat.status:
                pygame.draw.rect(window,(100,100,100),plat)
                continue
            if "cover" in plat.status:
                pygame.draw.rect(window,(100,100,100),plat)
                continue

            pygame.draw.rect(window,(50,200,50),plat)#draws the thing swhere to draw,colour,what are specifications
        
        pygame.display.update()

    def move_plat():
        for plat in platforms:
            if "move_h" in plat.status :
                plat.x+=plat.vx
            if 'move_v' in plat.status:
                plat.y+=plat.vy
                vertical_platform_movement()
            plat.counter+=1
            if ("move_h" in plat.status and plat.counter > plat.maxcount_x) or ("move_v" in plat.status and plat.counter > plat.maxcount_y):
                if "move_h" in plat.status:
                    plat.vx*= -1
                if "move_v" in plat.status:
                    plat.vy*=-1
                plat.counter=0

    def death(player):
        nonlocal cover_rem,level_trick,player_dead,platforms
        if player.y>=level[level_count].game_height or player_dead:
            if cover_rem:
                cover_rem=False
                level_trick=True
                platforms.clear()
                platforms=load_level(level_count)
                return
            level_trick=True
            player.x=level[level_count].start_x
            player.y=level[level_count].start_y
            player_dead=False

    #start game
    player =Player()
    platforms=load_level(level_count)#specification of platofrom x y width height

    while True:

        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()#quits the game
                exit()
        
        keys=pygame.key.get_pressed()
        if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE] )and not player.jumping:
            player.velocity_y=player_velocity_y
            player.jumping=True

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.velocity_x=player_velocity_x
            player.direction="right"

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.velocity_x=-player_velocity_x
            player.direction="left"
        
        if level[level_count]==level_2:
            level_2.trick(player)
        
        if level[level_count]==level_3:
            
            if not level_trick:
                for plat in platforms:
                    if "cover" in plat.status:
                        cover_rem=True
                        platforms.remove(plat)

        if level_clear:
            level_clear=False
            level_count+=1
            level_trick=True
            if level_count >=len(level):
                pygame.quit()
                exit()
            platforms.clear()
            platforms=load_level(level_count)

        move_plat()
        move()
        death(player)
        draw()
        clock.tick(60)#framerate is 60

