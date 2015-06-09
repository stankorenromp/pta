from collections import Counter
from nltk.metrics import ConfusionMatrix

def main():
	maplijst = ['p17/d0018','p17/d0036','p17/d0114','p17/d0148','p17/d0191','p17/d0203','p17/d0306','p17/d0383','p17/d0457','p17/d0468', 'p18/d0048','p18/d0100','p18/d0421','p18/d0463','p18/d0485','p18/d0671','p18/d0688', 'p19/d0009','p19/d0153','p19/d0178','p19/d0269','p19/d0364','p19/d0542','p19/d0653','p19/d0686','p19/d0688']
	listGerben = []
	listKamil = []
	listStan = []
	for mapfile in maplijst:
		pathGerben = mapfile + "/en.tok.off.pos.ex2GerbenTimmerman"
		infile = open(pathGerben, 'r+')
		for line in infile:
			listGerben.append(line.split())
		pathStan = mapfile + "/en.tok.off.pos.ex2StanKorenromp"
		infile2 = open(pathStan, 'r+')
		for line in infile2:
			listStan.append(line.split())
		pathKamil = mapfile + "/en.tok.off.pos.ex2KamilZukowski"
		infile3 = open(pathKamil, 'r+')
		for line in infile3:
			listKamil.append(line.split())
	
	item5gerben = []
	item5stan = []
	item5kamil = []
	
	
	for item in listGerben:
		try:
			item5gerben.append(item[5])
		except IndexError:
			item5gerben.append('*')
			pass
	for item in listStan:
		try:
			item5stan.append(item[5])
		except IndexError:
			item5stan.append('*')
			pass
	for item in listKamil:
		try:
			item5kamil.append(item[5])
		except IndexError:
			item5kamil.append('*')
			pass
			
	listinterestingGerben = []
	listinterestingStan = []
	listinterestingKamil = []
			
	for item in item5gerben:
		if item == '*':
			listinterestingGerben.append('/')
		else:
			listinterestingGerben.append('*')
	for item in item5stan:
		if item == '*':
			listinterestingStan.append('/')
		else:
			listinterestingStan.append('*')
	for item in item5kamil:
		if item == '*':
			listinterestingKamil.append('/')
		else:
			listinterestingKamil.append('*')
			
	print("Interesting entities vs non-interesting entities")		
	print('Gerben vs. Stan')
	matrix1(listinterestingGerben,listinterestingStan)
	print('Gerben vs. Kamil')
	matrix1(listinterestingGerben,listinterestingKamil)
	print('Stan vs. Kamil')
	matrix1(listinterestingStan,listinterestingKamil)
	
	print("All entities")
	print('Gerben vs. Stan')
	matrix(item5gerben,item5stan)
	print('Gerben vs. Kamil')
	matrix(item5gerben,item5kamil)
	print('Stan vs. Kamil')
	matrix(item5stan,item5kamil)

def matrix1(lijst1, lijst2):
	ref  = lijst1
	tagged = lijst2
	cm = ConfusionMatrix(ref, tagged)

	print(cm)

	labels = set('* /'.split())

	true_positives = Counter()
	false_negatives = Counter()
	false_positives = Counter()

	for i in labels:
		for j in labels:
			if i == j:
				true_positives[i] += cm[i,j]
			else:
				false_negatives[i] += cm[i,j]
				false_positives[j] += cm[i,j]

	print("TP:", sum(true_positives.values()), true_positives)
	print("FN:", sum(false_negatives.values()), false_negatives)
	print("FP:", sum(false_positives.values()), false_positives)
	print() 

	for i in sorted(labels):
		if true_positives[i] == 0:
			fscore = 0
		else:
			precision = true_positives[i] / float(true_positives[i]+false_positives[i])
			recall = true_positives[i] / float(true_positives[i]+false_negatives[i])
			fscore = 2 * (precision * recall) / float(precision + recall)
		print("fscore: ",i, fscore)

def matrix(lijst1, lijst2):
	ref  = lijst1
	tagged = lijst2
	cm = ConfusionMatrix(ref, tagged)

	print(cm)

	labels = set('COU CIT NAT PER ORG ENT'.split())

	true_positives = Counter()
	false_negatives = Counter()
	false_positives = Counter()

	for i in labels:
		for j in labels:
			if i == j:
				true_positives[i] += cm[i,j]
			else:
				false_negatives[i] += cm[i,j]
				false_positives[j] += cm[i,j]

	print("TP:", sum(true_positives.values()), true_positives)
	print("FN:", sum(false_negatives.values()), false_negatives)
	print("FP:", sum(false_positives.values()), false_positives)
	print() 

	for i in sorted(labels):
		if true_positives[i] == 0:
			fscore = 0
		else:
			precision = true_positives[i] / float(true_positives[i]+false_positives[i])
			recall = true_positives[i] / float(true_positives[i]+false_negatives[i])
			fscore = 2 * (precision * recall) / float(precision + recall)
		print("fscore: ",i, fscore)
		
main()
