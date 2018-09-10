#!/usr/bin/env python
import sounddevice as sd
from utils import frequency, waveform, crossfade
from intervals import semitones, interval


rate = 44100
duration = 1
volume = 1

sd.default.samplerate = rate

scale = 'major'

print(scale)
for s in semitones(range(8), scale):
    f = frequency(s)
    i = interval(s)
    print(f'{s:02} {f:.2f} Hz : {i[0]} ({i[1]})')
    wave = waveform(f, rate, duration, volume)
    crossfade(wave)
    sd.play(wave, blocking=True)
