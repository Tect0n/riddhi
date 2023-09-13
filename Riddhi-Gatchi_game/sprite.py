import pygame
import random

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("8-Bit Sprite")


girl_sprite = pygame.image.load("Riddhi V2.png")
girl_sprite = pygame.transform.scale(girl_sprite, (100, 100))
girl_position = [200, 200]  # Set the initial position of the girl sprite

background = pygame.image.load("floor.png").convert()
background = pygame.transform.scale(background, (800, 600))


movement_interval = random.randint(500, 2000)  # Random interval for movement in milliseconds
movement_counter = 0  # Counter to keep track of elapsed time
move_direction = "right"  # Initial movement direction

step_size = 50
max_x = 500
max_y = 200
min_x = 400
min_y = 100


##########################################################
## For text

black = (0, 0, 0)

# Define font

font = pygame.font.Font('Pixeboy-z8XGD.ttf', 24)

# Define Text
text = "This is a test sentence"

# Define text surfaces and positions
text_surfaces = []
text_rects = []
for i in range(len(text)):
    text_surface = font.render(text[:i+1], True, black)
    text_surfaces.append(text_surface)
    text_rect = text_surface.get_rect()
    text_rect.center = (390, 500)
    text_rects.append(text_rect)


# Define animation variables
animation_delay = 50  # milliseconds
animation_counter = 0
animation_index = 0





running = True
clock = pygame.time.Clock()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the girl's position
    if movement_counter >= movement_interval:
        if move_direction == "right":
            girl_position[0] += step_size
            if girl_position[0] >= max_x:
                move_direction = "down"
        elif move_direction == "down":
            girl_position[1] += step_size
            if girl_position[1] >= max_y:
                move_direction = "left"
        elif move_direction == "left":
            girl_position[0] -= step_size
            if girl_position[0] <= min_x:
                move_direction = "up"
        elif move_direction == "up":
            girl_position[1] -= step_size
            if girl_position[1] <= min_y:
                move_direction = "right"

        movement_interval = random.randint(500, 2000)  # Reset the movement interval
        movement_counter = 0  # Reset the movement counter
    else:
        movement_counter += clock.get_time()  # Increment the movement counter

    # Redraw the screen
    screen.blit(background, (0, 0))  # Clear the screen
    screen.blit(girl_sprite, girl_position)  # Draw the girl sprite at the current position
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Limit the frame rate

pygame.quit()
