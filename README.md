# BBCRecommendation

## Project Introduction

The ultimate goal is to learn how to make a simple article recommendation engine using a semi-recent advance in natural language processing called word2vec (or just word vectors). In particular, we're going to use a "database" from Stanford's GloVe project trained on a dump of Wikipedia. The project involves reading in a database of word vectors and a corpus of text articles then organizing them into a handy table (list of lists) for processing.

To make it accessibled, I build a web server that displays a list of recommended BBC articles on the side when you read an article. Once you click on any article suggested on the side, it will direct you to the recommended articles that are similar based on the contents.
