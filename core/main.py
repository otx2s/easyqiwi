#!/usr/bin/env python3

import os
from time import sleep as ts
from core.colors import *
from SimpleQIWI import *
from core.balance import *
from core.main import *
from core.vivod import *
from core.banner import *

os.system("clear")

def main():
	print(banner)
	van = input(">>> ")
	if van == "1" or van == "01":
		bal()
		main()

	elif van == "2" or van == "02":
		viv()
		main()

	elif van == "3" or van == "03":
		print(R+"\nBye, bye\n"+W)
		ts(1)

	else:
		print(R+"[-]"+W+" Wrong command -> " + van)
		main()

if __name__ == '__main__':
	main()
