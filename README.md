# MouseController
Control the mouse with the keyboard. The controls can be modified. This program is for Windows 10 machines but it is likely that it runs fine on other machines.

<a name="requirements"></a>
## Prerequisites ##
If you want to be able to run this program you must have the following libraries installed on your computer:
- [pynput](https://pypi.org/project/pynput/)

Optional libraries:
- [pyautogui](https://pypi.org/project/PyAutoGUI/)

<a name="set-up"></a>
## Set Up ##
You can modify this code to your liking, for ease of use I have put all of the variables that can be changed into the `__init__()` function of the `MouseController` class. These variables come under the `MODIFY AT WILL` comment. The other variables are for initialisation and should not be modified unless you are changing the code itself.

The `speed` variable determines the number of pixels that the mouse travels per 0.01 seconds. This value can be changed while the code is running to change the speed of the mouse movements.

When changing keybinds I have included a list of keys in a .txt file along with the Python program, to use any of these keys you can use the format `keyboard.Key.[key]` [(reference)](https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key). To include conventional keys replace the `keyboard.Key.[key]` with `keyboard.KeyCode.from_char('[key]')`.

The order of the keybinds is `[ MAIN , UP , DOWN , LEFT , RIGHT , LEFT_CLICK , RIGHT_CLICK ]`.

The variable `toggle` determines whether or not the `MAIN` key acts as a toggle (if set to True) for the mouse controls or if you need to hold it down (if set to False) to be able to use the mouse controls. 

<a name="usage"></a>
## Usage ##
When the `toggle` variable is set to `True` you can press the `MAIN` key to control the mouse using the `UP, DOWN, LEFT, RIGHT, LEFT_CLICK, RIGHT_CLICK` keys and press it again to disable the controls. If the `toggle` variable is set to `False` you have to hold down the `MAIN` key to use these controls.

When the MouseController#start() function is run the code will re-centre the mouse on your screen - this requires [pyautogui](https://pypi.org/project/PyAutoGUI/) to be installed but is not necessary. If you want the code not to re-centre your mouse you can initialise the class with no parameters - e.g. `mouse = MouseController()`.
