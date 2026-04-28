"""
MooseGesture - A mouse gestures recognition library.
By Al Sweigart al@coffeeghost.net
http://coffeeghost.net/2011/05/09/moosegesture-python-mouse-gestures-module

Usage:
    import moosegesture
    gesture = moosegesture.getGesture(points)

Where "points" is a list of x, y coordinate tuples, e.g. [(100, 200), (1234, 5678), ...]
getGesture returns a list of string for the recognized mouse gesture. The strings
correspond to the 8 cardinal and diagonal directions:

    'UL' (up-left), 'U' (up), 'UR' (up-right)
    'L' (left), 'R' (right)
    'DL' (down-left), 'D' (down), 'DR' (down-right)

Second usage:
    strokes  = ['D', 'L', 'R']
    gestures = [['D', 'L', 'D'], ['D', 'R', 'UR']]
    gesture = moosegesture.findClosestMatchingGesture(strokes, gestures)

    gesture == ['D', 'L', 'D']

Where "strokes" is a list of the directional integers that are returned from
getGesture(). This returns the closest resembling gesture from the list of
gestures that is passed to the function.

The optional "tolerance" parameter can ensure that the "closest" identified
gesture isn't too different.


Explanation of the nomenclature in this module:
    A "point" is a 2D tuple of x, y values. These values can be ints or floats,
    MooseGesture supports both.

    A "point pair" is a point and its immediately subsequent point, i.e. two
    points that are next to each other.

    A "segment" is two or more ordered points forming a series of lines.

    A "stroke" is a segment going in a single direction (one of the 8 cardinal or
    diagonal directions: up, upright, left, etc.)

    A "gesture" is one or more strokes in a specific pattern, e.g. up then right
    then down then left.


"""

__version__ = '1.0.2'

import doctest

from math import sqrt

# This is the minimum distance the mouse must travel (in pixels) before a
# segment will be considered for stroke interpretation.
_MIN_STROKE_LEN = 60

DOWNLEFT = 'DL'
DOWN = 'D'
DOWNRIGHT = 'DR'
LEFT = 'L'
RIGHT = 'R'
UPLEFT = 'UL'
UP = 'U'
UPRIGHT = 'UR'

def getGesture(points):
    """
    Returns a gesture as a list of directions, i.e. ['U', 'DL'] for
    the down-left-right gesture.

    The `points` parameter is a list of (x, y) tuples of points that make up
    the user's mouse gesture.
    """
    pass


def getSegments(points):
    """
    Returns a list of tuples of integers. The tuples are the start and end
    indexes of the points that make up a consistent stroke.
    """
    pass


def getGestureAndSegments(points):
    """
    Returns a list of tuples. The first item in the tuple is the directional
    integer, and the second item is a tuple of integers for the start and end
    indexes of the points that make up the stroke.
    """
    pass


def findClosestMatchingGesture(strokes, gestureList, maxDifference=None):
    """
    Returns the gesture(s) in `gestureList` that closest matches the gesture in
    `strokes`. The `maxDifference` is how many differences there can be and still
    be considered a match.
    """
    pass


def levenshteinDistance(s1, s2):
    """
    Returns the Levenshtein Distance between two strings, `s1` and `s2` as an
    integer.

    http://en.wikipedia.org/wiki/Levenshtein_distance
    The Levenshtein Distance (aka edit distance) is how many changes (i.e.
    insertions, deletions, substitutions) have to be made to convert one
    string into another.

    For example, the Levenshtein distance between "kitten" and "sitting" is
    3, since the following three edits change one into the other, and there
    is no way to do it with fewer than three edits:
      kitten -> sitten -> sittin -> sitting
    """
    pass


def _identifyStrokes(points):
    pass

def _getDirection(coord1, coord2):
    """
    Return the direction the line formed by the (x, y)
    points in `coord1` and `coord2`.
    """
    pass

def _distance(coord1, coord2):
    """
    Return the distance between two points, `coord1` and `coord2`. These
    parameters are assumed to be (x, y) tuples.
    """
    pass
