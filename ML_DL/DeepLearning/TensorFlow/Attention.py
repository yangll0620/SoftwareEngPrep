query_input = tf.keras.Input(shape=(None,), dtype='int32')
value_input = tf.keras.Input(shape=(None,), dtype='int32')



# Embedding looup
token_embedding = tf.keras.layers.Embedding(input_dim=1000, output_dim=64)
# Query embeddings of shape [batch_size, Tq, dimension].
query_embeddings = token_embedding(query_input)
# Value embeddings of shape [batch_size, Tv, dimension].
value_embeddings = token_embedding(value_input)


# CNN layer
cnn_layer = tf.keras.layers.Conv1D(
    filter=100,  kernal_size = 4, padding='same')

query_seq_encoding = cnn_layer(query_embeddings)
# Value encoding of shape [batch_size, Tv, filters].
value_seq_encoding = cnn_layer(value_embeddings)


query_value_attention_seq = tf.keras.layer.Attention()(
    [query_seq_encoding, value_seq_encoding]
)


## Multihead Attention
import tensorflow as tf
from tensorflow.keras.layers import MultiHeadAttention

layer = MultiHeadAttention(num_heads=2, key_dim = 2)
target = tf.keras.Input(shape=[8,16])
source = tf.keras.Input(shape=[4, 16])

output_tensor, weights = layer(target, source, 
                               return_attention_scores=True)
