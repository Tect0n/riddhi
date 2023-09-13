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

# Define Font
Font = pygame.font.Font('Pixeboy-z8XGD.ttf', 64)
Font2 = pygame.font.Font('Pixeboy-z8XGD.ttf', 24)
Font3 = pygame.font.Font('Pixeboy-z8XGD.ttf', 20)

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)


# Set up background of game
background = pygame.image.load("floor.png").convert()
background = pygame.transform.scale(background, (window_width, window_height))


####################### Title screen ############################


# Title screen fade-in effect

text1  = Font.render("Welcome to Riddhi-Gotchi!", True, black)
fade_duration = 4  # Fade-in duration in seconds
fade_frames = fade_duration * 60  # Number of frames for the fade effect

fade_alpha = 255  # Initial alpha value for fade effect
fade_step = fade_alpha // fade_frames  # Alpha decrement per frame

# Calculate text position
text_rect = text1.get_rect()
text_rect.center = (window_width // 2, window_height // 2)




timer = 0


######################## Text Class #############################

class Text:
    def __init__(self, text, font, position):
        self.text = text
        self.font = font
        self.position = position
        self.animation_delay = 50  # milliseconds
        self.animation_counter = 0
        self.animation_index = 0
        self.animation_text = ""
        self.surface = self.font.render(self.text, True, black)
        self.rect = self.surface.get_rect(left=self.position[0], top=self.position[1])
        self.active = True

    def update(self):
        pass


    def update_animation(self, surface):
        if self.animation_index < len(self.text):
            self.animation_counter += clock.tick()
            if self.animation_counter >= self.animation_delay:
                self.animation_counter = 0
                self.animation_text += self.text[self.animation_index]
                self.animation_index += 1
                self.surface = self.font.render(self.animation_text, True, black)
                self.rect = self.surface.get_rect(left=self.position[0], top=self.position[1])
        if self.active :
            surface.blit(self.surface, self.rect)        
        
    def render(self, surface) :
        if self.active:
            surface.blit(self.surface, self.rect)

    def set_position(self, position):
        self.position = position
        self.rect.center = self.position

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False

    def set_animation_delay(self, delay):
        self.animation_delay = delay

    def reset_animation(self):
        self.animation_counter = 0
        self.animation_index = 0
        self.animation_text = ""
        self.surface = self.font.render(self.text, True, black)
        self.rect = self.surface.get_rect(center=self.position)


# Create instances of Text class
#text1 = Text("Welcome to Riddhi-Gotchi!", Font, (60, 250))
text2 = Text("Hi, My name is Riddhi! Welcome to my dorm.", Font2, (300, 500))
text3 = Text("I'm a 20-something year old Art student who ", Font2, (300, 500))
text4 = Text("loves to paint, read and drink chai.", Font2, (300, 530))
text5 = Text("Help me get through my time in uni by feeding ", Font2, (300, 500))
text6 = Text("me, playing with me and making sure my health ", Font2, (300, 530))
text7 = Text("doesn't drop to 0!", Font2, (300, 500))
text8 = Text("This is my health bar, if it drops to 0, then", Font2, (300, 530))
text9 = Text("I drop out of uni!", Font2, (300, 500))
text10 = Text("This is my Happy bar, if it drops to 0", Font2, (300, 530))
text11 = Text("then I will drop out of uni! Keep me" , Font2 ,(300, 500))
text12 = Text("happy!", Font2, (300, 530) )

text13 = Text("This is my hunger bar, if it drops to 0", Font2,(300,500))
text14 = Text("then I will drop out of uni! Keep me fed!", Font2, (300, 530))
health_bar_text = Text("Health : ", Font3, (60, 490))
happy_bar_text = Text("Happy : ", Font3, (60, 520)) 
hunger_bar_text = Text("Hunger : ", Font3, (60, 550)) 

choice_text = Text("What would you like to do? - " , Font2 ,(300, 500))



listen_text1 = Text("This one time, out of nowehere... " , Font2 ,(300, 500))
listen_text2 = Text("my friend erin had given me a clove of garlic!" , Font2 ,(300, 530))
listen_text3 = Text("I love her so much" , Font2 ,(300, 500))

story1_text1 = Text("Do you know what's my favourite painting? " , Font2 ,(300, 500))
story1_text2 = Text("It's called 'Las Meninas' by Deigo Velazquez " , Font2 ,(300, 530))

story1_text3 = Text("It's an amazing piece of work that uses persepective", Font2 ,(300, 500))
story1_text4 = Text("and light for a royal potrait!", Font2 ,(300, 530)) 
story1_text5 = Text(" I hope to travel to Spain and see it someday :D", Font2 ,(300, 500) )


story2_text1 = Text("One of my favourite song lyrics is - ", Font2 ,(300, 500))
story2_text2 = Text("'In another life, we were arsonists'!", Font2 ,(300, 530))

story3_text1 = Text("Someone get me Posca pens!!!", Font2 ,(300, 500))

story4_text1 = Text("Both Chrysanthmum and Chamomile Teas are scams.", Font2 ,(300, 500))
story4_text2 = Text(" Don't ask me why.", Font2 ,(300, 530))

story5_text1 = Text("Soup is like an edible hug!", Font2 ,(300, 500))


################################ Sprite Class ###########################

step_size = 50
max_x = 500
max_y = 200
min_x = 400
min_y = 100



class Sprite:
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.movement_interval = random.randint(500, 2000)
        self.movement_counter = 0
        self.movement_paused = False
        self.move_direction = "right"
        self.last_update_time = 0

    def update(self, clock, min_x, max_x, min_y, max_y, step_size):
        current_time = pygame.time.get_ticks()
        time_elapsed = current_time - self.last_update_time

        if not self.movement_paused:
            if self.movement_counter >= self.movement_interval:
                if self.move_direction == "right":
                    self.position[0] += step_size
                    if self.position[0] >= max_x:
                        self.move_direction = "down"
                elif self.move_direction == "down":
                    self.position[1] += step_size
                    if self.position[1] >= max_y:
                        self.move_direction = "left"
                elif self.move_direction == "left":
                    self.position[0] -= step_size
                    if self.position[0] <= min_x:
                        self.move_direction = "up"
                elif self.move_direction == "up":
                    self.position[1] -= step_size
                    if self.position[1] <= min_y:
                        self.move_direction = "right"
                self.movement_interval = random.randint(500, 2000)
                self.movement_counter = 0
            else:
                self.movement_counter += time_elapsed
        self.last_update_time = current_time


    def render(self, surface):
        surface.blit(self.image, self.position)

    def stop(self):
        self.movement_paused = True

    def restart(self):
        self.movement_paused = False

# Initlalize riddhi

girl_sprite = pygame.image.load("Riddhi V2.png")
girl_sprite = pygame.transform.scale(girl_sprite, (100, 100))
girl_position = [200, 200]

riddhi = Sprite(girl_sprite, girl_position)

############################### Bar class ##############################

class Bar:
    def __init__(self, max_value, position, color):
        self.max_value = max_value
        self.value = max_value
        self.position = position
        self.color = color
        self.active = True

    def decrease(self, amount):
        if self.active:
            self.value -= amount
            if self.value < 0:
                self.value = 0

    def increase(self, amount):
        if self.active:
            self.value += amount
            if self.value > self.max_value:
                self.value = self.max_value
    
    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True



    def draw(self, surface):
            
        # Calculate the width of the bar based on the current value and the maximum value
        bar_width = int((self.value / self.max_value) * 100)

        # Draw the background of the bar
        pygame.draw.rect(surface, (255, 0, 0), (self.position[0], self.position[1], 100, 10))

        # Draw the filled portion of the bar
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], bar_width, 10))


