import pygame
from Terrain import terrain
terrain = terrain()

# Loading an image
def load_image(filename, pos_x, pos_y, width, height):
    image = 'images\\' + filename 
    start_screen = pygame.image.load(image).convert_alpha()
    start_menu = terrain.env.get_rect().move(pos_x, pos_y)
    start_screen = pygame.transform.scale(start_screen, (width, height))
    terrain.env.blit(start_screen, start_menu)
    
    rect = pygame.Rect(pos_x, pos_y, width, height)
    
    return rect