import curses
from curses import wrapper
from wpm.wpm import WPM

def main(stdscr):
	curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_RED, curses.COLOR_RED)

	wpm = WPM(curses)
	wpm.start_screen(stdscr)
	while True:
		wpm.wpm_test(stdscr)
		stdscr.addstr(2, 0, "You completed the text! Press any key 'y' to continue or 'esc' to quit.")
		try:
			key = stdscr.getkey()
			while ord(key) != 121:
				key = stdscr.getkey()
		except:
			break
		
		if ord(key) == 27:
			break

if __name__ == "__main__":
	wrapper(main)