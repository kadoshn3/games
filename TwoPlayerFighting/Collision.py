import pygame
from PS4 import ps4_config, ps4_button, ps4_hat, ps4_joystick
from Terrain import terrain
terrain = terrain()
def collision(player, player_select):
    button_layout, dpad_layout = ps4_config()
    keys = pygame.key.get_pressed()
    health_width, health_length = 400, 100
    if player.collide_flag:
        if player.damage_count % 2 == 0:
            if player_select == 'PLAYER_1':
                if ps4_button(button_layout['X']):
                    player.health -= player.damage
                    print('Player 1 Health:', player.health)
                if ps4_button(button_layout['CIRCLE']):
                    player.health -= player.combo_damage
                    print('Player 1 Health:', player.health)
                if ps4_button(button_layout['SQUARE']):
                    player.health -= player.damage
                    print('Player 1 Health:', player.health)
                
    
            elif player_select == 'PLAYER_2':
                if keys[ord('f')] & ~keys[pygame.K_LSHIFT]:
                    player.health -= player.damage
                    print('Player 2 Health:', player.health)
                if keys[ord('f')] & keys[pygame.K_LSHIFT]:
                    player.health -= player.combo_damage
                    print('Player 2 Health:', player.health)
                if keys[ord('e')]:
                    player.health -= player.damage
                    print('Player 2 Health:', player.health)
    
        player.damage_count += 1
        
    if player_select == 'PLAYER_1':
        health = pygame.image.load('images/health/'+str(player.health)+'hp.png').convert_alpha()
        bar_pos = health.get_rect().move(int(terrain.screen_size[0]*.8), 
                                         int(terrain.screen_size[1]*.1))
        health = pygame.transform.scale(health, (health_width, health_length))
        terrain.env.blit(health, bar_pos)
    if player_select == 'PLAYER_2':
        health = pygame.image.load('images/health/'+str(player.health)+'hp.png').convert_alpha()
        bar_pos = health.get_rect().move(int(terrain.screen_size[0]*.1), 
                                         int(terrain.screen_size[1]*.1))
        health = pygame.transform.scale(health, (health_width, health_length))
        terrain.env.blit(health, bar_pos)