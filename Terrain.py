'''
Game terrain
'''
#from Player import player
import pygame
import PIL

#player = player()

class terrain():
    def __init__(self):
        self.env_images = ['images\Backyard.PNG', 'images\Bamboo_house.jpg', 'images\super_smash_bros.png', 'images\jungle.jfif']
        self.env_select = 0
        
        self.image = PIL.Image.open(self.env_images[self.env_select])
        self.env_width, self.env_height = self.image.size
        self.screen_shift = int(0.5*self.env_width)
        self.screen_width = self.env_width-self.screen_shift
        self.screen_size = [self.screen_width, self.env_height]
        self.env = pygame.display.set_mode(self.screen_size)
        self.backdrop = pygame.image.load(self.env_images[self.env_select]).convert()
        #self.backdrop = pygame.transform.scale(self.backdrop, self.screen_size)
        self.perimeter = self.env.get_rect()
    
    def map_shift(self):
        self.backdrop = pygame.image.load(self.env_images[self.env_select]).convert()