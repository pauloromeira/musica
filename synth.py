#!/usr/bin/env python
import math
import pyaudio
from array import array
from numbers import Number


player = pyaudio.PyAudio()

major_scale = [0,2,4,5,7,9,11,12]
pentatonic_scale = [0,2,4,7,9,12]
redemption_song = [0,2,4,0,5,9,7,4,0,2,4,7,4,5,4,2,0]


def frequency(steps, base=440):
    return base * math.pow(2.0, steps/12.0)


def linspace(start=0, stop=1, steps=50):
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
    return (math.sin(2.0 * math.pi * r * frequency / rate)
            for r in range(math.ceil(rate * duration)))


def play(steps=major_scale, start=3, base=220, duration=1.0, rate=44100, volume=1):
    stream = player.open(
        format=pyaudio.paFloat32,
        channels=1,
        rate=rate,
        output=True,
    )

    if isinstance(steps, Number):
        steps = [steps]

    for step in steps:
        freq = frequency(start + step, base)
        print(f'{step:02}: {freq:.2f} Hz')

        wave = array('f', (p * volume for p in waveform(freq, rate, duration)))
        crossfade(wave)
        stream.write(wave.tobytes())

    # Empty input to avoid clipping sound
    stream.write(array('f', [0] * (rate // 2)).tobytes())
    stream.stop_stream()
    stream.close()


if __name__ == "__main__":
    import IPython; IPython.embed()
    player.terminate()
