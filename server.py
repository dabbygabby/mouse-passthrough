import socket
from pynput import mouse, keyboard

# Change this to the IP address of your Windows machine
WINDOWS_IP = '192.168.1.100'  
PORT = 12345

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Mouse controller
mouse_controller = mouse.Controller()

def on_move(x, y):
    sock.sendto(f"MOVE {x} {y}".encode(), (WINDOWS_IP, PORT))

def on_click(x, y, button, pressed):
    sock.sendto(f"CLICK {x} {y} {button} {pressed}".encode(), (WINDOWS_IP, PORT))

def on_scroll(x, y, dx, dy):
    sock.sendto(f"SCROLL {x} {y} {dx} {dy}".encode(), (WINDOWS_IP, PORT))

# Keyboard controller
keyboard_controller = keyboard.Controller()

def on_press(key):
    sock.sendto(f"PRESS {key}".encode(), (WINDOWS_IP, PORT))

def on_release(key):
    sock.sendto(f"RELEASE {key}".encode(), (WINDOWS_IP, PORT))

# Start listening to the mouse and keyboard
mouse_listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
keyboard_listener = keyboard.Listener(on_press=on_press, on_release=on_release)

mouse_listener.start()
keyboard_listener.start()

print("KVM Server started. Press Ctrl+C to exit.")

try:
    mouse_listener.join()
    keyboard_listener.join()
except KeyboardInterrupt:
    print("KVM Server stopped.")