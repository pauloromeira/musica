#!/usr/bin/env python
import pyaudio
import math
from array import array

player = pyaudio.PyAudio()

major_scale = [0,2,4,5,7,9,11,12]
pentatonic_scale = [0,2,4,7,9,12]
redemption_song = [0,2,4,0,5,9,7,4,0,2,4,7,4,5,4,2,0]


def frequency(n):
    return math.pow(2.0, (n-49.0)/12.0) * 440.0

def linspace(start=0, stop=1, steps=50):
    return (
        start * (1-p) + stop * p for p in
        (i/(steps-1) for i in range(steps))
    )

def crossfade(note, percent=.01):
    n = int(len(note) * percent)
    for i, j, p in zip(range(n), range(-1,-(n+1),-1), linspace(steps=n)):
        note[i] *= p
        note[j] *= p

def play(sequence=major_scale, start=40, duration=1.0, rate=44100, volume=1):
    stream = player.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=rate,
        output=True,
    )

    for s in sequence:
        f = frequency(s + start)
        print(f'{s:02}: {f:.2f} Hz')

        note = array('f', (
            math.sin(2.0 * math.pi * r * f / rate) * volume 
            for r in range(math.ceil(rate * duration))
        ))
        crossfade(note)

        stream.write(note.tobytes())

    # Empty input to avoid clipping sound
    stream.write(array('f', [0] * (rate // 2)).tobytes())
    stream.stop_stream()
    stream.close()

import IPython; IPython.embed()

player.terminate()
