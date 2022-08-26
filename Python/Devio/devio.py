from itertools import count
import pygame
import random
import math
from modules import Map_module
from settings import *
from modules.player import Player
whos_playing_data = {
    'lives': 5
}
whos_playing = Player(whos_playing_data)

def generate_end(x,y):
    end_data = {
        'id': -2,
        'x_value': x,
        'y_value': y,
        'img': END_DOOR,
        'type': 'end_door'
    }
    return Map_module.Object(end_data)

def generate_obj(x,y,type):
    if type == "brick":
        brick_data = {
            'id': -2,
            'x_value': x,
            'y_value': y,
            'img': BRICK,
            'type': 'brick'
        }
        return Map_module.Object(brick_data)
    if type == "stone":
        brick_data = {
            'id': -2,
            'x_value': x,
            'y_value': y,
            'img': STONE,
            'type': 'stone'
        }
        return Map_module.Object(brick_data)
    if type == "spikeybrick":
        brick_data = {
            'id': -2,
            'x_value': x,
            'y_value': y,
            'img': SPIKEY_BRICK,
            'type': 'spikeybrick'
        }
        return Map_module.Object(brick_data) 
        
    

def generate_enemy(x,y,type,id):
    if type == "turtle":
        enemy_data = {
            'id': id,
            'x_value': x,
            'y_value': y,
            'type': type,
            'img': TURTLE
        }
        enemy = Map_module.Entity(enemy_data)
        enemy.velocity = 2
        enemy.direction = "left"
        return enemy
    if type == "angrybrick":
        enemy_data = {
            'id': id,
            'x_value': x,
            'y_value': y,
            'type': type,
            'img': ANGRY_BRICK
        }
        enemy = Map_module.Entity(enemy_data)
        enemy.jump_power = 110
        return enemy
    if type == "jumperguy":
        enemy_data = {
            'id': id,
            'x_value': x,
            'y_value': y,
            'type': type,
            'img': JUMPER_GUY
        }
        enemy = Map_module.Entity(enemy_data)
        enemy.jump_power = 110
        enemy.velocity = 2
        return enemy
        
    
    
def generate_edit_grid():
    grid_blocks_instance = []
    for x in range(20):
        for y in range(8):
            grid_data = {
                'id': -10,
                'type': "edit_grid",
                'x_value': x*50,
                'y_value': y*50,
                'img': EDIT_BLOCK
            }
            grid_block = Map_module.Object(grid_data)
            grid_blocks_instance.append(grid_block)
            # print(f"x: {x} y: {y}")
    return grid_blocks_instance

def collide_x(obj1,obj2,offset):
    offset_x = obj2.x - (obj1.x + offset)
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x,offset_y)) != None



