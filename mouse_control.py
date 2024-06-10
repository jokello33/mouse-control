import pynput
from pynput.mouse import Controller, Listener, Button
import logging

# Set up logging
log_dir = r'/Users/jacobo/Desktop/projects'
logging.basicConfig(filename=(log_dir + r"/mouse_control.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Instantiate the mouse controller
mouse = Controller()

# Define the control function to handle mouse events
def control(x, y, button, pressed):
    if pressed:
        mouse.position = (0, 0)
        mouse.click(button)

# Define an on_move callback function for demonstration
def on_move(x, y):
    logging.info(f'Mouse moved to ({x}, {y})')

# Define an on_click callback function to log mouse clicks
def on_click(x, y, button, pressed):
    if pressed:
        logging.info(f'Mouse clicked at ({x}, {y}) with {button}')
        print(f'Mouse clicked at ({x}, {y}) with {button}')

# Start listening to mouse events
with Listener(on_move=on_move, on_click=on_click) as listener:
    listener.join()

