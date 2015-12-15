# coding: utf-8
# !/usr/bin/env python

import os
import re
from blablacar import blablacar_search
from liftshare import liftshare_search

# main
##


def main():
    print("Hello World!")
    origin = "Birmingham, UK"
    destination = "London, UK"
    date = "18/12/2015"
    blablacar_search(origin, destination, date)
    liftshare_search(origin, destination, re.sub('20', "", date))
    pass

main()
os.system("PAUSE")