def game(level):
    SOUNDTRACK = pygame.mixer.music.load("assets/sounds/Devio_background_harp.wav")
    pygame.mixer.music.play()
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    countdown = 60
    timer = 0
    main_font = pygame.font.SysFont('comicsans', 20)
    end_font = pygame.font.SysFont('comicsans', 80)
    ground = []
    grid_blocks = []
    lost = False
    won = False
    x_offset = 0
    x_previous =0
    y_previous = 0
    GODMODE = False
    pause_count = 0
    edit_selector = "brick"
    angry_counter = 0

    player_data = {
        'id': -1,
        'x_value': 450,
        'y_value': 300,
        'img': DEVIO,
        'type': 'player'
    } # make DEVIO with player_data-------------------
    player = Map_module.Entity(player_data)
    player.jump_power = 125
    player.velocity = 5
    #----------------------------------------------REDRAW WINDOW---------------
    def redraw_window():
        WIN.blit(SKY,(0,0))
        for ground_block in ground:
            ground_block.draw(WIN,0)

        for enemy in map.map_entities:
            enemy.draw(WIN,x_offset)
        for brick in map.map_items:
            brick.draw(WIN,x_offset)
        if GODMODE:
            for grid_block in grid_blocks:
                grid_block.draw(WIN,0)

        #draw countdown timer and number of lives
        countdown_label = main_font.render(f"Time Remaining: {countdown}",1,(155,155,255))
        score_label = main_font.render(f"Score: {whos_playing.score}",1,(155,155,155))
        lives_label = main_font.render(f"Lives: {whos_playing.lives}",1,(155,155,155))
        WIN.blit(lives_label, (10,10))
        WIN.blit(score_label, (WIDTH/2 - score_label.get_width()/2, 10))
        WIN.blit(countdown_label, (WIDTH - countdown_label.get_width()-10,10))
        
        player.draw(WIN,0)

        if lost:
            lost_label = end_font.render("You Lost",1,(255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2, 200))
        if won:
            won_label = end_font.render("You Won!!!",1,(255,255,255))
            WIN.blit(won_label, (WIDTH/2 - won_label.get_width()/2, 200))
        pygame.display.update()
    #------------------------------------ END REDRAW WINDOW--------------------

    map = Map_module.Map.load_map_by_name(level)
    
    #this will make random turtles that wont save to the DB to keep things interesting!
    enemy_turtle_count = 4
    for i in range(enemy_turtle_count):
        valid_placement = True
        new_enemy = generate_enemy(random.randrange(500,5000),random.randrange(0,FLOOR-50),'turtle',-3)
        if collide_x(new_enemy,player,x_offset):
            valid_placement = False
        for brick in map.map_items:
            if collide_x(brick,new_enemy, x_offset):
                valid_placement= False
        if valid_placement == True:
            map.map_entities.append(new_enemy)
                                                        #| window |
    ground_count = 3 #sets the ground like this:  ground | ground | ground... if you move too far one way or another it moves the invisible ground in front of the direction you are moving so you will always see ground with only 3 images
    for i in range(ground_count):
        ground_data = {
            'id': -1,
            'x_value': (i*WIDTH-WIDTH),
            'y_value': FLOOR,
            'img': GROUND,
            'type': "ground"
        }
        ground_block = Map_module.Object(ground_data)
        ground.append(ground_block)

    
        
    #Game Loop----------------------------------------------------------------
    while run:
        redraw_window()
        clock.tick(FPS)

        #adjust countdown timer
        timer += 1
        if timer == FPS:
            if countdown > 0:
                countdown -=1
            timer = 0
        
        if whos_playing.lives <= 0 or countdown <= 0:
            lost = True
            pause_count += 1
            
        if lost:
            if pause_count > FPS * 3:
                whos_playing.lives -=1
                run = False
                pygame.mixer.music.load("assets/sounds/music.mp3")
                pygame.mixer.music.play()
            else:
                continue #pauses the game for 3 seconds and won't go below
        if won:
            pause_count += 1
            if pause_count > FPS *3:
                whos_playing.levels_won.append(map.name)
                run = False
                pygame.mixer.music.load("assets/sounds/music.mp3")
                pygame.mixer.music.play()
            else:
                continue
        if whos_playing.score > 1000:
            whos_playing.score -= 1000
            whos_playing.lives +=1
        keys = pygame.key.get_pressed()       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            # THIS WILL ALLOW YOU TO ADD OR REMOVE map.map_items AS LONG AS GODMODE IS ACTIVE
            if GODMODE:
                countdown = 60
                if event.type == pygame.MOUSEBUTTONUP:
                    (click_x, click_y)= pygame.mouse.get_pos()
                    # (click_x, click_y) = pos
                    print(f'clicked x: {click_x} clicked y: {click_y}')
                    
                    if event.button == 3:
                        for brick in map.map_items:
                            if brick.x + x_offset < click_x and brick.x + x_offset + brick.img.get_width() > click_x and brick.y < click_y and brick.y + brick.img.get_height() > click_y:
                                print(f"Removing brick at: GRID x: {int(brick.x/50)} GRID y: {int(brick.y/50)}")
                                if brick.id > 0:
                                    map.deleted_indexes.append(brick)
                                map.map_items.remove(brick)
                        for enemy in map.map_entities:
                            if enemy.x + x_offset < click_x and enemy.x + x_offset + enemy.img.get_width() > click_x and enemy.y < click_y and enemy.y + enemy.img.get_height() > click_y:
                                print(f"Removing enemy at: GRID x: {int(enemy.x/50)} GRID y: {int(enemy.y/50)}")
                                if enemy.id > 0:
                                    map.deleted_indexes.append(enemy)
                                map.map_entities.remove(enemy)

                    if event.button == 1:
                        if edit_selector == 'brick':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_items.append(generate_obj(block_x - x_offset,block_y, "brick"))
                        if edit_selector == 'turtle':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_entities.append(generate_enemy(block_x - x_offset,block_y,'turtle',-2))
                            print("turtle was turtley enough for the turtle club!")
                        if edit_selector == "level_ending":
                            for item in map.map_items: # removes the old ending location if there was one
                                if item.type == 'end_door':
                                    map.map_items.remove(item)

                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_items.append(generate_end(block_x - x_offset, block_y))
                        if edit_selector == 'stone':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_items.append(generate_obj(block_x - x_offset,block_y, "stone"))
                        if edit_selector == 'angrybrick':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_entities.append(generate_enemy(block_x - x_offset,block_y,'angrybrick',-2))
                        if edit_selector == 'spikeybrick':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_items.append(generate_obj(block_x - x_offset, block_y, "spikeybrick"))
                        if edit_selector == 'jumperguy':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_entities.append(generate_enemy(block_x - x_offset,block_y,'jumperguy',-2))
                        if edit_selector == 'wall':
                            for block in grid_blocks:
                                    if block.x < click_x and block.x + block.img.get_width() > click_x and block.y < click_y and block.y + block.img.get_height() > click_y:
                                        block_x = block.x
                                        block_y = block.y
                                        print(f"GRID x: {int(block.x/50)} GRID y: {int(block.y/50)}")
                            map.map_items.append(generate_obj(block_x - x_offset, block_y, "brick"))
                            map.map_items.append(generate_obj(block_x - x_offset, block_y-50, "brick"))
                            map.map_items.append(generate_obj(block_x - x_offset, block_y-100, "brick"))
                            map.map_items.append(generate_obj(block_x - x_offset, block_y-150, "brick"))
                        
                # SAVE SAVE SAVE SAVE SAVE SAVE SAVE SAVE SAVE SAVE SAVE SAVE SAVE
                if keys[pygame.K_LCTRL] and keys[pygame.K_s]:
                    print("attempting to save level...")
                    map.save_map()
                    GODMODE = False
                
                #layout the edit grid
                if grid_blocks == []:
                    grid_blocks = generate_edit_grid()
                if keys[pygame.K_1]:
                    print("edit_selector set to brick")
                    edit_selector = 'brick'
                if keys[pygame.K_2]:
                    print("edit_selector set to turtle")
                    edit_selector = 'turtle'
                if keys[pygame.K_3]:
                    print("edit_selector set to stone")
                    edit_selector = "stone"
                if keys[pygame.K_4]:
                    print("edit_selector set to angrybrick")
                    edit_selector = "angrybrick"
                if keys[pygame.K_5]:
                    print("edit_selector set to spikeblock")
                    edit_selector = "spikeybrick"
                if keys[pygame.K_6]:
                    print("edit_selector set to jumperguy")
                    edit_selector = "jumperguy"
                if keys[pygame.K_7]:
                    print("edit_selector set to wall")
                    edit_selector = "wall"

                if keys[pygame.K_0]:
                    print("edit_selector set to level ending")
                    edit_selector = 'level_ending'
        # when in edit mode it will keep moving the player until they line up with the grid
        if GODMODE and player.status == "stationary" and x_offset%50 !=0:
                    if player.direction == 'left':
                        x_offset +=player.velocity
                    if player.direction == 'right':
                        x_offset -= player.velocity 
        # if 'g' + 'o' + 'd' are pressed at the same time then activate GODMODE
        if keys[pygame.K_g] and keys[pygame.K_o] and keys[pygame.K_d]:
            if GODMODE == False:
                print("GODMODE activated!")
                GODMODE = True
            
        if x_previous == x_offset  and y_previous == player.y:
            player.status = "stationary"
        if y_previous == player.y and player.status == "jumping":
            player.status = 'walking'
        player.animate(timer)
        x_previous = x_offset
        y_previous = player.y
        if keys[pygame.K_a]: #MOVE LEFT                  (a)
            if player.status != 'jumping':
                player.status = 'walking'
            if player.direction != 'left':
                player.direction = 'left'
                player.img = DEVIO_LEFT_STANDING_1
            x_offset += player.velocity
            for ground_block in ground:
                ground_block.x += player.velocity

            for brick in map.map_items:
                if collide_x(brick,player,x_offset):
                    x_offset -= player.velocity
                    for ground_block in ground:
                        ground_block.x -= player.velocity
                    if brick.type == "end_door":
                        won = True
                    if brick.type == "spikeybrick":
                        DEATH_SOUND.play()
                        countdown = 0

            for enemy in map.map_entities:
                if collide_x(enemy,player,x_offset):
                    countdown = 0
                    DEATH_SOUND.play()
                    map.map_entities.remove(enemy)

        if keys[pygame.K_d]: #MOVE RIGHT                  (d)
            if player.status != 'jumping':
                player.status = 'walking'
            if player.direction != 'right':
                player.direction = 'right'
                player.img = DEVIO_RIGHT_STANDING_1
            x_offset -= player.velocity
            for ground_block in ground:
                ground_block.x -= player.velocity

            for brick in map.map_items:
                if collide_x(brick,player,x_offset):
                    x_offset += player.velocity
                    for ground_block in ground:
                        ground_block.x += player.velocity
                    if brick.type == "end_door":
                        won = True
                    if brick.type == "spikeybrick":
                        countdown = 0
                        DEATH_SOUND.play()

            for enemy in map.map_entities:
                if collide_x(enemy,player,x_offset):
                    # whos_playing.lives -=1
                    countdown = 0
                    DEATH_SOUND.play()
                    map.map_entities.remove(enemy)
                    

        if keys[pygame.K_SPACE]: #  JUMP                  (spacebar)
            if player.grounded == True:
                player.jump_velocity = player.jump_power
                player.grounded = False
                player.status = "jumping"
                JUMP_SOUND.play()
        
        # make the player jump/fall and adjust the map accordingly
        map.map_items,countdown, whos_playing.score = player.jump(map.map_items,x_offset, countdown,whos_playing.score)
        map.map_entities, countdown, whos_playing.score = player.gravity(map.map_items,map.map_entities,x_offset, countdown, whos_playing.score)
        if y_previous != player.y:
            player.status = 'jumping'

        #checks to see if an enemy collides with the player
        for enemy in map.map_entities:
            enemy.move(map.map_items)
            enemy.gravity(map.map_items,map.map_entities,x_offset, countdown,0)
            if collide_x(enemy,player,x_offset):
                countdown = 0
                DEATH_SOUND.play()
                map.map_entities.remove(enemy)
                
            if enemy.type == "angrybrick" or enemy.type == "jumperguy":
                enemy.jump(map.map_items,0,0,0)
                enemy.next_jump -=1
                if enemy.next_jump < 1:
                    enemy.jump_velocity = enemy.jump_power
                    enemy.grounded = False
                    enemy.status = "jumping"
                    enemy.y -= 10
                    enemy.next_jump = random.randrange(2,6) * 60

                
        # 3 ground objects will move front to back so the screen will always see ground as you move
        for ground_block in ground: 
            if ground_block.x < -WIDTH:
                ground_block.x = WIDTH*2
            if ground_block.x > WIDTH*2:
                ground_block.x = -WIDTH
        


