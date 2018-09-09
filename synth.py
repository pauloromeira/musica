#!/usr/bin/env python
import sounddevice as sd
from utils import frequency, waveform, crossfade
from intervals import semitones


rate = 44100
duration = 1

sd.default.samplerate = rate

for s in semitones(range(8)):
    print(s)
    f = frequency(s)
    wave = waveform(f, rate, duration)
    crossfade(wave)
    sd.play(wave, blocking=True)
