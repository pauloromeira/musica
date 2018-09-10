#!/usr/bin/env python
import sounddevice as sd
import matplotlib.pyplot as plt
from utils import frequency, waveform, crossfade
from intervals import semitones, interval
from numpy import math


rate = 44100
duration = 5
volume = 1
sd.default.samplerate = rate

scale = 'minor'

print(scale)
notes = [0,2,4,6]

wave = None
amplitude = math.sqrt(volume) / len(notes)
for s in semitones(notes, scale):
    f = frequency(s)
    i = interval(s)
    print(f'{s:02} {f:.2f} Hz : {i[0]} ({i[1]})')
    w = waveform(f, rate, duration, amplitude)
    if wave is None:
        wave = w
    else:
        wave += w


    # sd.play(wave, blocking=True)
crossfade(wave)
plt.plot(wave[:rate//2])
sd.play(wave, blocking=True)
plt.show()