# Max value of each bar
max_value = 100


bar1 = Bar(max_value, (130,490), (0, 255, 0))
bar2 = Bar(max_value, (130,520), (0, 0, 255))
bar3 = Bar(max_value, (130,550), (255, 255, 0))


############################### Button Class #########################
class Button:
    def __init__(self, text, position, font_size=20, border_width=2, border_color=(0, 0, 0)):
        self.text = text
        self.position = position
        self.font_size = font_size
        self.border_width = border_width
        self.border_color = border_color
        self.font = pygame.font.Font('Pixeboy-z8XGD.ttf', self.font_size)
        self.rect = pygame.Rect(self.position, (0, 0))
        self.active = True

    def draw(self, surface):
        if self.active == True : 
            # Draw the button background
            button_rect = pygame.Rect(self.position, (0, 0))
            button_rect.width = self.font.size(self.text)[0] + self.border_width * 2 + 10
            button_rect.height = self.font.size(self.text)[1] + self.border_width * 2 + 10
            #pygame.draw.rect(surface, (255, 255, 255), button_rect)

            # Draw the button border
            border_rect = button_rect.copy()
            border_rect.inflate_ip(self.border_width * -1, self.border_width * -1)
            pygame.draw.rect(surface, self.border_color, border_rect, self.border_width)

            # Draw the text on the button
            text_surface = self.font.render(self.text, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=button_rect.center)
            surface.blit(text_surface, text_rect)

            # Update the button rect
            self.rect = button_rect

    def is_hovered(self):
        if self.active == True : 
         # Check if the mouse is hovering over the button
            mouse_pos = pygame.mouse.get_pos()
            return self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if self.active == True : 
            # Handle events for the button
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.is_hovered():
                    return True
            return False

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False



