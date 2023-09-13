import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Riddhi-Gotchi")

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)

# Define font
font = pygame.font.Font('Pixeboy-z8XGD.ttf', 64)
font2 = pygame.font.Font('Pixeboy-z8XGD.ttf', 24)

# Define text
text = font.render("Welcome to Riddhi-Gotchi!", True, black)
intro_text = font2.render("Hi! My name is Riddhi.", True, black)

# Calculate text position
text_rect = text.get_rect()
text_rect.center = (window_width // 2, window_height // 2)


## TODO : Define the numbers of the location so it's easier in the future
intro_text_rect = intro_text.get_rect()
intro_text_rect.center = (390, 500)


# Define text box position and size
text_box_x = 100
text_box_y = 100
text_box_width = 600
text_box_height = 200

# Draw textbox
pygame.draw.rect(window, white, (text_box_x, text_box_y, text_box_width, text_box_height))


# Define text animation variables
animation_delay = 50  # milliseconds
animation_counter = 0
animation_index = 0
animation_text = ""



# Title screen fade-in effect
fade_duration = 4  # Fade-in duration in seconds
fade_frames = fade_duration * 60  # Number of frames for the fade effect

# Set up background of game
background = pygame.image.load("floor.png").convert()
background = pygame.transform.scale(background, (window_width, window_height))


# Add Riddhi Sprite
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



# Game Loop
running = True
clock = pygame.time.Clock()

fade_alpha = 255  # Initial alpha value for fade effect
fade_step = fade_alpha // fade_frames  # Alpha decrement per frame


timer = 0

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic

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




    # Fading effect
    if fade_alpha > 0:
        fade_alpha -= fade_step
        if fade_alpha < 0:
            fade_alpha = 0
    


    """
    if fade_alpha == 0 :
        timer = 2000000

    if timer <= 0 :
        movement_counter = 999999
    """
    

    # Rendering
    window.blit(background, (0, 0)) # Fill the window with dorm image

    window.blit(girl_sprite, girl_position)  # Draw the girl sprite at the current position
    #pygame.display.flip()  # Update the display
    clock.tick(60)
    

    # Draw the white screen with fade effect
    fade_screen = pygame.Surface((window_width, window_height))
    fade_screen.set_alpha(fade_alpha)
    fade_screen.fill(white)
    window.blit(fade_screen, (0, 0))

    # Draw the text on the title screen
    text.set_alpha(fade_alpha)
    window.blit(text, text_rect)

    # Update the display
    if fade_alpha > 0 :
        window.blit(text, text_rect)

    #window.blit(background, (0, 0))  # Clear the screen


    # Render the text on the text box
    window.blit(intro_text, intro_text_rect)

    pygame.display.flip()

    # Delay to control the frame rate
    pygame.time.Clock().tick(60)

# Quit the game
pygame.quit()
