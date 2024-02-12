import os
import time
import random

class WPM:
	def __init__(self, curses):
		self.curses = curses

	def start_screen(self, stdscr):
		stdscr.clear()
		stdscr.addstr("Welcome to the Speed Typing Test!")
		stdscr.addstr("\nPress any key to begin!")
		stdscr.refresh()
		stdscr.getkey()

	def display_text(self, stdscr, target, current, wpm=0):
		stdscr.addstr(target)
		stdscr.addstr(1, 0, f"WPM: {wpm}")

		for i, char in enumerate(current):
			correct_char = target[i]
			color = self.curses.color_pair(1)
			if char != correct_char:
				if(char == " "):
					color = self.curses.color_pair(4)
				else: 
					color = self.curses.color_pair(2)

			stdscr.addstr(0, i, char, color)

	def load_text(self):
		# with open("../data/text.txt", "r") as f:
		cur_path = os.path.dirname(__file__)
		x = cur_path.split()
		x.pop()
		x.append("data")
		x.append("text.txt")
		text_path = "/".join(x)
		with open(text_path, "r") as f:
			lines = f.readlines()
			return random.choice(lines).strip()

	def wpm_test(self, stdscr):
		target_text = self.load_text()
		current_text = []
		wpm = 0
		start_time = time.time()
		stdscr.nodelay(True)

		while True:
			time_elapsed = max(time.time() - start_time, 1)
			wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

			stdscr.clear()
			self.display_text(stdscr, target_text, current_text, wpm)
			stdscr.refresh()

			if "".join(current_text) == target_text:
				stdscr.nodelay(False)
				break

			try:
				key = stdscr.getkey()
			except:
				continue

			if ord(key) == 27:
				break

			if key in ("KEY_BACKSPACE", '\b', "\x7f"):
				if len(current_text) > 0:
					current_text.pop()
			elif len(current_text) < len(target_text):
				current_text.append(key)
