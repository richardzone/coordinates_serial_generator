import time
import random
from typing import Tuple, List
import argparse
import serial
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def get_command(self) -> str:
        pass

class RandomCoordinatesCommand(Command):
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def generate_random_coordinates(self) -> Tuple[int, int]:
        return random.randint(0, self.screen_width), random.randint(0, self.screen_height)

    def get_command(self) -> str:
        coordinates = self.generate_random_coordinates()
        return str(coordinates)

class CalibrationRequiredCommand(Command):
    def get_command(self) -> str:
        return "calibration_required"

class CalibrationDoneCommand(Command):
    def get_command(self) -> str:
        return "calibration_done"

def get_screen_size() -> Tuple[int, int]:
    # Using tkinter to get screen size
    import tkinter as tk
    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height

def main():
    parser = argparse.ArgumentParser(description='Serial communication emulator')
    parser.add_argument('--port', default='COM2', help='Serial port (default: COM2)')
    parser.add_argument('--rate', type=int, default=9600, help='Baud rate (default: 9600)')
    parser.add_argument('--min-interval', type=int, default=500, help='Min interval in milliseconds between commands (default: 500)')
    parser.add_argument('--max-interval', type=int, default=4000, help='Max interval in milliseconds between commands (default: 4000)')
    args, _ = parser.parse_known_args()
    port = args.port
    rate = args.rate
    min_interval = args.min_interval
    max_interval = args.max_interval

    screen_width, screen_height = get_screen_size()
    commands: List[Command] = [
        RandomCoordinatesCommand(screen_width, screen_height),
        CalibrationRequiredCommand(),
        CalibrationDoneCommand()
    ]

    # Assign weights for each command
    weights = [1, 1, 1]

    with serial.Serial(port, rate, timeout=0) as ser:
        while True:
            # Choose a command based on the assigned weights
            command = random.choices(commands, weights=weights)[0]
            command_str = command.get_command()
            ser.write(command_str.encode())
            ser.flush()
            sleep_duration = random.uniform(min_interval / 1000, max_interval / 1000)
            print(f"Sent to {port}: {command_str}. Now sleeping for {sleep_duration:.2f} seconds\n")
            time.sleep(sleep_duration)

if __name__ == '__main__':
    main()
