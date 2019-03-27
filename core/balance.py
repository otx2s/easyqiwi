#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *

def bal():
	try:
		tok = input(B+"[#]"+W+" Enter token: ")
		pho = input(B+"[#]"+W+" Enter phone: ")
		api = QApi(token=tok, phone=pho)
		print(G+"[+]"+W+" Balance Founded")
		print(api.balance)
	except OSError:
		print(R+"[-]"+W+" Something wrong!")
		pass
