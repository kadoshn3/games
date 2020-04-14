import pygame
from Player import player
from Terrain import terrain

# initialize game and call classes
pygame.init()
player = player()
terrain = terrain()

# Name of game
pygame.display.set_caption('First Game')

run_game = True

# Main game loop
while run_game:
    pygame.time.delay(100)
    # Move using arrow or adws keys
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_game = False
    
    if ((keys[pygame.K_UP]  | keys[ord('w')]) & player.hold_flag == True) | player.in_air_flag == True:
        player.jump_flag = True
        player.jump_up()
    elif player.jump_flag == True:
        player.jump_down()

    if keys[pygame.K_LEFT] | keys[ord('a')]:
        player.move_left()
    if keys[pygame.K_RIGHT] | keys[ord('d')]:
        player.move_right()
    #if keys[pygame.K_UP] | keys[ord('w')]:
        #player.move_up()
    if keys[pygame.K_DOWN] | keys[ord('s')]:
        player.sit_flag = True

        
    # Check direction and if or if not idle
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
    
    # Loading jump image if in the air
    if player.jump_flag == True | player.in_air_flag == True:
        player.load_jump_image()
        
    # Press Q to exit game
    if keys[ord('q')]:
        pygame.quit()
    
    # Game animation to move player and update terrain
    player.action = pygame.transform.scale(player.action, (player.width, player.height))
    if player.x < 0:
        map_position = terrain.env.get_rect().move(0, 0)
    elif player.x-player.vel > terrain.screen_width:
        map_position = terrain.env.get_rect().move(terrain.screen_width, 0)
    else:
        map_position = terrain.env.get_rect().move(-player.x-player.vel, 0)
    terrain.env.blit(terrain.backdrop, map_position)
    position = player.action.get_rect().move(player.x, player.y)
    terrain.env.blit(player.action, position)
    pygame.display.update() 
    
pygame.quit()