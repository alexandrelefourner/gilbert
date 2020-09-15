"""
Original code from Jakub Červený.
https://github.com/jakubcerveny/gilbert
Adapted by Alexandre A. LE FOURNER to get a numpy array.
"""

import numpy as np

def sgn(x):
    return (x > 0) - (x < 0)


def gilbert2d(x, y, ax, ay, bx, by):
    """
    Generalized Hilbert ('gilbert') space-filling curve for arbitrary-sized
    2D rectangular grids.
    """

    w = int(abs(ax + ay))
    h = int(abs(bx + by))

    (dax, day) = (sgn(ax), sgn(ay)) # unit major direction
    (dbx, dby) = (sgn(bx), sgn(by)) # unit orthogonal direction

    mlist = []
    if h == 1:
        # trivial row fill
        for i in range(0, w):
            mlist.append((int(x), int(y)))
            (x, y) = (x + dax, y + day)
        return mlist

    if w == 1:
        # trivial column fill
        for i in range(0, h):
            mlist.append((int(x), int(y)))
            (x, y) = (x + dbx, y + dby)
        return mlist

    (ax2, ay2) = (ax/2, ay/2)
    (bx2, by2) = (bx/2, by/2)

    w2 = abs(ax2 + ay2)
    h2 = abs(bx2 + by2)

    if 2*w > 3*h:
        if (w2 % 2) and (w > 2):
            # prefer even steps
            (ax2, ay2) = (ax2 + dax, ay2 + day)

        # long case: split in two parts only
        mlist = mlist + gilbert2d(x, y, ax2, ay2, bx, by)
        mlist = mlist + gilbert2d(x+ax2, y+ay2, ax-ax2, ay-ay2, bx, by)

    else:
        if (h2 % 2) and (h > 2):
            # prefer even steps
            (bx2, by2) = (bx2 + dbx, by2 + dby)

        # standard case: one step up, one long horizontal, one step down
        mlist = mlist + gilbert2d(x, y, bx2, by2, ax2, ay2)
        mlist = mlist + gilbert2d(x+bx2, y+by2, ax, ay, bx-bx2, by-by2)
        mlist = mlist + gilbert2d(x+(ax-dax)+(bx2-dbx), y+(ay-day)+(by2-dby),
                 -bx2, -by2, -(ax-ax2), -(ay-ay2))
    return mlist

def numpy_gilbert2d(width, height):
    """
    returns a numpy array of girlbert for easy data transformation.
    """
	
    if width >= height:
        return np.array(gilbert2d(0, 0, width, 0, 0, height))
    else:
        return np.array(gilbert2d(0, 0, 0, height, width, 0))
