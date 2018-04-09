# Wordembedding-and-semantics
## Abstract
In the past few years, neural-network-based word embeddings have been widely used in text mining. However, the vector
representations of word embeddings mostly act as a black box in downstream applications using them, thereby limiting
their interpretability. Even though word embeddings are able to capture semantic regularities in free text documents,
it is not clear how different kinds of semantic relations are represented by word embeddings and how semantically-related
terms can be retrieved from word embeddings.
### Methods
To improve the transparency of word embeddings and the interpretability of the applications using them, in this study,
we propose a novel approach for evaluating the semantic relations in word embeddings using external knowledge bases:
Wikipedia, WordNet and \acrfull{umls}. We trained multiple word embeddings using health-related articles in Wikipedia
and then evaluated their performance in the analogy and semantic relation term retrieval tasks. We also assessed if the
evaluation results depend on the domain of the textual corpora by comparing the embeddings of health-related Wikipedia
articles with those of general Wikipedia articles.
### Results
Regarding the retrieval of semantic relations, we found that word embeddings are able to retrieve diverse semantic
relations in the nearest neighbors of a given word. Meanwhile, the two popular word embedding approaches, Word2vec
and GloVe, obtained comparable results on both the analogy retrieval task and the semantic relation retrieval task,
while dependency-based word embeddings had much worse performance in both tasks. We also found that the word embeddings
trained with health-related Wikipedia articles obtained better performance in the health-related relation retrieval tasks
than those trained with general Wikipedia articles.
### Conclusion
It is evident from this study that word embeddings can group terms with diverse semantic relations together. It is thus
recommended to use domain-specific corpus to train word embeddings for domain-specific text mining tasks.


## Figures

### Figure 1 gives concrete examples of these semantic relations
![figure 1](materials/Figure1.jpg)

### Figure 2 shows the words faculty and loyalty and their top 10 nearest neighbors in the reduced word embedding space by Principal Component Analysis (PCA)
![figure 2](materials/Figure2.jpg)

### In Figure 3, the same type of relation terms are labeled with the same symbol
![figure 3](materials/Figure3.jpg)

### Figures 4 and 5 show the evaluation results of different types of word embeddings in the general and medical-related analogy term retrieval subtasks
![figure 4](materials/Figure4.jpg)
![figure 5](materials/Figure5.jpg)

### Figure 6 shows the detailed analogy task results when k = 5 for different embedding training methods
![figure 6](materials/Figure6.jpg)

### Figure 7 and 8 investigated the retrieved ratio for top 1, 5, 20 and 100 nearest neighbors for each of the three kinds of word embeddings
![figure 7](materials/Figure7.jpg)
![figure 8](materials/Figure8.jpg)

### Figures 9 and 10 give a closer comparison among the methods when k=5
![figure 9](materials/Figure9.jpg)
![figure 10](materials/Figure10.jpg)

### Figure 11 shows that health related corpus and general corpus had the similar results in the analogy term retrieval task
![figure 11](materials/Figure11.jpg)

### Figure 12 shows that health related corpus obtained slightly better result on general semantic relation retrieval task
![figure 12](materials/Figure12.jpg)

Related data: [Google Drive sharing link](https://drive.google.com/open?id=0Bze8dEz4G92GOFRsYlZJdHNHRDA)
