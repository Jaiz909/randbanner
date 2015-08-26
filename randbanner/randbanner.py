#!/usr/bin/env python
__author__ = 'Jai Grimshaw'
import argparse
import os
import sys
from pyfiglet import Figlet
from clint.textui import colored, puts
from random import choice

# Big list of cool fonts, hand curated from pyfiglet's extensive library.
font_list = ['stellar', 'puffy', 'diamond', 'smslant', 'rounded', 'alligator',
             'fender', 'colossal', 'sansb', 'bigchief', 'sblood',
             'cybermedium', 'gothic', 'roman', 'os2', 'r2-d2___', 'standard',
             'double', 'banner3', 'com_sen_', 'peaks', 'mirror', 'timesofl',
             'univers', 'banner3-D', 'isometric1', 'smisome1', 'letters',
             '5lineoblique', 'eftiwater', 'script', 'fourtops', 'threepoint',
             'larry3d', 'slscript', 'starwars', 'barbwire', 'bulbhead',
             'cosmic', 'nipples', 'gradient', 'rowancap', 'thin', 'smscript',
             'cosmike', 'computer', 'straight', 'usaflag', 'o8', 'lockergnome',
             'pepper', 'serifcap', 'contessa', 'weird', 'catwalk', 'pebbles',
             'eftirobot', 'shadow', 'chunky', 'graffiti', 'tanja',
             'cyberlarge', 'drpepper', 'alligator2', 'stacey', 'poison',
             'smshadow', 'speed', 'epic', 'cybersmall', 'ogre', 'cricket',
             'whimsy', 'crawford', 'trek', 'gothic', 'contrast', 'thick',
             'marquee', 'rectangles', 'tombstone', 'ticksslant', 'coinstak',
             'lean', '3-d', 'bell', 'jazmine']

colours = [colored.blue, colored.green,
           colored.magenta, colored.red, colored.yellow]
bold_options = [True, False]


def make_banner(text, font=font_list[0], colour=colours[0], bold=False):
    f = Figlet(font=font)
    text = f.renderText(text)
    coloured_text = colour(text, False, bold=bold)
    return coloured_text

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--all', '-a', action='store_true',
                        dest='display_all', help='Display all fonts')
    parser.add_argument('-t', '--text', dest='text',
                        default=os.getenv('USER', default='me'), help='Text to display')
    args = parser.parse_args()
    bold = choice(bold_options)
    if args.display_all:
        for font in font_list:
            colour = choice(colours)
            puts(make_banner(args.text, font, colour, bold))
    else:
        font = choice(font_list)
        colour = choice(colours)
        puts(make_banner(args.text, font, colour, bold))

if __name__ == '__main__':
   main()
