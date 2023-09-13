import PySimpleGUI as sg
import time

class Tamagotchi:
    def __init__(self):
        self.hunger = 50
        self.happiness = 50
        self.health = 100
        self.alive = True

    def feed(self):
        if self.hunger < 100:
            self.hunger += 20
            if self.hunger > 100:
                self.hunger = 100
        else:
            sg.popup("Your Tamagotchi is not hungry!")

    def play(self):
        if self.happiness < 100:
            self.happiness += 20
            if self.happiness > 100:
                self.happiness = 100
        else:
            sg.popup("Your Tamagotchi is already happy!")

    def check_health(self):
        if self.hunger < 25 or self.happiness < 25:
            self.health -= 10
            if self.health <= 0:
                self.alive = False
                sg.popup("Your Tamagotchi has died! :(")
                return False
        return True

    def update_display(self, window):
        window["hunger"].update(value=str(self.hunger) + "%")
        window["happiness"].update(value=str(self.happiness) + "%")
        window["health"].update(value=str(self.health) + "%")

def main():
    tamagotchi = Tamagotchi()

    layout = [[sg.Text("Hunger: "), sg.Text(str(tamagotchi.hunger) + "%", key="hunger")],
              [sg.Text("Happiness: "), sg.Text(str(tamagotchi.happiness) + "%", key="happiness")],
              [sg.Text("Health: "), sg.Text(str(tamagotchi.health) + "%", key="health")],
              [sg.Button("Feed"), sg.Button("Play"), sg.Button("Exit")]]

    window = sg.Window("Tamagotchi", layout)

    while True:
        event, values = window.read(timeout=5000)

        if event in (sg.WIN_CLOSED, "Exit"):
            break
        if not tamagotchi.alive:
            break

        if event == "Feed":
            tamagotchi.feed()
        elif event == "Play":
            tamagotchi.play()

        tamagotchi.hunger -= 1
        tamagotchi.check_health()
        tamagotchi.update_display(window)

if __name__ == "__main__":
    main()