import curses

class OutputHandler:
    def __init__(self):
        pass

    def exec(self, stdscr):
        # No cursor blinking
        curses.curs_set(False)

        # Use Default Background
        curses.use_default_colors()

        