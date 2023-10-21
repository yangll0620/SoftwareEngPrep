[Embedding](#embedding) 
* [Text Embedding](#text-embedding)
    * [Word2vec](#word2vec)
    * [Context-based embeddings](#context-based-embeddings)
* [Visual Embedding](#visual-embedding)

[Predictive Model Pros and Cons](#predictive-model-pros-and-cons)
* [Logistic Regression](#logistic-regression)
* [Gradient-boosted decision Tree (GBDT)](#gradient-boosted-decision-tree-gbdt)


## Approximate Neighbor Method

## Embedding
Embeddings enable the encoding of entities (e.g., words, docs, images, person, ad, etc.) in a low dimensional vector space such that it captures their semantic information.

### Text Embedding
#### Word2vec

 Word2vect produces word embeddings by using shallow neural networks (having a single hidden layer) and self-supervised learning from a large corpus of text data.

* Methods

CBOW: Continuous bag of words (CBOW) tries to predict the current word from its surrounding words. Helpful with small training set


Skipgram: predict surrounding words from the current word. Helpfult with larget training set


* Pros:

Once trained, Word2vec embeddings have a fixed vector for every term. Word2vec embedding doesn’t consider the context in which the word appears to generate its embedding

#### Context-based embeddings
Contextualized information can result in different meanings of the same word, and context-based embeddings look at neighboring terms at embedding generation time.

* Architectures used to generate word context-based embedding 

Embeddings from Language Models (ELMo) use the bi-directional LSTM model to capture the words that appear before and after the current word.

Bidirectional Encoder Representations from Transformers (BERT)  uses an attention mechanism and is able to see all the words in the context, utilizing only the ones (i.e., pay more attention) which help with the prediction.

### Visual Embedding
#### Auto Encoders
Auto-encoders use neural networks consisting of both an encoder and a decoder. They first learn to compress the raw image pixel data to a small dimension via an encoder model and then try to de-compress it via a decoder to re-generate the same input image. 

### Visual supervised learning tasks#
The penultimate layer before softmax captures all image information in a vector such that it can be used to classify the image correctly.

## Predictive Model Pros and Cons
### Logistic Regression

* Pros:    
    * Fast to train 
    * Easy to implement
* Cons:
    * Can not solve non-linear problems
    * Inability to capture feature interactions

### Gradient-boosted decision Tree (GBDT)
* Pros:
    * Interpretable
    * Easy to understand

* Cons:
    * Inefficient for continual learning.
    * Cannot train embedding layers.


