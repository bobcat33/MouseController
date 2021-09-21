from pynput import keyboard
from pynput.mouse import Controller, Button
import threading
from time import sleep

using_pyautogui = True
try:
    import pyautogui
except:
    using_pyautogui = False

class MouseController:
    def __init__(self, recentre=True):
        # DO NOT MODIFY ------------------
        self.alt_down = False
        self.pressing = [False] * 5
        self.active = False
        self.mouse = Controller()
        self.can_recentre = recentre

        # MODIFY AT WILL -----------------

        # Number of pixels that the mouse travels per 0.01 seconds
        # (can be changed while the code is running to change the speed of the mouse movements should you wish)
        self.speed = 5
        
        # Keybind order: [ MAIN , UP , DOWN , LEFT , RIGHT , CLICK ]
        self.keybinds = [keyboard.Key.print_screen, keyboard.Key.up, keyboard.Key.down, keyboard.Key.left, keyboard.Key.right, keyboard.Key.ctrl_r]
        # With toggle set to True the user can enable the mouse control by pressing the MAIN key, when set
        # to false the user has to hold down the MAIN key in order to use the mouse controls
        self.toggle = True

    def start(self):
        if not self.active == True:
            self.active = True
            self.create_thread()
            if self.can_recentre == True:
                self.recentre()
            self.start_listener()
    
    def create_thread(self):
        self.input_listener = threading.Thread(target=self.controller)
        self.input_listener.start()

    def controller(self):
        while True:
            if self.pressing[0] == True:
                self.mouse.move(0,-1 * self.speed)
            if self.pressing[1] == True:
                self.mouse.move(0,self.speed)
            if self.pressing[2] == True:
                self.mouse.move(-1 * self.speed,0)
            if self.pressing[3] == True:
                self.mouse.move(self.speed,0)
            sleep(0.01)
    
    def start_listener(self):
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()

    # pynput keyboard listener event functions
    def on_press(self, key):
        if self.alt_down == True:
            if key == self.keybinds[1] and self.pressing[0] == False:
                self.pressing[0] = True
            elif key == self.keybinds[2] and self.pressing[1] == False:
                self.pressing[1] = True
            elif key == self.keybinds[3] and self.pressing[2] == False:
                self.pressing[2] = True
            elif key == self.keybinds[4] and self.pressing[3] == False:
                self.pressing[3] = True
            elif key == self.keybinds[5] and self.pressing[4] == False:
                self.pressing[4] = True
                self.mouse.press(Button.left)

        elif key == self.keybinds[0] and self.toggle != True:
            self.alt_down = True
            print("MOUSE ACTIVE")

    def on_release(self, key):
        if key == self.keybinds[0]:
            if self.toggle == True:
                if self.alt_down == True:
                    self.alt_down = False
                    self.pressing = [False] * len(self.pressing)
                    print("MOUSE OFF")
                else:
                    self.alt_down = True
                    print("MOUSE ACTIVE")
            else:
                self.alt_down = False
                self.pressing = [False] * len(self.pressing)
                print("MOUSE OFF")

        elif key == self.keybinds[1]:
            self.pressing[0] = False
        elif key == self.keybinds[2]:
            self.pressing[1] = False
        elif key == self.keybinds[3]:
            self.pressing[2] = False
        elif key == self.keybinds[4]:
            self.pressing[3] = False
        elif key == self.keybinds[5]:
            self.pressing[4] = False
            self.mouse.release(Button.left)

    # Movement functions
    def move_to(self, x, y):
        self.mouse.position = (x,y)

    def recentre(self):
        if self.can_recentre == True:
            width, height = pyautogui.size()
            self.move_to(round(width/2), round(height/2))

if __name__ == "__main__":
    mouse = MouseController(recentre=using_pyautogui)
    
    mouse.start()
