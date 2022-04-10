import PIL
from PIL import ImageOps
def extract_sprite(filename, row, col, i, height, width):
    sprite = PIL.Image.open(filename)
    flip = False
    bias = 20
    left = width * col
    top = height * row
    right = width + left
    bottom = top + height - bias
    
    sprite = sprite.crop((left, top, right, bottom)) 
    if flip:
        sprite = ImageOps.mirror(sprite)
    sprite.save('images\Fighter\\combo_punch_' + str(i) + '.png')
    

# row and column starts at 0
filename = 'images\Fighter\Fighter_sprite.png'
row = 2.41
col = 5.5
i = 5
# Sprite demensions
height = 120
width = 55
obtain = True
if obtain:
    extract_sprite(filename, row, col, i, height, width)