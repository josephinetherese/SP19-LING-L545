import csv
import argparse
import sys
import wer


# generates surface form dictionary
def get_surface_csv(file):
	surface = {}
	with open(file) as f:
		csvreader = csv.reader(f, delimiter='\t')
		for row in csvreader:
			if 'sent_id' not in row and len(row) > 3:
				token = row[1]
				if token not in surface:
					surface[token] = 1
				else:
					surface[token] += 1
	return surface


# generates surface form dictionary and punct dictionary
def get_dicts(file):
	surface = {}
	punct = {}
	with open(file) as f:
		csvreader = csv.reader(f, delimiter='\t')
		for row in csvreader:
			if 'sent_id' not in row and len(row) > 3:
				token = row[1]
				if row[3] == 'PUNCT':
					if token in punct:
						punct[token] += 1
					else:
						punct[token] = 1
				if token not in surface:
					surface[token] = 1
				else:
					surface[token] += 1
	return (surface, punct)


sentences = []


# returns word sequence W
def maxmatch(sentence, dictionary):
	i = len(sentence)
	if i == 0:
		return []
	while i > 0:
		firstword = sentence[:i]
		remainder = sentence[i:]
		i -= 1
		if firstword in dictionary:
			sentences.append(firstword)
			return maxmatch(remainder, dictionary)
		if i == 1 and len(sentence) > 0:
			sentences.append(sentence[0])
			if len(sentence) > 1:
				return maxmatch(sentence[1:], dictionary)
			return []
	return sentences


# return index of first punctuation mark in sentence
def find_punct(sentence, punct):
	for i in range(len(sentence)):
		if sentence[i] in punct:
			return i


# mild optimization of maxmatch - assumes punctuation occurs between words
def maxmatch_punct(sentence, dictionary):
	punct = dictionary[1]
	dictionary = dictionary[0]
	# tried_end = False
	i = len(sentence)
	if i == 0:
		return []
	while (len(sentence) > 0):
		i = find_punct(sentence, punct)
		# tried_end = False
		if i == None:
			i = len(sentence)
		while i > 0:
			firstword = sentence[:i]
			remainder = sentence[i:]
			# print(firstword, remainder)
			i -= 1
			if firstword in dictionary:
				# print(firstword)
				sentences.append(firstword)
				return maxmatch(remainder, dictionary)
			if i == 1 and len(sentence) > 0:  # gotten to the end and still haven't found a match
				# if tried_end:  #already tried the old school approach
				# 	sentences.append(sentence[0]) #add farthest left item to sentences, recur on rest of sentence
				# 	if len(sentence) > 1:
				# 		return maxmatch(sentence[1:], dictionary)
				# 	return []
				# else: # abandon the punct approach and try it the old school way
				i = len(sentence)
			# tried_end = True
	return sentences


def get_argparser():
	parser = argparse.ArgumentParser()
	parser.add_argument('filename', metavar='F', help='dictionary file to read')
	parser.add_argument('-p', action='store_true', help='run with punct method instead of standard')
	parser.add_argument('-e', action='store_true', help='run evaluation')
	return parser


def main():
	sentence = sys.stdin.read()
	parser = get_argparser()
	args = parser.parse_args()
	file = args.filename
	p = args.p
	e = args.e
	print(sentence)
	if (p):
		# print("PUNCT")
		m = maxmatch_punct(sentence.replace(" ", ""), get_dicts(file))
	else:
		m = maxmatch(sentence.replace(" ", ""), get_surface_csv(file))
	print(' '.join(m))
	if (e):
		wer.wer(sentence, m)

# sentences.clear()
# print(maxmatch_punct(sentence, get_dicts(file)))

if __name__ == '__main__':
	main()
