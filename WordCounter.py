#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
from porter2 import stem

def createWordsDict(fileName):
	inputFile = open(fileName).read()
	wordsDict = {}
	delims= r'[ "\t,;.?!\r\n]+'
	temp = re.split(delims,inputFile)
	for token in temp:
		token = turnToLower(token)
		if token not in wordsDict:
			wordsDict[token] = 1
		else:
			wordsDict[token] += 1
	return wordsDict

def frequency(wordDict, k):
	newlist = sorted(wordDict.items(), key=lambda item: item[1])
	newlist = newlist[::-1]
	newlist = newlist[:k]
	return newlist

def turnToLower(word):
	word = word.lower()
	return word

def performStem(wordsDict):
	stemmedDict =  {stem(k): v for k, v in wordsDict.items()}
	return stemmedDict

def main():
	try:
		fileName = sys.argv[1]
		k = int(sys.argv[2]) 

		#dictionary
		wordsDict = createWordsDict(fileName)
		
		#apply stem
		stemmedDict = performStem(wordsDict)
		
		#sort and reverse
		newlist = frequency(stemmedDict, k)	

		for line in newlist:
			print(line)
	
	except:
		print("Error")


if __name__ == '__main__':
	main()

#Author: Piyush Arora
#Have fun, keep coding
