import pygame
import random




## Bar attrius - 1. position 2. Colour of the bar 3. 


class Bar:
    def __init__(self, max_value, position, color):
        self.max_value = max_value
        self.value = max_value
        self.position = position
        self.color = color

    def decrease(self, amount):
        self.value -= amount
        if self.value < 0:
            self.value = 0

    def increase(self, amount):
        self.value += amount
        if self.value > self.max_value:
            self.value = self.max_value

    def draw(self, surface):
        # Calculate the width of the bar based on the current value and the maximum value
        bar_width = int((self.value / self.max_value) * 100)

        # Draw the background of the bar
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], 100, 10))

        # Draw the filled portion of the bar
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], bar_width, 10))



# Create a Pygame surface to draw on
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Create a bar and draw it on the surface
max_value = 100
# bar_position = (10, 100)
bar_color = (0, 255, 0)

bar1 = Bar(max_value, (10,100), bar_color)
bar2 = Bar(max_value, (10,200), (0, 0, 255))
bar3 = Bar(max_value, (10,300), (255, 255, 0))

print (bar2.value)
print(bar3.value)

clock = clock = pygame.time.Clock()




# Create the button and draw it on the surface
button_color = (255, 0, 0)
button_width = 100
button_height = 50
button_x = window_width - button_width - 10
button_y = window_height - button_height - 10
button_rect = pygame.Rect(button_x, button_y, button_width, button_height)


# Game loop
running = True

start_time1 = pygame.time.get_ticks()
decrease_amount = 20

x = 0
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button_rect.collidepoint(mouse_pos):
                    bar2.increase(10)
                    bar3.increase(30)
                    avg = (bar2.value + bar3.value)/2
                    count = max_value- avg
                    bar1.increase(20)

    # Update the game state

    decrease_amount = random.randint(1, 10)

    pygame.time.Clock().tick(60)
     
    current_time1 = pygame.time.get_ticks()  


    if bar2.value > 0 :
        # Get the current time
        current_time1 = pygame.time.get_ticks()

        # Check if 5 seconds have elapsed since the last decrease
        if current_time1 - start_time1 >= 1000:
            # Decrease the value of bar2 by the decrease amount
            bar2.decrease(decrease_amount)

            # Reset the start time to the current time
            start_time1 = current_time1


    #bar2.decrease(20)
    #bar3.decrease(40)
    #bar1.decrease(10)

    # Draw the game state
    window.fill((0, 0, 0))
    bar1.draw(window)

    bar2.draw(window)
    bar3.draw(window)

    pygame.draw.rect(window, button_color, button_rect)

    # Update the display
    pygame.display.flip()

pygame.quit()

# Quit the game
