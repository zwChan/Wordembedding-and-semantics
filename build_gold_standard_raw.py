from __future__ import division,print_function
__author__ = 'Jason'
import sys
import re
import itertools as it
import random
import random
import csv
import logging
import  gensim
from gensim import utils, matutils
# logger = logging.getLogger(__name__)


def get_vocab(vocFiles, intersect=True):
    # construct the vocabulary for evaluation
    evalVocab = set()
    for vocFile in vocFiles.split(','):
        vocab = set()
        with open(vocFile.strip()) as f:
            for line in f.readlines():
                tokens = line.split()
                if len(tokens)>0 and len(tokens[0]) > 0:
                    vocab.add(tokens[0].lower())
        if not evalVocab:
            evalVocab = vocab
        else:
            evalVocab &= vocab
    return evalVocab

def term_in_vocab(term, vocab, exact=True):
    if exact:
        return term in vocab
    for word in re.split(r'_|\s', term):
        word = word.strip().lower()
        if word not in vocab:
            return False
    return True

def filter_terms(inFile, vocab):
    res = []
    regex = re.compile(r'[^a-zA-Z\d\- ]')
    invalid = re.compile(r'[^a-zA-Z]*')
    with open(inFile) as f:
        for line in f.readlines():
            tokens = line.split(',')
            if len(tokens) < 4: continue
            source = regex.sub('',tokens[1]).replace(' ','_').strip().lower()
            target = regex.sub('',tokens[3]).replace(' ','_').strip().lower()
            if source == target: continue
            if invalid.match(source) or invalid.match(target): continue
            if term_in_vocab(source, vocab) and term_in_vocab(target, vocab):
                res.append((source, target))
    print('rels %d' % len(res))
    return list(set(res))


def build_analogy(rels, outFile, number=10000):
    # singles = [x for x in rels if x[0].count(' ')!=0 and x[1].count(' ') != 0]
    # print('singles %d' % len(singles))
    pairs = list(it.product(rels, rels))
    print ('pairs %d' % len(pairs))
    pairs_single_end = [x for x in pairs if x[1][1].count('_') == 0 and x[0] > x[1]]  # remove symmetric pairs
    print ('pairs_single_end %d' % len(pairs_single_end))
    random.shuffle(pairs_single_end)
    with open(outFile, 'w+') as f:
        for pair in pairs_single_end[:number]:
            f.write('%s %s %s %s\n' % (pair[0][0].replace(' ','_'),pair[0][1].replace(' ','_'),
                                     pair[1][0].replace(' ','_'),pair[1][1].replace(' ','_')))

def main():
    print('sys.argv: ' + str(sys.argv))
    if len(sys.argv) <= 3:
        print('Usage: [vocab_files] [input_files] [output_file] [relation_pairs_file]')
    vocab = get_vocab(sys.argv[1])
    print(len(vocab))
    rels = filter_terms(sys.argv[2], vocab)
    if len(sys.argv) > 4:
        with open(sys.argv[4], 'w+') as f:
            f.write('\n'.join(['\t'.join(rel) for rel in rels]))
    build_analogy(rels,sys.argv[3], 10000)
if __name__ == '__main__':
    main()