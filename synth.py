#!/usr/bin/env python
import sounddevice as sd
from utils import frequency, waveform, crossfade
from intervals import semitones, interval_name


rate = 44100
duration = 1

sd.default.samplerate = rate

scale = 'major pentatonic'

print(scale)
for s in semitones(range(6), scale):
    f = frequency(s)
    print(f'{s:02} {f:.2f} Hz : {interval_name(s)}')
    wave = waveform(f, rate, duration)
    crossfade(wave)
    sd.play(wave, blocking=True)
