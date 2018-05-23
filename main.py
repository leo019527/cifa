# -*- coding:utf-8 -*-
# @Time    : 2018/5/10 14:13
# @Author  : leolee
# @File    : main.py
from DFA import DFA




wenfa = open("wenfa","r").readlines()

Dfa = DFA(wenfa)

sentence = open('input',"r").read()

Dfa.run(sentence)

Dfa.printOutput()