#--------------------------------------- MENU CODE---------------------
def get_selection(selection):
    selection1_data = {
        'option': 0,
        'starting_x': 400,
        'starting_y': 120,
        'ending_x': 600,
        'ending_y':120
    }
    if selection == 0:
        return selection1_data

    selection2_data = {
        'option': 1,
        'starting_x': 400,
        'starting_y': 170,
        'ending_x': 600,
        'ending_y':170
    }
    if selection ==1:
        return selection2_data

    selection3_data = {
        'option': 2,
        'starting_x': 400,
        'starting_y': 220,
        'ending_x': 600,
        'ending_y': 220
    }
    if selection == 2:
        return selection3_data

def menu():
    pygame.mixer.music.load("assets/sounds/music.mp3")
    pygame.mixer.music.play()
    menu = True
    main_font = pygame.font.SysFont('comicsans', 40)
    option_font = pygame.font.SysFont('comicsans', 30)
    mini_font = pygame.font.SysFont('comicsans', 20)
    selection = 0
    menu_location = "main menu"
    selection_data = get_selection(selection)
    all_maps = Map_module.Map.list_all_maps()
    level_color = []
    for i in range(3):
        level_color.append((0,255,0))

    def redraw_menu():
        WIN.blit(BLACK_BACKGROUND,(0,0))
        
        if menu_location == 'main menu':
            menu_title = main_font.render(f"Devio Main Menu",1,(100,100,255))
            WIN.blit(menu_title, (WIDTH/2 - menu_title.get_width()/2,10))

            menu_option1 = option_font.render(f"Choose Level",1,(255,255,255))
            WIN.blit(menu_option1, (WIDTH/2 - menu_option1.get_width()/2, menu_title.get_height() + 20))
            
            
            menu_option2 = option_font.render("Settings",1,(255,255,255))
            WIN.blit(menu_option2, (WIDTH/2 - menu_option2.get_width()/2, menu_title.get_height() + menu_option1.get_height() + 30))
            
            menu_option3 = option_font.render(f"Quit",1,(255,255,255))
            WIN.blit(menu_option3, (WIDTH/2 - menu_option3.get_width()/2, menu_title.get_height() + menu_option1.get_height() + menu_option2.get_height() +30))
            
            controls_text = mini_font.render("Controls: w = up, s = down, d = choose selection, a = back",1,(125,125,125))
            WIN.blit(controls_text, (WIDTH/2 - controls_text.get_width()/2, 450))

        if menu_location == "level_selection":
            
            menu_title = main_font.render(f"Level Selection Menu",1,(100,100,255))
            WIN.blit(menu_title, (WIDTH/2 - menu_title.get_width()/2,10))

            for i in range(3): # if the level was already won, it will change the color of the level to indicate its been beeten
                if all_maps[i].name in whos_playing.levels_won:
                    level_color[i] = (100,100,100)

            menu_option1 = option_font.render(f"Level Name: {all_maps[0].name}",1,level_color[0])
            WIN.blit(menu_option1, (WIDTH/2 - menu_option1.get_width()/2, menu_title.get_height() + 20))
            
            menu_option2 = option_font.render(f"Level Name: {all_maps[1].name}",1,level_color[1])
            WIN.blit(menu_option2, (WIDTH/2 - menu_option2.get_width()/2, menu_title.get_height() + menu_option1.get_height() + 30))
            
            menu_option3 = option_font.render(f"Level Name: {all_maps[2].name}",1,level_color[2])
            WIN.blit(menu_option3, (WIDTH/2 - menu_option3.get_width()/2, menu_title.get_height() + menu_option1.get_height() + menu_option2.get_height() +30))
        
        pygame.draw.line(WIN,(255,50,50),(selection_data['starting_x'], selection_data['starting_y']), (selection_data['ending_x'],selection_data['ending_y']),4)
        
        pygame.display.update()


# ------------------- MENU LOOP MENU LOOP MENU LOOP MENU LOOP
    while menu:
        # keys = pygame.key.get_pressed()       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    selection -=1
                    if selection == -1:
                        selection = 2
                if event.key == pygame.K_s:
                    selection +=1
                    if selection == 3:
                        selection = 0
                if event.key == pygame.K_d:
                    if menu_location == "level_selection":
                        game({'name': all_maps[selection].name})
                    if menu_location == "main menu":
                        if selection == 0:
                            menu_location = "level_selection"
                        if selection == 1:
                            menu_location = "settings"
                        if selection == 2:
                            if menu_location == "main menu":
                                menu = False

                if event.key == pygame.K_a:
                    if menu_location == "level_selection":
                        selection = 0
                        menu_location = "main menu"

        selection_data = get_selection(selection)
        redraw_menu()
menu()
#Call the game function to start the game*******************************
# game(LEVEL)
