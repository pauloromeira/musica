#!/usr/bin/env python
import math
import numpy as np
import sounddevice as sd

rate = 44100
freq = 440
duration = 2

sd.default.samplerate = rate

def waveform(frequency, rate, duration):
    return np.array([
        math.sin(2.0 * math.pi * r * frequency / rate)
        for r in range(math.ceil(rate * duration))
    ])

wave = waveform(freq, rate, duration)
sd.play(wave, blocking=True)
