from pynput import mouse, keyboard
from pynput.keyboard import Key, Controller
from datetime import datetime

import time

inactivity_timeout = 590  # Screen locks up after 10 minutes of inactivity, so run every 9 minutes and 50 seconds
key_to_press = Key.ctrl_r # Hopefully the key that could hypothetically cause the least harm
last_activity_time = time.time()


def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")


def get_current_time():
    return datetime.now().strftime("%H:%M:%S")


def log_activity(message):
    with open(f"Logs/keypress-log-{get_current_date()}.txt", "a") as log_file:
        log_file.write(message)


def on_mouse_move(x, y):
    global last_activity_time
    last_activity_time = time.time()


def on_mouse_click(x, y, button, pressed):
    global last_activity_time
    last_activity_time = time.time()


def on_mouse_scroll(x, y, dx, dy):
    global last_activity_time
    last_activity_time = time.time()


def on_keyboard_press(key):
    global last_activity_time
    last_activity_time = time.time()


def on_keyboard_release(key):
    pass


def main():
    start_message = f"Program started at {get_current_time()}.\n"
    log_activity(start_message)

    keyboard_controller = Controller()
    mouse_listener = mouse.Listener(on_move=on_mouse_move, on_click=on_mouse_click, on_scroll=on_mouse_scroll)
    keyboard_listener = keyboard.Listener(on_press=on_keyboard_press, on_release=on_keyboard_release)

    mouse_listener.start()
    keyboard_listener.start()

    while True:
        current_time = time.time()

        if current_time - last_activity_time > inactivity_timeout:
            keyboard_controller.press(key_to_press)
            keyboard_controller.release(key_to_press)
            log_activity(f"Inactivity timeout - {key_to_press.name} pressed at {get_current_time()}.\n")

        time.sleep(1)


if __name__ == "__main__":
    main()
