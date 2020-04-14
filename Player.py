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
        self.jump_vel = 15
        
        # Map character starting position
        self.start_x = 170
        self.start_y = 800#290
        self.x = self.start_x
        self.y = self.start_y
        
        # Character dimension
        self.width = 60*3
        self.height = 50*3
        
        # Player starting direction
        self.direction = 'Right'
        
        # Character files
        self.idle_image = 'images\panda\walk_3.png'
        self.jump_file = 'images\panda\jump.png'
        self.walking_images = ['images\panda\walk_1.png', 'images\panda\walk_2.png', 'images\panda\walk_3.png']
        self.walk_cycle = 0
        
        # Character player image to be moved
        self.action = pygame.image.load(self.idle_image).convert_alpha()
        
        # row and column starts at 0
        self.filename = 'images\panda_sprite.png'
        self.row = 2
        self.col = 3
        self.i = 0
        # Sprite demensions
        self.sprite_height = 60
        self.sprite_width = 49
        self.obtain = True
        if self.obtain:
            self.get_sprite(self.filename, self.row, self.col, self.i, 
                            self.sprite_height, self.sprite_width)
       
        # Jumping paramters
        self.jump_counter = 0 
        self.gravity = 10
        self.t = 4
        self.jump_cycle = self.t + 1
        
        # Flags
        self.idle_flag = True
        self.in_air_flag = False
        self.hold_flag = True
        self.jump_flag = False
        self.sit_flag = False
        
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
        self.action = pygame.image.load(self.idle_image).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
    
    def walk(self):
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
        self.action = pygame.image.load(self.jump_file).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)
            
    def get_sprite(self, filename, row, col, i, height, width):
        # Open sprite sheet
        self.sprite_sheet = filename
        self.sprite = PIL.Image.open(self.sprite_sheet)
        self.flip = True
        self.bias = 20
        self.left = width * col
        self.top = height * row
        self.right = width + self.left
        self.bottom = self.top + height - self.bias
        
        self.sprite = self.sprite.crop((self.left, self.top, 
                                        self.right, self.bottom)) 
        if self.flip:
            self.sprite = ImageOps.mirror(self.sprite)
        self.sprite.save('images\panda\sprite_' + str(i) + '.png')
        
    def sit(self):
        self.sit_file = 'images\panda\sit.png'
        self.action = pygame.image.load(self.sit_file).convert_alpha()
        if self.direction == 'Left':
            self.action = pygame.transform.flip(self.action, True, False)