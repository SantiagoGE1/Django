import pygame
pygame.init()
pygame.quit()
large = 600
width = 600
screen = pygame.display.set_mode((large, width))
img_to_import = pygame.image.load("img/bataman_img.png")
img_to_import = pygame.transform.scale(img_to_import, (200, 200))
object_in_screen = img_to_import.get_rect()
object_in_screen.topleft = (width/2,large/2)
velocity = 1
run = True
while run:
    keyword = pygame.key.get_pressed()
    if keyword[pygame.K_RIGHT] and object_in_screen.right<large:
        object_in_screen.x += velocity
    elif keyword[pygame.K_LEFT] and object_in_screen.left>0:
        object_in_screen.x -= velocity
        print("Does work")
    elif keyword[pygame.K_UP] and object_in_screen.top>0:
        object_in_screen.y -= velocity
        print("does work")
    elif keyword[pygame.K_DOWN] and object_in_screen.bottom<width:
        object_in_screen.y += velocity
        print("does work")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.blit(img_to_import, object_in_screen)    
    pygame.display.update()
