# -*- coding:utf-8 -*-
# @Time    : 2018/5/10 14:13
# @Author  : leolee
# @File    : main.py
from DFA import DFA

#关键字
keyWorld = ["break","case","char","const","continue","default","double","double","else","enum","extern",
            "float","for","if","int","long","register","return","short","signed","sizeof","static","struct",
            "switch","typedef","union","unsigned","void","volatile","while"]
compute = ["+","-","*","/"]
seperator = [";",",","(",")","{","}"]
assignment = ["+=","-=","*=","/=","="]
comparater = [">=","<=",">","<","!=","=="]

allWord = [keyWorld,compute,seperator,assignment,comparater]

wenfa = open("wenfa","r").readlines()

Dfa = DFA(wenfa)

sentence = open('input',"r").read()

Dfa.run(sentence)

Dfa.identifyKeys(keyWorld)

Dfa.printOutput()