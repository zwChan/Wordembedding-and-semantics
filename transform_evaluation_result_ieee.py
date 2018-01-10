from __future__ import division,print_function
__author__ = 'Jason'

import sys
import re
import numpy as np
from transform_evaluation_result import get_relation_data,get_row,fig_method_topn,fig_compare_methods


if len(sys.argv) < 2:
    print("Usage: [input_file.csv] [relation|analogy")
    exit(1)
print(sys.argv,file=sys.stderr)
np.set_printoptions(precision=2,linewidth=120,suppress=True)
input_file = sys.argv[1]
isRelation = sys.argv[2].lower()=='relation'
res_tag = sys.argv[3] if len(sys.argv) > 3 else ""
rr = get_relation_data(input_file, isRelation)
print(rr)

topN = [1, 5, 10, 20, 100]

#################################################
value,methods,tasks,topns = get_row(rr.value,'*','*','*','*')
methods = methods
tasks = tasks
topns = sorted(topns)

#### method detial vs topn performance
for m in methods:
    if isRelation:
        fig_method_topn(rr,m,'hit_cnt_term_pct',topns,'Semantic relation tasks','Retrieved terms ratio (%)')
        fig_method_topn(rr,m,'hit_weight_term_pct',topns,'Semantic relation tasks','Weighted Retrieved terms ratio (%)')
    else:
        fig_method_topn(rr,m,'accuracy',topns,'Analogy tasks','Accuracy (%)')

#### method compaire on unigram
for topn in topN:
    if isRelation:
        fig_compare_methods(rr,['word2vec','deps-word2vec','glove'],['hit_cnt_term_pct'],[topn],'Semantic relation tasks','Retrieved Ratio (%)')
        fig_compare_methods(rr,['word2vec','deps-word2vec','glove'],['hit_weight_term_pct'],[topn],'Semantic relation tasks','Weighted Retrieved ratio (%)')
    else:
        fig_compare_methods(rr,['word2vec','deps-word2vec','glove'],['accuracy'],[topn],'Analogy tasks','Accuracy (%)')
#
# #### method compaire on phrases
# for topn in topN:
#     if isRelation:
#         fig_compare_methods(rr,['linear-estimate','word2phrase','ner'],['hit_cnt_term_pct'],[topn],'Semantic relation tasks','Retrieved ratio (%)')
#         fig_compare_methods(rr,['linear-estimate','word2phrase','ner'],['hit_weight_term_pct'],[topn],'Semantic relation tasks','Weighted Retrieved ratio (%)')
#     else:
#         fig_compare_methods(rr,['linear-estimate','word2phrase','ner'],['accuracy'],[topn],'Analogy tasks','Accuracy (%)')
