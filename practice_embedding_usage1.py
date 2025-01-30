'''
This program is used to implement embedding of different text message formats - a word, a sentence and paragraphs.
The universal sentence encoder url is used to model the input and arrive at the embedding output tensor.  

'''
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import logging

#module_url = "https://tfhub.dev/google/universal-sentence-encoder/4"
module_url = "https://www.kaggle.com/models/google/universal-sentence-encoder/tensorFlow2/universal-sentence-encoder/2"

# Tensorflow Hub loads the module based on the module URL

model = hub.load(module_url)
print("module %s loaded" % module_url)

# Function definition to formulate embedding based on list of messages which are passed as input parameter and passed on to the module

def embed(input):
  return model(input)


# Setting the Input Text or Message Data for Embedding

word = "God"
sentence = "It has been a good day so far!."
paragraph = (
    "Universal Sentence Encoder embeddings also support short paragraphs. "
    "There is no hard limit on how long the paragraph is. Roughly, the longer "
    "the more 'diluted' the embedding will be.")
paragraph1= (
    "I am trying to project a few lines in this paragraph. "
     "What we do is what we get!"
     "All are one! Be alike to everyone!!"
     "Knowledge is Power! THINK BIG!")

messages = [word, sentence, paragraph, paragraph1]


# Reduce logging output

logging.basicConfig(level=logging.ERROR)


# Invoke the embed function by passing the list of input text messages

message_embeddings = embed(messages)


# Iterate through each message present in the embeddings tensor and print the embedding snippet/output 

for i, message_embedding in enumerate(np.array(message_embeddings).tolist()):

  print("Message: {}".format(messages[i]))

  print("Embedding size: {}".format(len(message_embedding)))

  message_embedding_snippet = ", ".join(

      (str(x) for x in message_embedding[:len(message_embedding)]))

  print("Embedding: [{}]\n".format(message_embedding_snippet))