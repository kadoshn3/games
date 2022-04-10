import pygame
from Terrain import terrain
from Player import player

terrain = terrain()
player = player()

class menu():
    def __init__(self):
        self.run = True
        self.start_screen_image = 'images\menu\selection_screen.jpg'
        self.start_screen = pygame.image.load(self.start_screen_image).convert()
        self.options = 'Null'
        
        self.player_names = ['Rafi', 'Panda', ' Villager', 'Squirtle']
        self.player_images = ['images\Rafi_1.png', 'images\panda\sit.png', 
                              'images\Villager\stand.png', 'images\pokemon\stand.png']
        # SP = Select Player
        self.sp_background = 'cloudy.jpg'
        self.sp_text = 'text\select_player.png'
        self.switch_flag = 'Stay'
        self.player_counter = 0
        self.player_1_coordinates = [terrain.screen_size[0]*0.3-player.width, terrain.screen_size[1]*0.5,]
        self.player_2_coordinates = [terrain.screen_size[0]*0.7, terrain.screen_size[1]*0.5,]
        
        self.options_pos_x = terrain.screen_size[0]/3
        self.options_pos_y = [int(terrain.screen_size[1]*0.2), int(terrain.screen_size[1]*0.3), 
                              int(terrain.screen_size[1]*0.4), int(terrain.screen_size[1]*0.5)]
        
    def player_switch(self):  
        if self.switch_flag == 'Left':
            if self.player_counter == 0:
                self.player_counter = len(self.player_names)-1
            else:
                self.player_counter -= 1
        elif self.switch_flag == 'Right':
            if self.player_counter == len(self.player_names)-1:
                self.player_counter = 0
            else:
                self.player_counter += 1
            
        self.switch_flag = 'Stay'

        return self.player_counter
    
    def select_player(self, player_counter, player_select):
        if player_select == 'PLAYER_1':
            self.player_select = pygame.image.load(self.player_images[player_counter]).convert_alpha()
            self.player_position = terrain.env.get_rect().move(self.player_1_coordinates)
        elif player_select == 'PLAYER_2':
            self.player_select = pygame.image.load(self.player_images[player_counter]).convert_alpha()
            self.player_position = terrain.env.get_rect().move(self.player_2_coordinates)
        self.player_select = pygame.transform.scale(self.player_select, (player.width, player.height))
        terrain.env.blit(self.player_select, self.player_position)
    
    def start_screen(self):
        self.start_menu = terrain.env.get_rect()
        self.start_screen = pygame.transform.scale(self.start_screen, 
                            (terrain.screen_size[0], terrain.screen_size[1]))
        terrain.env.blit(self.start_screen, self.start_menu)
        