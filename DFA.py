# -*- coding:utf-8 -*-
# @Time    : 2018/5/15 16:43
# @Author  : leolee
# @File    : DFA.py
import os
class DFA:
    #文法处理成NFA
    def __init__(self,wenfa):
        #词法输出
        self.output = []
        # 状态转移字典
        self.stateChangeDic = {}
        #初始状态
        self.startState = '开始'
        for w in wenfa:
            s = w.replace("\n","").split('->')
            Vn = s[0][1:-1]
            if not self.stateChangeDic.__contains__(Vn):
                self.stateChangeDic[Vn] = {}
            tmp = self.hasVn(s[1])
            if tmp[0]:
                self.stateChangeDic[Vn][tmp[2]]=tmp[1]
            else:
                self.stateChangeDic[Vn][tmp[1]]='e'

    #判断文法中有无非终结符号
    def hasVn(self,wenfa):
        Vt = wenfa[0]
        Vn = ''
        tmp = wenfa[1:]
        if not tmp.__eq__(''):
            Vn = tmp[1:-1]
            return True,Vn,Vt
        else:
            return False,Vt

    #字母数字符号路由
    def router(self,word):
        if word.isalpha():
            return 'l'
        elif word.isdigit():
            return 'd'
        else:
            return word
    #接收输入并运行状态转换机
    def run(self,sentence):
        buff = ''
        # num = -1
        for a in sentence:
            if a.__eq__(' ') or a.__eq__('\n'):
                while not buff.__eq__(''):
                    num = self.runNFA(buff)
                    buff = buff[num:]
            else:
                buff += a
        return self.output

    #错误处理
    def error(self,word):
        print 'has error arround:"'+word+'"'
        os._exit(1)

    #判断是否为终止状态
    def isStop(self,state):
        return self.stateChangeDic[state].has_key('e')

    #接收单词运行状态机，返回接收的字母数量，并加入最终集合
    def runNFA(self,word):
        preState = ''
        currentState = '开始'
        dfaWord = ''
        for n in range(len(word)):
            dfaWord += word[n]
            tmp = self.router(word[n])
            if not self.stateChangeDic[currentState].has_key(tmp):
                if self.isStop(currentState):
                    self.output.append('<' + currentState + ":" + dfaWord[:-1] + ">")
                    return n
                else:
                    self.error(word[n])
            else:
                nextState = self.stateChangeDic[currentState][tmp]
                if nextState.__eq__('e'):
                    self.output.append('<'+currentState+":"+dfaWord+">")
                    return n+1
                else:
                    preState = currentState
                    currentState = nextState
        if self.isStop(currentState):
            self.output.append('<'+currentState+":"+dfaWord+">")
            return len(word)
        else:
            self.error(word)

    def printOutput(self):
        for i in self.output:
            print i
