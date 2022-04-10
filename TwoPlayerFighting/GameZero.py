import pygame
from Player import player
from Terrain import terrain
from MainMenu import menu
from Leaderboard import leaderboard_read, leaderboard_write
from LoadImage import load_image
from Motion import motion
from Collision import collision
import time

# initialize game and call classes
pygame.init()
player_1 = player()
player_2 = player()
terrain = terrain()
menu = menu()
player_2.x = int(terrain.screen_size[0]*0.8)
player_2.direction = 'Left'
# Name of game
pygame.display.set_caption('First Game')

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
        # SP = Select Player
        load_image(menu.sp_background, 0, 0, terrain.screen_size[0], terrain.screen_size[1])
        load_image(menu.sp_text, int(terrain.screen_size[0]*0.4), int(terrain.screen_size[1]*0.1), \
                   int(terrain.screen_size[0]*0.2), int(terrain.screen_size[1]*0.2))
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
        
        menu.select_player(menu.player_counter, 'PLAYER_1')
        menu.select_player(menu.player_counter, 'PLAYER_2')

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
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = True
            
    run_game = motion(player_1, run_game, 'PLAYER_1')
    run_game = motion(player_2, run_game, 'PLAYER_2')
    # Players can jump over each other
    if (player_1.jump_flag == False) & (player_2.jump_flag == False):
        # If the two run into each other
        if abs(player_1.x - player_2.x) < player_1.distance:
            # Case I: Player 1 looking left and Player 2 looking right facing each other
            if (player_1.direction == 'Left') & (player_2.direction == 'Right'):
                if player_1.walking_flag & player_2.walking_flag:
                    player_1.x += player_1.vel
                    player_2.x -= player_2.vel
                elif player_1.walking_flag:
                    player_1.x += player_1.vel
                elif player_2.walking_flag:
                    player_2.x -= player_2.vel
           # Case II: Player 1 looking right and Player 2 looking left facing each other
            elif (player_1.direction == 'Right') & (player_2.direction == 'Left'):
                if player_1.walking_flag & player_2.walking_flag:
                    player_1.x -= player_1.vel
                    player_2.x += player_2.vel
                elif player_1.walking_flag:
                    player_1.x -= player_1.vel
                elif player_2.walking_flag:
                    player_2.x += player_2.vel
            # Case III: Player 1 looking right and Player 2 looking right at the players back
            elif (player_1.direction == 'Right') & (player_2.direction == 'Right'):
                if player_1.walking_flag & player_2.walking_flag:
                    player_1.x -= player_1.vel
                    player_2.x -= player_2.vel
                elif player_1.walking_flag:
                    player_1.x -= player_1.vel
                elif player_2.walking_flag:
                    player_2.x -= player_2.vel
            # Case IV: Player 1 looking left and Player 2 looking left at the players back
            elif (player_1.direction == 'Left') & (player_2.direction == 'Left'):
                if player_1.walking_flag & player_2.walking_flag:
                    player_1.x += player_1.vel
                    player_2.x += player_2.vel
                elif player_1.walking_flag:
                    player_1.x += player_1.vel
                elif player_2.walking_flag:
                    player_2.x += player_2.vel

    # Game animation to move player and update terrain
    player_1.action = pygame.transform.scale(player_1.action, (player_1.width, player_1.height))
    player_2.action = pygame.transform.scale(player_2.action, (player_2.width, player_2.height))
    ''' Shift map
    if player.x < 0:
        map_position = terrain.env.get_rect().move(0, 0)
    elif player.x-player.vel > terrain.screen_width:
        map_position = terrain.env.get_rect().move(terrain.screen_width, 0)
    efflse:
        map_position = terrain.env.get_rect().move(-player.x-player.vel, 0)
    terrain.env.blit(terrain.backdrop, map_position)
    '''
    terrain.env.blit(terrain.backdrop, terrain.perimeter)
    
    position_1 = player_1.action.get_rect().move(player_1.x, player_1.y)
    terrain.env.blit(player_1.action, position_1)
    
    position_2 = player_2.action.get_rect().move(player_2.x, player_2.y)
    terrain.env.blit(player_2.action, position_2)
    
    # Flag if players make contact with each other
    if position_1.colliderect(position_2):
        player_1.collide_flag = True
        player_2.collide_flag = True
    else:
        player_1.collide_flag = False
        player_2.collide_flag = False
    # Update health
    collision(player_1, 'PLAYER_1')
    collision(player_2, 'PLAYER_2')
    
    # Finishing move, perhaps zoom in and watch a slomo frames of the defeat
    if (player_1.health <= 0) | (player_2.health <= 0):
        run_game = False
        # Upload 'GAME OVER' text
        game_over = pygame.image.load('images/Text/game_over.png').convert_alpha()
        game_over_pos = game_over.get_rect().move(int(terrain.screen_size[0]*.22), 
                                                  int(terrain.screen_size[1]*.001))
        game_over = pygame.transform.scale(game_over, (1400, 800))
        terrain.env.blit(game_over, game_over_pos)
    
    pygame.display.update() 
    

time.sleep(3)
pygame.quit()