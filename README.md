# Coordinates Serial Generator

[![Python Version Badge](https://img.shields.io/python/required-version-toml?tomlFilePath=https%3A%2F%2Fraw.githubusercontent.com%2Frichardzone%2Fcoordinates_serial_generator%2Fmaster%2Fpyproject.toml)](https://github.com/richardzone/coordinates_serial_generator/blob/master/pyproject.toml)
[![Build Test Upload Status Badge](https://img.shields.io/github/actions/workflow/status/richardzone/coordinates_serial_generator/python-app-windows.yml?label=Build%20Test%20Upload)](https://github.com/richardzone/coordinates_serial_generator/actions)
[![Code Coverage Badge](https://img.shields.io/codecov/c/github/richardzone/coordinates_serial_generator?label=Code%20Coverage)](https://app.codecov.io/gh/richardzone/coordinates_serial_generator)

This app will emulate eye tracker hardware and send commands to serial port.

Specifically, this app does the following:
1. Randomly select one of 3 types of commands
2. Send the command to serial port (`COM2` by default)
3. Pause for a random interval
4. Repeat

The 3 types of commands are described in the [Eye Tracker App](https://github.com/richardzone/eye-tracker-app) documentation.

## Usage

```log
usage: run.py [-h] [--port PORT] [--rate RATE] [--min-interval MIN_INTERVAL] [--max-interval MAX_INTERVAL]

Serial communication emulator

options:
  -h, --help            show this help message and exit
  --port PORT           Serial port (default: COM2)
  --rate RATE           Baud rate (default: 9600)
  --min-interval MIN_INTERVAL
                        Min interval in milliseconds between commands (default: 500)
  --max-interval MAX_INTERVAL
                        Max interval in milliseconds between commands (default: 4000)
```

