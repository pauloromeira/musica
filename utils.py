#!/usr/bin/env python
import numpy as np
from numpy import math


def frequency(steps, start=-9, base=440.0):
    return base * math.pow(2.0, (start + steps)/12.0)


def crossfade(wave, percent=.2):
    n = int(len(wave) * percent / 2)
    n_sqrt = math.sqrt(n)
    for i in range(n):
        amp = math.sqrt(i) / n_sqrt
        wave[i] *= amp
        wave[-(i+1)] *= amp


def waveform(frequency, rate, duration=1, volume=1):
    count = math.ceil(rate * duration)
    return np.fromiter(
        (math.sin(2.0 * math.pi * r * frequency / rate) * math.sqrt(volume)
         for r in range(count)),
        dtype=np.float32,
        count=count
    )

