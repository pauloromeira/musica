#!/usr/bin/env python
from itertools import islice, cycle
from numbers import Number


SCALES = {
    'major': (2,2,1,2,2,2,1),
    'minor': (2,1,2,2,1,2,2),
    'major pentatonic': (2,2,3,2,3),
    'minor pentatonic': (3,2,2,3,2),
    'chromatic': (1,) * 11,
}

INTERVAL_NAMES = [
    'unison',
    'minor second',
    'major second',
    'minor third',
    'major third',
    'perfect fourth',
    'augmented fourth/diminished fifth', # tritone
    'perfect fifth',
    'minor sixth',
    'major sixth',
    'minor seventh',
    'major seventh',
]


def semitones(notes, scale='major'):
    if isinstance(scale, str):
        scale = SCALES[scale]

    _semi = lambda note, scale: sum(s for s in islice(cycle(scale), note))
    if isinstance(notes, Number):
        return _semi(notes, scale)
    else:
        return (_semi(n, scale) for n in notes)


def interval(semitones):
    intervals_count = len(INTERVAL_NAMES)
    octaves = semitones // intervals_count
    interval = semitones % intervals_count if octaves else semitones
    return INTERVAL_NAMES[interval], octaves
