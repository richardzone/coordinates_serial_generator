import time
import random
from typing import Tuple
import argparse

import serial


def get_screen_size() -> Tuple[int, int]:
    # Using tkinter to get screen size
    import tkinter as tk
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height


def generate_random_coordinates(screen_width: int, screen_height: int) -> Tuple[int, int]:
    return [random.randint(0, screen_width), random.randint(0, screen_height)]


def main():

    parser = argparse.ArgumentParser(description='Serial communication emulator')
    parser.add_argument('--port', default='COM2', help='Serial port (default: COM2)')
    args, _ = parser.parse_known_args()
    port = args.port

    screen_width, screen_height = get_screen_size()
    with serial.Serial(port, 9600, timeout=1) as ser:
        while True:
            coordinates = list(generate_random_coordinates(screen_width, screen_height))
            encoded_text = str(coordinates).encode()
            ser.write(str(coordinates).encode())
            print(f"Sent to {port}: {encoded_text}\n")
            time.sleep(random.uniform(0.5, 4))


if __name__ == '__main__':
    main()
