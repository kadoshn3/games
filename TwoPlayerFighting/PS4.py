import pygame

'''
PS4 DUALSHOCK CONTROLLER
'''
def ps4_config():
    button_layout = {'SQUARE': 0,
                     'X': 1,
                     'CIRCLE': 2,
                     'TRIANGLE': 3,
                     'L1': 4,
                     'R1': 5,
                     'L2': 6,
                     'R2': 7,
                     'SHARE': 8,
                     'OPTIONS': 9,
                     'L3': 10,
                     'R3': 11,
                     'PS': 12,
                     'TOUCH': 13}
    
    dpad_layout = {'DPAD_UP': (0, 1),
                   'DPAD_DOWN': (0, -1),
                   'DPAD_LEFT': (-1, 0),
                   'DPAD_RIGHT': (1, 0)}
    
    return button_layout, dpad_layout

def ps4_button(button_select):
    pygame.joystick.init()
    ps4 = pygame.joystick.Joystick(0)
    ps4.init()
    button = ps4.get_button(button_select)
    
    return button

def ps4_hat():
    pygame.joystick.init()
    ps4 = pygame.joystick.Joystick(0)
    ps4.init()
    hat = ps4.get_hat(0)
    
    return hat

def ps4_joystick():
    pygame.joystick.init()
    ps4 = pygame.joystick.Joystick(0)
    ps4.init()
    joystick = ps4.get_axis(0)

    return joystick