play_button = Button("Play", (300, 520))
feed_button = Button("Feed", (400, 520))
lie_button = Button("Lie Horizontal", (500, 520))
hug_button = Button("Hug", (650, 520))
test_button = Button("Test", (400, 520))
y = 0


#### Play Options ####
paint_button = Button("paint", (300, 520))
listen_button = Button("listen", (400, 520))
invite_button = Button("invite", (500, 520))
gift_button = Button("gift", (600, 520))


#### Feed Options ####
chai_button = Button("chai", (300, 520))
pav_button = Button("pav bhaji", (370, 520))
tiger_button = Button("tiger beer", (480, 520))
cake_button = Button("Red Vevlet cake", (590, 520))

intro_button_list = [play_button, feed_button, lie_button, hug_button]

play_button_list = [paint_button, listen_button, gift_button, invite_button]
feed_button_list = [chai_button, pav_button, tiger_button, cake_button]




################################ Game loop ##############################
running = True
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()
x = 0
start_time1 = pygame.time.get_ticks() 
start_time2 = pygame.time.get_ticks()
start_time3 = pygame.time.get_ticks()
decrease_amount = 20

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.handle_event(event):
                y = 1
            elif feed_button.handle_event(event):
                #chai_button.activate()
                y = 2
            elif lie_button.handle_event(event) and bar1.value < 100:
                bar1.value = bar1.value + 10
                y = 0
            elif hug_button.handle_event(event) and bar1.value < 100:
                bar1.value = bar1.value + 10
                y = 0
            elif chai_button.handle_event(event) and bar3.value < 100 :
                bar3.value = bar3.value + 10
                chai_button.deactivate()
                y = 0
            elif gift_button.handle_event(event) and bar2.value < 100:
                bar2.value = bar2.value + 10
                gift_button.deactivate()
                y = 0
            elif listen_button.handle_event(event):
                listen_time = pygame.time.get_ticks()
                story = [0,1,2,3,4,5]
                story_choice = random.choice(story)
                bar2.value = bar2.value + 10
                bar2.deactivate()
                y = 3
  

            
                
    
    # Set animation delay
    #text2.set_animation_delay(10)


    # Fill the window with dorm image
    window.blit(background, (0, 0))


    # Animate Riddhi
    riddhi.update(clock, min_x, max_x, min_y, max_y, step_size)


    # Add Riddhi
    riddhi.render(window)

    current_time1 = pygame.time.get_ticks()  
    decrease_amount = random.randint(1, 10)


    # Fading effect
    if fade_alpha > 0:
        fade_alpha -= fade_step
        if fade_alpha < 0:
            fade_alpha = 0


    # Draw the white screen with fade effect
    fade_screen = pygame.Surface((window_width, window_height))
    fade_screen.set_alpha(fade_alpha)
    fade_screen.fill(white)
    window.blit(fade_screen, (0, 0))


    # Draw the text on the title screen
    text1.set_alpha(fade_alpha)
    window.blit(text1, text_rect)

    pygame.time.Clock().tick(60)

    ##### Button Logic #####
    if y == 0 and x == 7:
        for button in intro_button_list:
            button.activate()

        for button in intro_button_list:
            button.activate()
            button.draw(window)  

    if y == 1:
        for button in intro_button_list:
            button.deactivate()  

        for button in play_button_list:
            button.activate()
            button.draw(window)


    if y == 2:
        for button in intro_button_list:
            button.deactivate()        

        for button in feed_button_list:
            button.activate()
            button.draw(window)




    ####### Listen Button ########

    if y == 3:
        choice_text.deactivate()
        
        for button in play_button_list: 
            button.deactivate()   

        if story_choice == 0 :

            listen_text1.update_animation(window)
            #listen_text1.render(window)
            listen_time2 = pygame.time.get_ticks()

            if listen_time2 - listen_time >= 3500:
                listen_text2.update_animation(window)
            
            if listen_time2 - listen_time >= 7000:
                bar2.activate()
                y = 0
                choice_text.activate()
                listen_text1.reset_animation()
                listen_text2.reset_animation()
                
        
        elif story_choice == 1:

            story1_text1.update_animation(window)
            listen_time2 = pygame.time.get_ticks()

            if listen_time2 - listen_time >= 3500:
                story1_text2.update_animation(window)

            if listen_time2 - listen_time >= 7000:
                bar2.activate()
                y = 0
                choice_text.activate()
                story1_text1.reset_animation()
                story1_text2.reset_animation()

        elif story_choice == 2:

            story2_text1.update_animation(window)
            listen_time2 = pygame.time.get_ticks()

            if listen_time2 - listen_time >= 3500:
                story2_text2.update_animation(window)


            if listen_time2 - listen_time >= 6500:
                bar2.activate()
                y = 0
                choice_text.activate()
                story2_text1.reset_animation()
                story2_text2.reset_animation() 
            
        elif story_choice == 3:

            story3_text1.update_animation(window)
            listen_time2 = pygame.time.get_ticks()

            if listen_time2 - listen_time >= 3500:
                bar2.activate()
                y = 0
                choice_text.activate()
                story3_text1.reset_animation()

        elif story_choice == 4:

            story4_text1.update_animation(window)
            listen_time2 = pygame.time.get_ticks()

            if listen_time2 - listen_time >= 3500:
                story4_text2.update_animation(window)


            if listen_time2 - listen_time >= 6500:
                bar2.activate()
                y = 0
                choice_text.activate()
                story4_text1.reset_animation()
                story4_text2.reset_animation() 
    

        elif story_choice == 5:

            story5_text1.update_animation(window)
            listen_time2 = pygame.time.get_ticks()

            if listen_time2 - listen_time >= 3500:
                bar2.activate()
                y = 0
                choice_text.activate()
                story5_text1.reset_animation()



            





        #listen_text2.update_animation(window)
        #listen_text2.render(window)   



    ###### Text Logic ######
    
    current_time = pygame.time.get_ticks()  

    if current_time >= 10000:
        x = 1

    if current_time >= 17500:
        x = 2
    
    if current_time >= 23500:
        x = 3

    if current_time >= 30500:
        x = 4
    
    if current_time >= 36500:
        x = 5
    
    if current_time >= 41000:
        x = 6
    
    if current_time >= 48000:
        x = 7


    if current_time - start_time >= 4000 and x == 0:
        text2.update_animation(window)
        #text2.render(window)
    elif current_time - start_time >= 10000 and x == 1:
        text3.update_animation(window)
        #text3.render(window)
        

    if current_time - start_time >= 12500 and x == 1:
        text4.update_animation(window)
        
    elif current_time - start_time >= 17500 and x == 2:
        text5.update_animation(window)
        
    
    if current_time - start_time >= 20000 and x == 2:
        text6.update_animation(window)
        
    elif current_time - start_time >= 23500 and x == 3:
        text7.update_animation(window)
        

    if current_time - start_time >= 26500 and x == 3:
        text8.update_animation(window)
        
        
    elif current_time - start_time >= 30500 and x == 4:
        text9.update_animation(window)
        

    if current_time - start_time >= 33500 and x == 4:
        text10.update_animation(window)
        
    elif current_time - start_time >= 36500 and x == 5:
        text11.update_animation(window)
        

    if current_time - start_time >= 39000 and x == 5:
        text12.update_animation(window)
    elif current_time - start_time >= 41000 and x == 6:
        text13.update_animation(window)
       

    if current_time - start_time >= 44000 and x == 6:
        text14.update_animation(window)
        
    elif current_time - start_time >= 48000 and x == 7:
        choice_text.update_animation(window)
        


