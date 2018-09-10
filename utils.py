#!/usr/bin/env python
import numpy as np
from numpy import math


def frequency(steps, start=-9, base=440.0):
    return base * math.pow(2.0, (start + steps)/12.0)


def crossfade(wave, percent=.1):
    n = int(len(wave) * percent / 2)
    weight = lambda i: math.pow(i, 2)
    i_max = weight(n)
    for i in range(n):
        amp = weight(i) / i_max
        wave[i] *= amp
        wave[-(i+1)] *= amp


def waveform(frequency, rate, duration=1, amplitude=1):
    count = math.ceil(rate * duration)
    return np.fromiter(
        (math.sin(2.0 * math.pi * r * frequency / rate) * amplitude
         for r in range(count)),
        dtype=np.float32,
        count=count
    )

