# Client script (Run this on your Windows machine)

import socket
from pynput import mouse, keyboard

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 12345

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

# Mouse and keyboard controllers
mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

print("KVM Client started. Waiting for commands...")

while True:
    data, addr = sock.recvfrom(1024)
    command = data.decode().split()

    if command[0] == "MOVE":
        mouse_controller.position = (int(command[1]), int(command[2]))
    elif command[0] == "CLICK":
        button = mouse.Button.left if command[3] == "Button.left" else mouse.Button.right
        mouse_controller.position = (int(command[1]), int(command[2]))
        if command[4] == "True":
            mouse_controller.press(button)
        else:
            mouse_controller.release(button)
    elif command[0] == "SCROLL":
        mouse_controller.scroll(int(command[3]), int(command[4]))
    elif command[0] == "PRESS":
        key = keyboard.KeyCode.from_char(command[1]) if len(command[1]) == 1 else keyboard.Key[command[1]]
        keyboard_controller.press(key)
    elif command[0] == "RELEASE":
        key = keyboard.KeyCode.from_char(command[1]) if len(command[1]) == 1 else keyboard.Key[command[1]]
        keyboard_controller.release(key)