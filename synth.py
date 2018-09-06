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

def play(sequence=major_scale, start=40, duration=1.0, rate=44100, volume=1):
    stream = player.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=rate,
                    output=True)

    for s in sequence:
        f = frequency(s + start)
        print(f'{s:02}: {f:.2f}Hz')

        note = array('f', (
            math.sin(2.0 * math.pi * r * f / rate) * volume 
            for r in range(math.ceil(rate * duration))
        ))

        stream.write(note.tobytes())

    stream.stop_stream()
    stream.close()

import IPython; IPython.embed()

player.terminate()
