import nltk
from nltk.corpus import *
from nltk.stem.wordnet import *
from nltk import pos_tag, word_tokenize
from nltk.wsd import lesk
import os
from nltk.tag.stanford import NERTagger



def getText(mapfile):
	path = mapfile + "/en.raw"
	f = open(path)
	rawText = f.read()
	f.close()
	rauwetekst = rawText.decode('utf-8')
	return rauwetekst

def tokenize(rauwetekst):
	regels = rauwetekst.strip()
	tokens = nltk.word_tokenize(regels)
	
def picklocations(tags3list):
	locationlist = []
	for sentence in tags3list:
		for item in sentence:
			if item[1] == 'LOCATION':
				locationlist.append(item)
			else:
				locationlist.append('*')
	return locationlist 

def findcities(locationlist):
	citylist = []
	countrylist = []
	for word in locationlist:
		if word == '*':
			continue
		else:
			synsets = wordnet.synsets(word[0], pos="n")
			for synset in synsets:
				definition = synset.definition()
				if 'city' in definition:
					citylist.append(word[0])
				elif 'country' or 'republic' or 'state' in definition:
					countrylist.append(word[0])
	print(citylist)
	print(countrylist)

def main():
	maplijst = ['p17/d0018','p17/d0036','p17/d0114','p17/d0148','p17/d0203','p17/d0306','p17/d0383','p17/d0457','p17/d0468', 'p18/d0048','p18/d0100','p18/d0421','p18/d0463','p18/d0485','p18/d0671','p18/d0688', 'p19/d0009','p19/d0153','p19/d0178','p19/d0269','p19/d0364','p19/d0542','p19/d0653','p19/d0686','p19/d0688']
	st3class = NERTagger('stanford-ner-2014-06-16/classifiers/english.all.3class.distsim.crf.ser.gz', 'stanford-ner-2014-06-16/stanford-ner-3.4.jar')
	
	for mapfile in maplijst:
		rawText = getText(mapfile)
		rawText = rawText.split()
		tags3list = st3class.tag(rawText)
		locationlist = picklocations(tags3list)
		findcities(locationlist)
				
	#slides week 3 synsets
main()
