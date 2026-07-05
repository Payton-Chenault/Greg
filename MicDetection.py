# Referenced https://gist.github.com/notalentgeek/48aeab398b6b74e3a9134a61b6b79a36


import aubio
import numpy as np
import pyaudio
import sys

BUFFER_SIZE = 2048
CHANNELS = 1
FORMAT = pyaudio.paFloat32
METHOD = "default"
SAMPLE_RATE = 44100
HOP_SIZE = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME = HOP_SIZE
SILENCE_THRESHOLD = -40

current_volume_db = -100.0

def audio_listener_thread():
    global current_volume_db
    p = pyaudio.PyAudio()

    try:
        mic = p.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, input=True,frames_per_buffer=PERIOD_SIZE_IN_FRAME)
    except Exception as e:
        print(f"Failed to open mic: {e}")
        return

    p_detection:aubio.pitch = aubio.pitch(METHOD, BUFFER_SIZE, HOP_SIZE, SAMPLE_RATE)
    p_detection.set_unit("Hz")
    p_detection.set_silence(SILENCE_THRESHOLD)

    try:
        while True:
            data:bytes = mic.read(PERIOD_SIZE_IN_FRAME, exception_on_overflow=False)

            samples = np.frombuffer(data, dtype=aubio.float_type)

            pitch = p_detection(samples)[0]

            rms_volume = np.sqrt(np.mean(samples**2))

            current_volume_db = 20 * np.log10(max(rms_volume, 1e-10))


    except KeyboardInterrupt:
        print("\nStopping audio stream")

    finally:
        if mic.is_active():
            mic.stop_stream()
        mic.close()
        p.terminate()