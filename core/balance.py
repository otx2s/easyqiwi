#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *

def bal():
	try:
		tok = input(B+"\n[#]"+W+" Enter token: ")
		pho = input(B+"[#]"+W+" Enter phone: ")
		api = QApi(token=tok, phone=pho)
		if api.balance != 0:
			print(G+"[+]"+W+" Balance Founded")
			print(G+"[+]"+W+" Balance =", api.balance)
	except:
		print(R+"[X]"+W+" Balance not found")
		pass
