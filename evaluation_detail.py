from __future__ import division,print_function
__author__ = 'Jason'

from evaluation import *

# --------------------------------------------------------------------------------
if len(sys.argv) < 5:
    print("Usage: [model-file] [vocab-file] [analogy-file] [relation-file] [output-file] [top-n] ",file=sys.stderr)
    exit(1)
print(sys.argv)
model = sys.argv[1]
# model = r'C:\fsu\class\thesis\token.txt.bin'
vocFile=sys.argv[2]
# vocFile = r'C:\fsu\class\thesis\token.txt.voc'
analogyfile = sys.argv[3]
# qfile = r'C:\fsu\ra\data\201706\synonym_ret.csv'
relfile = sys.argv[4]
outputFile=sys.argv[5]
topn = 10 if len(sys.argv) < 7 else int(sys.argv[6])
usePhrase = True
otherVocab = ""
isIntersectVacab = False
sample = 0

isBin = model.strip().endswith('bin')

evalVocab = get_evaluation_vocab(vocFile,otherVocab,isIntersectVacab)
print("evalVocab isIntersectVacab=%s, vocab number is %d" % (str(isIntersectVacab), len(evalVocab)))
wv = gensim.models.KeyedVectors.load_word2vec_format(model,fvocab=vocFile,binary=isBin)
termList = accuracy_rel(wv,relfile,gensim.models.KeyedVectors.most_similar,evalVocab,topn=topn,usePhrase=usePhrase,sample=sample)
output_detail_relation_result(termList,outputFile)

# evaluation_rel = EvaluateRelation(termList,topn=topn)
# # print("### result start: ###")
# # evaluation.PrintHitList()
# # print("#### evaluation result ###")
# evaluation_rel.evaluate()
# print(evaluation_rel)

# analogyList = accuracy_analogy(wv,analogyfile,gensim.models.KeyedVectors.most_similar,topn=topn, usePhrase=usePhrase,sample=sample)
# evaluation_analogy = EvaluateAnalogy(analogyList,topn=topn)
# print(evaluation_analogy)
#



