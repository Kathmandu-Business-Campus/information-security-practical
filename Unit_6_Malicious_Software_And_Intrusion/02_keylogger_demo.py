"""
Safe Keylogger Demonstration
Logs key presses while the script is running.
Does NOT run in background; stops when the script is closed.
"""

from pynput import keyboard

log = []

def on_press(key):
    try:
        log.append(key.char)  # normal characters
        print(f"Key pressed: {key.char}")
    except AttributeError:
        # special keys (e.g., space, enter)
        log.append(str(key))
        print(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener when ESC is pressed
        print("\nESC pressed. Stopping keylogger...")
        return False

# Start keylogger (runs only in foreground)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger running... Press ESC to stop.")
    listener.join()

# After stopping, show logged keys
print("\nLogged keys during this session:")
print("".join(log))
