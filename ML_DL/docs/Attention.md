## Attention Mechanism

Using simpleRNN to descibe the ideas of attention and self-attetion mechanism. reference to https://www.youtube.com/watch?v=XhWdv7ghmQQ

Attention mechanism is to focus the attention to specific parts of data through adding a layer of neural network.

* SimpleRNN + Attention

Attention Weight: $\alpha_i = align(h_i, s_0)$  is to measure the relationship between the hidden state $h_i$ and the encoded vector $s_0$


![Alt text](figures/AttentionMechanism.jpg?raw=true "Attention") 


* Methods to obtain attention weights

1. Used in orginal paper which proposed attention mechanism.

![Alt text](figures/AttentionWeight_1.png?raw=true "Attention") 

$\bold v$ and $W$ are trainable.

2. Used in Transformer

![Alt text](figures/AttentionWeight_2.png?raw=true "Attention") 

$W_K$ and $W_Q$ are trainable.


## Self Attention Mechanism

The importance or relevance of each element is calcualted with respected to all other elements within the same sequence.

![Alt text](figures/SelfAttentionMechanism.jpg?raw=true "Attention") 


