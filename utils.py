#!/usr/bin/env python
import numpy as np
from numpy import math


def frequency(steps, start=-9, base=440.0):
    return base * math.pow(2.0, (start + steps)/12.0)


def linspace(start=0.0, stop=1.0, steps=50):
    return (
        start * (1-p) + stop * p for p in
        (i/(steps-1) for i in range(steps))
    )


def crossfade(wave, percent=.01):
    n = int(len(wave) * percent)
    for i, j, p in zip(range(n), range(-1,-(n+1),-1), linspace(steps=n)):
        wave[i] *= p
        wave[j] *= p


def waveform(frequency, rate, duration):
    count = math.ceil(rate * duration)
    return np.fromiter(
        (math.sin(2.0 * math.pi * r * frequency / rate) for r in range(count)),
        dtype=np.float32,
        count=count
    )

