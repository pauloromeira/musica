#!/usr/bin/env python
from itertools import chain
import sounddevice as sd
import matplotlib.pyplot as plt
from utils import frequency, waveform, crossfade
from intervals import semitones, interval
from numpy import math

from intervals import SCALES


rate = 44100
duration = 5
volume = 1
sd.default.samplerate = rate

scale = 'major'

print(scale)
chord = [0, 2, 4]
octaves = 2
notes = chain.from_iterable(
    (n+o*len(SCALES[scale]) for n in chord) for o in range(octaves)
)

wave = None
amplitude = math.sqrt(volume) / (len(chord) * octaves)
for s in semitones(notes, scale):
    f = frequency(s, base=220)
    i = interval(s)
    print(f'{s:02} {f:.2f} Hz : {i[0]} ({i[1]})')
    w = waveform(f, rate, duration, amplitude)
    if wave is None:
        wave = w
    else:
        wave += w


crossfade(wave)
plt.plot(wave)
sd.play(wave)
plt.show()
# sd.wait()
