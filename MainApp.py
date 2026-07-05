import threading
import time
import MicDetection
import Notifier
import pystray

from PIL import Image
from pystray import MenuItem as item
from MicDetection import current_volume_db
from RandomAsset import get_random_picture_path
from ResourceUtil import resource_path

is_running = True
def quit_app(icon):
    global is_running
    is_running = False
    icon.stop()

def setup():
    image = Image.open(resource_path(get_random_picture_path())).resize((64, 64))
    menu = pystray.Menu(item('Quit', quit_app))

    icon = pystray.Icon("VolumeMonitor", image, "Too Loud Monitor", menu)
    icon.run()

if __name__ == "__main__":
    tray_thread = threading.Thread(target=setup, daemon=True)
    tray_thread.start()

    listener = threading.Thread(target=MicDetection.audio_listener_thread, daemon=True)
    listener.start()

    print("App Started")

    WARNING_THRESHOLD = -15
    COOLDOWN_SECONDS = 10.0
    last_warning_time = 0.0

    try:
        while is_running:
            current_vol = MicDetection.current_volume_db
            current_time = time.time()

            if current_vol > WARNING_THRESHOLD and (current_time - last_warning_time) > COOLDOWN_SECONDS:
                print(f"Notifying -> {current_vol}")
                last_warning_time = time.time()
                Notifier.warn_user()


            time.sleep(.1)
    except KeyboardInterrupt:
        pass