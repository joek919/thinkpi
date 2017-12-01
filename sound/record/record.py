"""
PyAudio example: Record a few seconds of audio and save to a WAVE
file.
"""

import pyaudio
import wave
import sys
from ctypes import *

ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
  pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)
asound = cdll.LoadLibrary('libasound.so')
# Set error handler
asound.snd_lib_error_set_handler(c_error_handler)

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

if sys.platform == 'darwin':
    CHANNELS = 1

p = pyaudio.PyAudio()

print(p.get_default_input_device_info())

for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print((i,dev['name'],dev['maxInputChannels']))


stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


frameCount = int(RATE / CHUNK * RECORD_SECONDS)
print(frameCount)

frames = []
print("* recording")
for i in range(0, frameCount):
    data = stream.read(CHUNK)
    frames.append(data)
    print i,"/",frameCount,"  \r",
    sys.stdout.flush()
print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
frames = []
print("* recording2")
for i in range(0, frameCount):
    data = stream.read(CHUNK)
    frames.append(data)
    print i,"/",frameCount,"  \r",
    sys.stdout.flush()
print("* done recording2")
stream.stop_stream()
stream.close()
p.terminate()


# Set error handler
asound.snd_lib_error_set_handler(None)

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
