import threading
import time

import MicDetection
import Notifier
from MicDetection import current_volume_db


if __name__ == "__main__":
    listener = threading.Thread(target=MicDetection.audio_listener_thread, daemon=True)
    listener.start()

    print("App Started")

    WARNING_THRESHOLD = -15

    try:
        while True:
            current_vol = MicDetection.current_volume_db

            if current_vol > WARNING_THRESHOLD:
                print(f"Notifying -> {current_vol}")
                Notifier.warn_user()
                time.sleep(.2)

            time.sleep(.1)


    except KeyboardInterrupt:
        print("Closing App")