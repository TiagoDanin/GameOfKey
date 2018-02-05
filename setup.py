#!/usr/bin/env python3
# setup.py

from setuptools import setup

setup(
	name='game_of_key',
	version ='1.0',
	description = 'The game made your keyboard, this is amazing!',
	long_description = '''
	Markdown is not supported here, see this document in: 
	https://TiagoDanin.github.io/gameofkey/
	''',
	author = 'Tiago Danin',
	author_email = 'TiagoDanin@outlook.com',
	license = 'MIT',
	url = 'https://TiagoDanin.github.io/gameofkey/',
	install_requires= [
		'pyautogui',
	],
	classifiers = [
		'Natural Language :: English',
		'Operating System :: MacOS',
		'Operating System :: Unix',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6'
	],
	keywords = 'game led leds keyboard key'
)
