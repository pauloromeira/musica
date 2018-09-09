#!/usr/bin/env python
from itertools import islice, cycle
from numbers import Number


SCALES = {
    'major': (2,2,1,2,2,2,1),
    'minor': (2,1,2,2,1,2,2),
    'chromatic': (1,) * 12,
}

INTERVALS = {
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
    _st = lambda note, scale: sum(s for s in islice(cycle(scale), note))

    if isinstance(scale, str):
        scale = SCALES[scale]

    if isinstance(notes, Number):
        return _st(notes, scale)
    else:
        return [_st(note, scale) for note in notes]
