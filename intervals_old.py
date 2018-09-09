#!/usr/bin/env python
from numbers import Number
from itertools import cycle, islice
from collections import deque, defaultdict

# |1|_|2|_|3|4|_|5|_|6|_| 7| 8|
# |0|_|2|_|4|5|_|7|_|9|_|11|12| # intevals
major_scale = [2,2,1,2,2,2,1]
# minor_scale = [2,1,2,2,1,2,2]
# chromatic_scale = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def semitones(notes, scale=major_scale):
    def _semitones(note, scale):
        return sum(s for s in islice(cycle(scale), note-1))
    if isinstance(notes, Number):
        return _semitones(notes, scale)
    else:
        return [_semitones(note, scale) for note in notes]


interval_names = {
    0: 'perfect unison',
    1: 'minor second',
    2: 'major second',
    3: 'minor third',
    4: 'major third',
    5: 'perfect fourth',
    6: 'augmented fourth/diminished fifth (aka "tritone")',
    7: 'perfect fifth',
    8: 'minor sixth',
    9: 'major sixth',
    10: 'minor seventh',
    11: 'major seventh',
    12: 'perfect octave',
}

notes = deque([5,3,6,1,2,8,4,7])
# notes.extend(range(9,16)) # +1 octave
# notes.extend(range(16,23)) # +2 octave

stack = deque()
combinations = []

stack.append(notes.popleft())
while notes:
    note = notes.popleft()
    for st in stack:
        combinations.append((st, note))
    stack.appendleft(note)

print('\nTrain')
training = []
interval_types = defaultdict(list)
for combination in combinations:
    distance = semitones(max(combination)) - semitones(min(combination))
    interval_name = interval_names.get(distance)
    interval_types[distance].append(sorted(combination))
    if interval_name:
        print(f'{combination} {tuple(reversed(combination))} [{distance}] {interval_name}')
        training.append((combination, interval_name))

print('\nFrequency')
for distance, intervals in sorted(interval_types.items(), key=lambda i: len(i[1]), reverse=True):
    interval_name = interval_names.get(distance)
    if interval_name:
        print(f'{len(intervals)} > {interval_name} [{distance}]')
        for interval in intervals:
            print(f'  {tuple(interval)} {tuple(reversed(interval))}')
