import pygame
from Player import player
from Terrain import terrain
from MainMenu import menu
from Leaderboard import leaderboard_read, leaderboard_write
from LoadImage import load_image
from PS4 import ps4_config, ps4_button, ps4_hat, ps4_joystick

# initialize game and call classes
pygame.init()
player = player()
terrain = terrain()
menu = menu()

# Name of game
pygame.display.set_caption('First Game')

# PS4 controller configuration
button_layout, dpad_layout = ps4_config()

'''
Game start menu
'''
run_game = False
while menu.run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            menu.run = False
        # load_image(filename, pos_x, pos_y, width, height)
        load_image('menu\selection_screen.jpg', 0, 0, terrain.screen_size[0], terrain.screen_size[1])
        start_game = load_image('menu\Start_game.png', menu.options_pos_x, menu.options_pos_y[0], 400, 100)
        high_score = load_image('menu\High_score.png', menu.options_pos_x, menu.options_pos_y[1], 400, 100)
        open_credits = load_image('menu\Credits.png', menu.options_pos_x, menu.options_pos_y[2], 400, 100)
        exit_game = load_image('menu\Quit.png', menu.options_pos_x, menu.options_pos_y[3], 400, 100)
        
        # Main menu game options
        pygame.mouse.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if start_game.collidepoint(x, y):
                print('Starting Game...')
                menu.options = 'Start Game'
                menu.run = False
                run_game = True
            elif high_score.collidepoint(x, y):
                print('Launching High Scores...')
                menu.options = 'High Score'
            elif open_credits.collidepoint(x, y):
                print('Launching Credits...')
                menu.options = 'Credits'
            elif exit_game.collidepoint(x, y):
                print('Exitting Game...')
                menu.options = 'Exit Game'
                menu.run = False
     
    # Begin player selection
    if menu.options == 'Start Game':
        menu.run = False
        run_game = True
        '''Uncomment and change above run flags to turn on player selection
        # Background Screen for player selection
        screen_position = terrain.env.get_rect().move(-player.start_x-player.vel, 0)
        terrain.env.blit(terrain.backdrop, screen_position)
        
        keys = pygame.key.get_pressed()
        # Plater selected
        if keys[pygame.K_RETURN]:
            menu.run = False
            run_game = True
        # Switch players to the right
        if keys[pygame.K_LEFT] | keys[ord('a')]:
            menu.switch_flag = 'Left'
            menu.player_counter = menu.player_switch()
    
        # Switch players to the right
        if keys[pygame.K_RIGHT] | keys[ord('d')]:
            menu.switch_flag = 'Right'
            menu.player_counter = menu.player_switch()
        
        menu.select_player(menu.player_counter)
        '''
    elif menu.options == 'High Score':
        l = leaderboard_read('high_score.txt')
        print(l)
        menu.options = 'Null'
    elif menu.options == 'Credits':
        print('Author: Neeve Kadosh\nDate: 18 April 2020')
        menu.options = 'Null'

    pygame.display.update() 

'''
Main game loop
'''
while run_game:
    pygame.time.delay(100)
    
    # Move using arrow or adws keys
    keys = pygame.key.get_pressed()
    hat = ps4_hat()
    joystick = ps4_joystick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
    # Jumping
    if ((ps4_button(button_layout['TRIANGLE']) | keys[pygame.K_UP]  | keys[ord('w')]) 
                            & player.hold_flag == True) | player.in_air_flag == True:
        player.jump_flag = True
        player.jump_up()
    elif player.jump_flag == True:
        player.jump_down()
    else:
        player.jump_cycle_images = 0
    
    # Move left
    if (hat == dpad_layout['DPAD_LEFT']) | (joystick < -0.7) | keys[pygame.K_LEFT] | keys[ord('a')]:
        player.move_left()
    # Moveright
    if (hat == dpad_layout['DPAD_RIGHT']) | (joystick > 0.7) | keys[pygame.K_RIGHT] | keys[ord('d')]:
        player.move_right()
    # Crouch
    if keys[pygame.K_DOWN] | keys[ord('s')]:
        player.sit_flag = True
    # Punch
    if ps4_button(button_layout['X']) | (keys[ord('f')] & ~keys[pygame.K_LSHIFT]):
        player.punch_flag = True
        player.finished_punching_flag = False
    # Kick
    if ps4_button(button_layout['SQUARE']) | keys[ord('e')]:
        player.kick_flag = True
        player.finished_kicking_flag = False
    # Combo Punch
    if ps4_button(button_layout['O']) | (keys[ord('f')] & keys[pygame.K_LSHIFT]):
        player.combo_punch_flag = True
        player.finished_combo_punching_flag = False
        
    # Check direction and if or if not idleqqqq
    if player.idle_flag == True:
        player.idle()
    # Player walking cycle
    else:
        player.walk()
    player.idle_flag = True
    
    # Character sitting
    if player.sit_flag == True:
        player.sit()
    player.sit_flag = False
    
    # Punching
    if player.punch_flag == False | player.finished_punching_flag == False:
        player.finished_punching_flag, player.punch_cycle_images = player.attack(player.punch_images, player.punch_cycle_images, player.finished_punching_flag)
    player.punch_flag = False
    
    # Kicking
    if player.kick_flag == False | player.finished_kicking_flag == False:
        player.finished_kicking_flag, player.kick_cycle_images = player.attack(player.kick_images, player.kick_cycle_images, player.finished_kicking_flag)
    player.kick_flag = False
    
    # Combo punching
    if player.combo_punch_flag == False | player.finished_combo_punching_flag == False:
        player.finished_combo_punching_flag, player.combo_punch_cycle_images = \
            player.attack(player.combo_punch_images, player.combo_punch_cycle_images, player.finished_combo_punching_flag)
    player.combo_punch_flag = False
    
    # Loading jump image if in the air
    if player.jump_flag == True | player.in_air_flag == True:
        player.load_jump_image()

    
    # Press Q to exit game
    if ps4_button(button_layout['OPTIONS']) | keys[ord('q')]:
        run_game = False
    
    # Game animation to move player and update terrain
    player.action = pygame.transform.scale(player.action, (player.width, player.height))
    if player.x < 0:
        map_position = terrain.env.get_rect().move(0, 0)
    elif player.x-player.vel > terrain.screen_width:
        map_position = terrain.env.get_rect().move(terrain.screen_width, 0)
    else:
        map_position = terrain.env.get_rect().move(-player.x-player.vel, 0)
    terrain.env.blit(terrain.backdrop, terrain.perimeter)#map_position)
    position = player.action.get_rect().move(player.x, player.y)
    terrain.env.blit(player.action, position)
    pygame.display.update() 
    
pygame.quit()