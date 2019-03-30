#!/usr/bin/env python3

import os
from time import sleep as ts
from core.colors import *
from SimpleQIWI import *
from core import balance
from core import main
from core import vivod
from core.banner import *

os.system("clear")

def main():
	print(banner)
	try:
		van = input(">>> ")
		if van == "1" or van == "01":
			balance.bal()
			main()

		elif van == "2" or van == "02":
			vivod.viv()
			main()

		elif van == "3" or van == "03":
			print(R+"\nBye, bye\n"+W)

		else:
			print(R+"[X]"+W+" Wrong command -> " + van)
			ts(1)
			main()

	except(KeyboardInterrupt):
		print(R+"[X]"+W+" Exiting...")
if __name__ == '__main__':
	main()