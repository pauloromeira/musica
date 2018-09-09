#!/usr/bin/env python
from itertools import islice, cycle
from numbers import Number


SCALES = {
    'major': (2,2,1,2,2,2,1),
    'minor': (2,1,2,2,1,2,2),
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
    if isinstance(scale, str):
        scale = SCALES[scale]
    if isinstance(notes, Number):
        notes = [notes]

    return (sum(s for s in islice(cycle(scale), n)) for n in notes)


def interval_name(semitones):
    return INTERVAL_NAMES.get(semitones, 'unknown')
