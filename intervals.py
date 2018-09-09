#!/usr/bin/env python
from itertools import islice, cycle
from numbers import Number


SCALES = {
    'major': (2,2,1,2,2,2,1),
    'minor': (2,1,2,2,1,2,2),
    'major pentatonic': (2,2,3,2,3),
    'minor pentatonic': (3,2,2,3,2),
    'chromatic': (1,) * 12,
}

INTERVAL_NAMES = {
    0: 'perfect unison',
    1: 'minor second',
    2: 'major second',
    3: 'minor third',
    4: 'major third',
    5: 'perfect fourth',
    6: 'augmented fourth/diminished fifth', # tritone
    7: 'perfect fifth',
    8: 'minor sixth',
    9: 'major sixth',
    10: 'minor seventh',
    11: 'major seventh',
    12: 'perfect octave',
}


def semitones(notes, scale='major'):
    _semi = lambda note, scale: sum(s for s in islice(cycle(scale), note))

    if isinstance(scale, str):
        scale = SCALES[scale]
    if isinstance(notes, Number):
        return _semi(notes, scale)
    else:
        return (_semi(n, scale) for n in notes)


def interval_name(semitones):
    return INTERVAL_NAMES.get(semitones, 'unknown')
