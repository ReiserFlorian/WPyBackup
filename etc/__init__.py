import argparse
import pathlib
import curses
import sys
import subprocess
import os
from os import path

import time

txt=[]

def main(stdscr):

    # No cursor blinking
    curses.curs_set(False)

    # Use Default Background
    curses.use_default_colors()


    pad = curses.newpad(11, 60)
    pad.scrollok(True)
    win = curses.newwin(1, 60, 3, 0)
    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 10):
        v = i-10
        pad.addstr('Test {}\n'.format(i))
        win.addstr(0, 0, '10 divided by {} is {}'.format(v, 10/v))
        pad.refresh(i-2, 0, 0, 0, 2, 60)
        win.refresh()
        time.sleep(0.1)
    for i in range(0, 11):
        txt.append(pad.instr(i, 0).decode())
    


class WPyBackupBase:
    def __init__(self):
        # Read version
        scriptPath = pathlib.Path(__file__).parent.resolve()
        with open(os.path.join(scriptPath, "version")) as fh:
            self._version = fh.readline()
        # Parse Command Line
        cmdParser = argparse.ArgumentParser(
            formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
        cmdParser.add_argument("-V", "--version", action="store_true", help="Print the version")

        self._cmdArgs = vars(cmdParser.parse_args())

    def checkMode(self):
        if self._cmdArgs["version"]:
            print(self._version)
            return True
        
    def checkCursors(self): 
        curses.wrapper(main)
        print ("\n".join(txt))

        # if self._cmdArgs["check"]:
        #     if self._returnCode == 0:
        #         print ("Everything seems to be fine")
        #     return True
        # else:
        #     return False