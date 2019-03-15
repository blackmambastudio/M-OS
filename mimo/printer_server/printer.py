#!/usr/bin/env python

from __future__ import print_function

from Adafruit_Thermal import *
import HTMLParser
from unidecode import unidecode


# Initialize printer
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)


def mimo_printer_init():
    title = 'Welcome to MiMo v4'
    subtitle = 'Latest news from MiMo feed'
    author = 'MiMo Team'

    # Initialize printer
    printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)

    # Print welcome messag
    print(HTMLParser().unescape(title))
    printer.print(bytes((unidecode(
            HTMLParser().unescape(title)
        )
    ).encode()))

    printer.feed(1)

    printer.print(unidecode(
            HTMLParser().unescape(subtitle)
        )
    )

    printer.feed(1)

    printer.print(unidecode(
            HTMLParser().unescape(author)
        )
    )

    printer.feed(1)

    #printer.print(unidecode(
    #        HTMLParser.HTMLParser().unescape('2019')
    #    )
    #)

    printer.feed(4)



def mimo_print(data):
    '''
    TODO: Implement JSON parse
    '''
    # Start printing
    printer.inverseOn()
    printer.print(' ' + '{:<31}'.format(data['user']))
    printer.inverseOff()

    printer.underlineOn()
    printer.print('{:<32}'.format(data['date']))
    printer.underlineOff()

    # Remove HTML escape sequences
    # and remap Unicode values to nearest ASCII equivalents
    printer.print(data['text'])

    printer.feed(3)
