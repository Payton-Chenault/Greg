# Referenced https://gist.github.com/notalentgeek/48aeab398b6b74e3a9134a61b6b79a36


import aubio
import numpy as np
import pyaudio
import sys

BUFFER_SIZE:int = 2048
CHANNELS:int = 1
FORMAT = pyaudio.paFloat32
METHOD = "default"
SAMPLE_RATE:int = 44100
HOP_SIZE:int = BUFFER_SIZE//2
PERIOD_SIZE_IN_FRAME:int = HOP_SIZE

def main(args):
    p = pyaudio.PyAudio()
    mic = p.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, input=True,frames_per_buffer=PERIOD_SIZE_IN_FRAME)

    p_detection:aubio.pitch = aubio.pitch(METHOD, BUFFER_SIZE, HOP_SIZE, SAMPLE_RATE)

    p_detection.set_unit("Hz")
    p_detection.set_silence(-40)

    while True:
        data:bytes = mic.read(PERIOD_SIZE_IN_FRAME)

        samples:np.ndarray[tuple[int], np.dtype[np.float64]] = np.frombuffer(data, dtype=aubio.float_type)

        pitch = p_detection(samples)[0]

        volume = np.sum(samples**2)/len(samples)

        volume = "{:6f}".format(volume)

        print(str(pitch) + " " + str(volume))

if __name__ == "__main__": main(sys.argv)