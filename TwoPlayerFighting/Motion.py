import pygame
from PS4 import ps4_config, ps4_button, ps4_hat, ps4_joystick

def motion(player, run_game, player_select):
    # Move using arrow or adws keys
    keys = pygame.key.get_pressed()
    hat = ps4_hat()
    joystick = ps4_joystick()
    
    # PS4 controller configuration
    button_layout, dpad_layout = ps4_config()
    
    '''
    Player 1 - PS4 Controller
    '''    
    if player_select == 'PLAYER_1':
        # Jumping
        if (ps4_button(button_layout['TRIANGLE']) & player.hold_flag == True) | player.in_air_flag == True:
            player.jump_flag = True
            player.jump_up()
        elif player.jump_flag == True:
            player.jump_down()
        else:
            player.jump_cycle_images = 0
        
        # Move left using dpad left or LJoystick left
        if (hat == dpad_layout['DPAD_LEFT']) | (joystick < -0.7):
            player.move_left()
        # Move right using dpad right or LJoystick right
        if (hat == dpad_layout['DPAD_RIGHT']) | (joystick > 0.7):
            player.move_right()
        # Crouch - not incorporated
        #if keys[pygame.K_DOWN] | keys[ord('s')]:
            #player.sit_flag = True
        # Punch with X
        if ps4_button(button_layout['X']):
            player.punch_flag = True
            player.finished_punching_flag = False
        # Kick with square
        if ps4_button(button_layout['SQUARE']):
            player.kick_flag = True
            player.finished_kicking_flag = False
        # Combo Punch with circle
        if ps4_button(button_layout['CIRCLE']):
            player.combo_punch_flag = True
            player.finished_combo_punching_flag = False
        
        if ps4_button(button_layout['R2']):
            player.vel = 70
        else:
            player.vel = 30
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
    
        # Press Options to exit game
        if ps4_button(button_layout['OPTIONS']):
            run_game = False
            
            
    '''
    Player 2 - Keyboard
    '''       
    if player_select == 'PLAYER_2':
        # Jumping
        if ((keys[pygame.K_UP]  | keys[ord('w')]) & player.hold_flag == True) | player.in_air_flag == True:
            player.jump_flag = True
            player.jump_up()
        elif player.jump_flag == True:
            player.jump_down()
        else:
            player.jump_cycle_images = 0
        
        # Move left
        if keys[pygame.K_LEFT] | keys[ord('a')]:
            player.move_left()
        # Moveright
        if keys[pygame.K_RIGHT] | keys[ord('d')]:
            player.move_right()
        # Crouch
        if keys[pygame.K_DOWN] | keys[ord('s')]:
            player.sit_flag = True
        # Punch
        if keys[ord('f')] & ~keys[pygame.K_LSHIFT]:
            player.punch_flag = True
            player.finished_punching_flag = False
        # Kick
        if keys[ord('e')]:
            player.kick_flag = True
            player.finished_kicking_flag = False
        # Combo Punch
        if keys[ord('f')] & keys[pygame.K_LSHIFT]:
            player.combo_punch_flag = True
            player.finished_combo_punching_flag = False
        if keys[ord(' ')]:
            player.vel = 70
        else:
            player.vel = 30
        # Check direction and if or if not idleqqqq
        if player.idle_flag == True:
            player.idle()
        # Player walking cycle
        else:
            player.walk()
        player.idle_flag = True
        
        # Character sitting - not incorporated
        #if player.sit_flag == True:
            #player.sit()
        #player.sit_flag = False
        
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
        if keys[ord('q')]:
            run_game = False
            
    return run_game