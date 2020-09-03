from tod.common.datetime_ import datetime
import os
import sys

__author__ = 'SLCIT inc'
__email__ = 'simoncharest@gmail.com'
__copyright__ = f'Copyright © {datetime.get_years(2020)} {__author__} <{__email__}>. All rights reserved.'
__project__ = 'Tunnels of Doom'
__credits__ = [
    'Kevin Kenney',
    'Texas Instruments'
    'TI-99/4A'
    'Paul Vincent Craven',
    'The Python Arcade Library',
    'https://arcade.academy/',
    '@professorcraven',
    'Opensource.com'
]
__license__ = 'GNU'
__maintainer__ = 'Simon Charest'
__status__ = 'Developement'
__version__ = '1.0.0'

ROOT_DIR = os.path.dirname(sys.modules['__main__'].__file__)
HEIGHT = 600
WIDTH = 800

"""
Sources:
    How to create a 2D game with Python and the Arcade library (https://opensource.com/article/18/4/easy-2d-game-creation-python-and-arcade)
"""
