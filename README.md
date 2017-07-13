# Wordembedding-and-semantics
## Abstract
Neural network based word embedding has demonstrated outstanding results in variety task, and become a standard input
for NLP related deep learning research. These representations are capable to catch semantic regularities in language,
e.g. analogy relation. While a general question "what kind of semantic relation does the embedding represent and how
 the semantic relation could be retrieved using the embedding model?" is not clear and rare relevant work was explored.
 In this study, we proposed a new approach to explore the semantic relation represented in neural-embedding based
 on WordNet and UMLS. Our study demonstrated neural embedding did prefer some semantic relation as well as the neural
 embedding also represented diverse semantic relations. Our study also found out the NER based phrase composition
 outperformed Word2phrase and the word variants did not affect the performance on analogy and semantic relation tasks.

 ## Method
 [Presentation Link](https://docs.google.com/presentation/d/1eyqICs6EJ0JALZkUqGJh5h2r3jt4aptCueWyutFYd98/edit?usp=sharing)

 ## Result

### Top 10 nearest neighbors
![top 10 nearest neighbos](materials/comedy-pca-tf500-top10-nb.jpg)

### Evaluation term and its relation term
![relation word](materials/comedy-pca-tf500-top20523-True.jpg)

### Analogy tasks @ Word2vec
![analogy](materials/word2vec-analogy.jpg)

### Analogy task @ top 5
![analogy top 5](materials/wdgpn-accuracy-top5-analogy.jpg)

### Semantic relation task @ Word2vec
![relation @ Word2vec](materials/word2vec-relation.jpg)

### Semantic relation @ top 5
![relation top 5](materials/wdgpn-hit_cnt_term_pct-top5-relation.jpg)

### Semantic weighted relation @ top5
![relation top 5](materials/wdgpn-hit_weight_term_pct-top5-relation.jpg)

### Analogy phrase composition
![phrase analogy top 5](materials/lwn-accuracy-top5-analogy.jpg)

### Semantic relation phrase composition
![phrase relation top 5](materials/lwn-hit_weight_term_pct-top5-relation.jpg)

