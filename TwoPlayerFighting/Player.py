'''
Player parameters
'''
from Terrain import terrain
import PIL
from PIL import ImageOps
import pygame
terrain = terrain()

class player():
    def __init__(self):
        # Velocity
        self.vel = 30
        self.jump_vel = 30
        
        # Map character starting position
        self.start_x = int(terrain.screen_size[0]*0.2)
        self.start_y = 700#290
        self.x = self.start_x
        self.y = self.start_y
        
        # Character dimension
        self.scale = 3
        self.width = int(50*self.scale)
        self.height = int(70*self.scale)
        self.distance = 100
        
        # Player starting direction
        self.direction = 'Right'
        
        # Character files
        self.idle_image = 'images\Fighter\Fight_0.png'
        self.jump_file = ['images\Fighter\jump_0.png', 'images\Fighter\jump_1.png', 'images\Fighter\jump_2.png']
        self.sit_file = 'images\panda\sit.png'
        self.walking_images = ['images\Fighter\walk_0.png', 'images\Fighter\walk_1.png', 'images\Fighter\walk_2.png',
                               'images\Fighter\walk_3.png', 'images\Fighter\walk_4.png']
        self.punch_images = ['images\Fighter\Fight_0.png', 'images\Fighter\Fight_2.png', 
                             'images\Fighter\Fight_2.png', 'images\Fighter\Fight_1.png']
        self.kick_images = ['images\Fighter\kick_0.png', 'images\Fighter\kick_1.png', 'images\Fighter\kick_1.png']
        self.combo_punch_images = ['images\Fighter\combo_punch_0.png', 'images\Fighter\combo_punch_1.png', 'images\Fighter\combo_punch_2.png', 
                                   'images\Fighter\combo_punch_3.png', 'images\Fighter\combo_punch_4.png', 'images\Fighter\combo_punch_5.png']
        self.walk_cycle = 0
        self.jump_cycle_images = 0
        self.punch_cycle_images = 0
        self.kick_cycle_images = 0
        self.combo_punch_cycle_images = 0
        
        # Character player image to be moved
        self.action = pygame.image.load(self.idle_image).convert_alpha()
       
        # Jumping paramters
        self.jump_counter = 0 
        self.gravity = 10
        self.t = 4
        self.jump_cycle = self.t + 1
        
        # Motion flags
        self.idle_flag = True
        self.in_air_flag = False
        self.hold_flag = True
        self.jump_flag = False
        self.sit_flag = False
        # Attack flags
        self.punch_flag = False
        self.finished_punching_flag = True
        self.kick_flag = False
        self.finished_kicking_flag = True
        self.combo_punch_flag = False
        self.finished_combo_punching_flag = True
        # Player collision and registering a hit
        self.collided_flag = True
        self.walking_flag = False
        
        self.health = 100
        self.damage = 10
        self.combo_damage = 20
        self.damage_count = 1
        
    # Character movement functions
    def move_left(self):
        self.idle_flag = False
        self.direction = 'Left'
        if self.x > 0:
            self.x -= self.vel
            
    def move_right(self):
        self.idle_flag = False
        self.direction = 'Right'
        if self.x < terrain.screen_width-self.width:
            self.x += self.vel
            
    def move_up(self):
        self.idle_flag = False
        if self.y > 0:
            self.y -= self.vel
            
    def move_down(self):
        self.idle_flag = False
        if self.y < terrain.screen_size[1]-self.height:
            self.y += self.vel
    
    # Character is idle
    def idle(self):
        self.walking_flag = False
        self.action = pygame.image.load(self.idle_image).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
    
    def walk(self):
        self.walking_flag = True
        self.action = pygame.image.load(self.walking_images[self.walk_cycle]).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
        self.walk_cycle += 1
        if self.walk_cycle == len(self.walking_images):
            self.walk_cycle = 0
            
    # Character jump functions
    def jump_up(self):
        self.in_air_flag = True
        if self.jump_counter < self.jump_cycle:
            self.y -= self.jump_vel + .5*self.gravity*self.t**2
            self.jump_counter += 1
            self.t -= 1 
        else:
            self.in_air_flag = False
            self.hold_flag = False
            self.t = 0
            
    def jump_down(self):
        if self.jump_counter > 0:
            self.y += self.jump_vel + .5*self.gravity*self.t**2
            self.jump_counter -= 1
            self.t += 1
        else:
            self.jump_flag = False
            self.hold_flag = True
            self.t = self.jump_cycle - 1
            
    def load_jump_image(self):
        self.action = pygame.image.load(self.jump_file[self.jump_cycle_images]).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
        if self.jump_cycle_images < len(self.jump_file)-1:
            self.jump_cycle_images += 1
        else:
            self.jump_cycle_images = len(self.jump_file)-1
        return self.jump_cycle_images
            
        
    def sit(self):
        self.action = pygame.image.load(self.sit_file).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
    
    def attack(self, images, cycle_images, finished_attacking_flag):
        self.action = pygame.image.load(images[cycle_images]).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
        cycle_images += 1
        if cycle_images == len(images):
            finished_attacking_flag = True
            cycle_images = 0
            
        return finished_attacking_flag, cycle_images