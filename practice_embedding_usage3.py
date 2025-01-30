'''
This program is used to implement embedding of different text message formats - a word, a sentence and paragraphs.
Different types of models through universal sentence encoder urls are used to process the input messages and arrive at the embedding output tensor.  
The tensor holds the embeddings of each message and the length of each embedding vector is 512
The messages and the embeddings are plotted to see if there are any simlarities between different messages
The semantic similarity of two sentences is trivially computed as the inner product of the encodings. 

'''

import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import seaborn as sns

# Function definition to provide embeddings when any set of messages are passed as an argument

def embed(input):
  return model(input)

# Function definition that considers labels as messages and features as embeddings. The output shows the similarity between different messages by considering their
# embeddings and plot them

def plot_similarity(labels, features, rotation):
 corr = np.inner(features, features)
 sns.set(font_scale=1.2)
 g = sns.heatmap(
      corr,
      xticklabels=labels,
      yticklabels=labels,
      vmin=0,
      vmax=1,
      cmap="YlOrRd")
 g.set_xticklabels(labels, rotation=rotation)
 g.set_title("Semantic Textual Similarity")


def run_and_plot(messages_):
 message_embeddings_ = embed(messages_)
 plot_similarity(messages_, message_embeddings_, 90)


# Main Program Starts - module url is passed as an input and tfhub loads the model

module_url = "https://www.kaggle.com/models/google/universal-sentence-encoder/tensorFlow2/universal-sentence-encoder/2"

# Tensorflow Hub loads the module based on the module URL

model = hub.load(module_url)
print("module %s loaded" % module_url)


# Different categories of Input messages are considered for illustrating the correlation between message

messages = [
    # phones
    "Phone running on Android is better than iOS",
    "I have a mobile phone connection",
    "I do have a landline number!",

    # climate or weather
    "It won't rain tomorrow!",
    "Thunderstorm prediction turned out to  be true in Northern India",
    "The climate here is bit sunny today",

    # Food or Health
    "Apple is Red and Oranges are Blue",
    "Health is Wealth",
    "Eating timely food helps to prevent ulcer complaints in humans",

    # Age related statements
    "Those who are in 40-50 age band would need to take care of themselves ",
    "The gym enrolment concessions are given for only youth who are above 15+ years",
]

# Invoking the function to determine embeddings of the input messages and plot them to determine the correlation based on the inner product of the encodings

run_and_plot(messages)