######  Logic to reduce Bar #####

    if bar1.value > 0 and current_time - start_time >= 26500 :
        # Get the current time
        current_time1 = pygame.time.get_ticks()
        health_bar_text.render(window)

        # Check if 5 seconds have elapsed since the last decrease
        if current_time1 - start_time1 >= 10000 :
            # Decrease the value of bar2 by the decrease amount
            bar1.decrease(decrease_amount)

            # Reset the start time to the current time
            start_time1 = current_time1   

        bar1.draw(window)  

    if bar2.value > 0 and current_time - start_time >= 33000 :
        # Get the current time
        current_time1 = pygame.time.get_ticks()
        happy_bar_text.render(window)

        # Check if 5 seconds have elapsed since the last decrease
        if current_time1 - start_time2 >= 10000 :
            # Decrease the value of bar2 by the decrease amount
            bar2.decrease(decrease_amount)

            # Reset the start time to the current time
            start_time2 = current_time1   

        bar2.draw(window)  

    if bar3.value > 0 and x >= 6:
        # Get the current time
        current_time1 = pygame.time.get_ticks()
        hunger_bar_text.render(window)

        # Check if 5 seconds have elapsed since the last decrease
        if current_time1 - start_time3 >= 10000 :
            # Decrease the value of bar2 by the decrease amount
            bar3.decrease(decrease_amount)
            
            
            # Reset the start time to the current time
            start_time3 = current_time1   

        bar3.draw(window)  

    
    #text3.render(window)
    pygame.display.update()


    # Limit frame rate
    #clock.tick(60)


pygame.quit()