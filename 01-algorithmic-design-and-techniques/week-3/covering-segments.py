#!/user/bin/python

'''Covering Segments by Points
Given a set of n segments with integer coordinates on a line, find the min
number m points such that each segment contains at least one point.


'''

import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments.sort(key=lambda s:s.end)
    seg_end = None

    for s in segments:
        if seg_end is None or s.start > seg_end:
            seg_end = s.end
            points.append(s.end)
        else:
            continue
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
