#!/usr/bin/env python3

def check():
	try:
		import SimpleQIWI
	except ImportError:
		print("Please download 'SimpleQIWI'")