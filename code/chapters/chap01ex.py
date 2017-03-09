"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

from modules import nsfg

import sys


def main(script):
    """Tests the functions in this module.
    script: string script name
    """
    print('%s: All tests passed.' % script)
    df = nsfg.ReadFemPreg()

    print(df.pregordr[0])



if __name__ == '__main__':
    main(*sys.argv)
