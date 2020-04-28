from time import sleep
from Xlib import display


def beep(frequency, amplitude, duration):
    sample = 8000
    half_period = int(sample / frequency / 2)
    beep = chr(amplitude) * half_period + chr(0) * half_period
    beep *= int(duration * frequency)
    audio = open('/dev/audio', 'wb')
    audio.write(beep)
    audio.close()


def generate_mouse_position():
    while True:
        data = display.Display().screen().root.query_pointer()._data
        yield data["root_x"], data["root_y"]


def main():
    coords = generate_mouse_position()
    while True:
        sleep(0.01)
        if next(coords) == (0, 0):
            beep(440, 63, 1)


if __name__ == '__main__':
    main()
