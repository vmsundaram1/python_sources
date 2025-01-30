'''
This program is used to implement embedding of different text message formats - a word, a sentence and paragraphs.
Different types of models through universal sentence encoder urls are used to process the input messages and arrive at the embedding output tensor.  
The tensor holds the embeddings of each message and the length of each embedding vector is 512

'''

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Assignment of Input URLs

url1 = "https://tfhub.dev/google/universal-sentence-encoder/4"
url2= "https://kaggle.com/models/google/universal-sentence-encoder/frameworks/TensorFlow1/variations/universal-sentence-encoder/versions/1"


# For URL-1 - Load the module based on the first URL and invoke a function to arrive at the embedding output tensor

embed = hub.load(url1)
embeddings1 = embed([
    "Do not be like a fox. Be like the King!!",
    "All are one! Be alike to everyone!!"]) 


# For URL-2 - Load the module based on the second URL and invoke a function to arrive at the embedding output tensor

embed = hub.load(url2)
embeddings2 = embed.signatures['default'](tf.constant([
    "Do not be like a fox. Be like a King!!",
    "All are one! Be alike to everyone!!"]))['default']


# Print the embeddings based on the output tensor for two different models

print("Using Model1 as per URL1:\n", len(embeddings1),"\n",embeddings1)
print("Using Model2 as per URL2:\n", len(embeddings2),"\n",embeddings2)


print("*****************************************************n")
print("PRINTING THE OUTPUT TENSOR FOR MODEL1 based on URL1 \n")
print("*****************************************************n")

for i, msg_embedding1 in enumerate(np.array(embeddings1).tolist()):

 print("Embedding1 Size: {}".format(len(msg_embedding1)))

 embedding_msg_snippet1 = ",".join( (str(x) for x in msg_embedding1[:len(msg_embedding1)]))

 print("Embedding1 [ {} ]\n".format(embedding_msg_snippet1))


print("*****************************************************n")
print("PRINTING THE OUTPUT TENSOR FOR MODEL2 based on URL2 \n")
print("*****************************************************n")

for i, msg_embedding2 in enumerate(np.array(embeddings2).tolist()):

 print("Embedding2 Size: {}".format(len(msg_embedding2)))

 embedding_msg_snippet2 = ",".join( (str(x) for x in msg_embedding2[:len(msg_embedding2)]))

 print("Embedding2 [ {} ]\n".format(embedding_msg_snippet2))