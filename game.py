import pyautogui
from random import randint
import curses
import time

config = ['numlock', 'capslock', 'scrolllock']

def key1():
	pyautogui.press(config[0])
	time.sleep(1)
	pyautogui.press(config[0])
def key2():
	pyautogui.press(config[1])
	time.sleep(1)
	pyautogui.press(config[1])
def key3():
	pyautogui.press(config[2])
	time.sleep(1)
	pyautogui.press(config[2])
def keyAll():
	pyautogui.press(config[0])
	pyautogui.press(config[1])
	pyautogui.press(config[2])
	time.sleep(1)
	pyautogui.press(config[2])
	pyautogui.press(config[1])
	pyautogui.press(config[0])

def keyFalid():
	pyautogui.press(config[0])
	pyautogui.press(config[2])
	time.sleep(1)
	pyautogui.press(config[0])
	pyautogui.press(config[1])
	pyautogui.press(config[2])
	time.sleep(1)
	pyautogui.press(config[1])

def keyNumb(numb):
	n = str(numb)
	if (n == '1'):
		key1()
	elif (n == '2'):
		key2()
	elif (n == '3'):
		key3()

keyAll()
keyAll()

def main(win):
	win.clear()
	win.nodelay(True)
	win.addstr('Start game\n')
	win.addstr('Disable numlock, scrolllock and capslock in your keyboard. Thank!\n')
	table = []
	next_ = True
	chon = 0
	len_ = 0
	while True:
		if (next_):
			win.addstr('...\n')
			table.append(randint(1, 3))
			len_ = len(table) - 1
			chon = 0
			for i in table:
				win.addstr(str(i))
				keyNumb(i)
			next_ = False
		try:
			key = win.getkey()
			win.clear()
			if(str(key) == str(table[chon])):
				if (len_ == chon):
					next_ = True
					win.addstr('OK! NEXT\n')
					keyAll()
				else:
					chon += 1
					#win.addstr('OK!\n')
			else:
				win.addstr('FALID!\n')
				keyFalid()
				table = []
				next_ = True
				chon = 0
				len_ = 0
				time.sleep(2)
				keyAll()
		except Exception as e:
			pass

curses.wrapper(main)
