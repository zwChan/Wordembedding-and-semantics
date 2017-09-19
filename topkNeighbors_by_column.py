from __future__ import division,print_function
__author__ = 'Jason'

import sys
import gensim

if len(sys.argv) <= 7:
    print(
    "Usage: [model-file] [vocab-file] [top-k] [input-file] [search-column] [keep-column] [output-file]\n" +
    """
    Goal: Given a keyword (could be phrase), Search the top k similar terms in the word embedding model.
    The input is supposed to be a columned file, e.g. csv, separated by 'tab'. You can specify any column as the key to search.
    Arguments:
    [model-file]: model of the word2vec binary format. (If you have txt format models, just modify the code a little bit)
    [vocab-file]: Vocabulary file of the model. If not exists, use "null".
    [top-k]: the number of similarity words
    [input-file]: The input file, should be separated by 'tab'
    [search-column]: the column used to search, 0-based
    [keep-column]: the columns you want to keep in the output file. e.g. 0,1,3,5. Note the top k similar terms will the next k column following these column.
    [output-file]: the output file
    """)
    exit(1)
print('\t'.join(sys.argv))
model = sys.argv[1]
# model = r'C:\fsu\class\thesis\token.txt.bin'
vocFile=sys.argv[2] if sys.argv[2] != 'null' else None
# vocFile = r'C:\fsu\class\thesis\token.txt.voc'
topn = 10 if len(sys.argv) <= 3 else int(sys.argv[3])
inputFile = sys.argv[4]
keyColumn = int(sys.argv[5])
keepColumns = [int(x) for x in sys.argv[6].split(',')]
outputFile = sys.argv[7]
print("Loading model...")
wv = gensim.models.KeyedVectors.load_word2vec_format(model,fvocab=vocFile,binary=True)
print("model loaded.")
lines = open(inputFile,'r').readlines()
with open(outputFile,'w+') as of:
    for line in lines:
        if not line.strip():
            continue
        tokens = line.strip().split('\t')
        try:
            sims = wv.most_similar(tokens[keyColumn].lower().split(),topn=topn)
            out = ""
            for i in keepColumns:
                out += str(tokens[i]) + '\t'
            for term,score in sims:
                out += term + '\t'
            of.write(out.strip() + '\n')
        except Exception as e:
            print("input: %s, Error: %s" % (line,e.message))