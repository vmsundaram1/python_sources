import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
from scipy.spatial.distance import cityblock, euclidean, cosine


def cosine_similarity1(v1,v2):
 similarity=0
 print(len(v1),len(v2))
 if(len(v1)==len(v2)):
  for i in range(len(v1)):
   similarity+= v1[i]*v2[i]
 else:
  print("The length of two vectors are not equal")
 return similarity 

def cosine_similarity2(v1,v2):

 v1_flat = v1.flatten()
 v2_flat = v2.flatten()

 if(len(v1_flat)!=len(v2_flat)):
  print("The length of two vectors are not equal")
 else:
	# Calculate similarity

  similarity = np.dot(v1_flat, v2_flat) / (np.linalg.norm(v1_flat) * np.linalg.norm(v2_flat))

 return similarity




'''
The value will range between -1 and 1:

1 indicates that the two vectors are exactly the same direction.

0 indicates that the vectors are orthogonal (perpendicular) and share no similarity.

-1 indicates that the vectors are diametrically opposed.

'''

def cosine_similarity(v1,v2):


 if(len(v1)!=len(v2)):
  print("The length of two vectors are not equal")
 else:
	# Calculate similarity

  similarity = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

 return similarity




url1 = "https://tfhub.dev/google/universal-sentence-encoder/4"
url2 = "https://www.kaggle.com/models/google/universal-sentence-encoder/tensorFlow2/universal-sentence-encoder/2"
url = "https://tfhub.dev/google/universal-sentence-encoder/4"

msg1 = "My experience is that this feature of product is really useful and beneficial in the long run"

msg2 = "Ït is one of the slowest website I have come across till now." 

msg3 = "This is the latest available functionality that will really ensure faster checkout process and it is a boon to all users." 

msg4 = "I may not be able to use this product frequently."

msg5 = "The storage option for this mobile phone is good and excellent."


embed = hub.load(url1)


embeddings_pos_numpy = embed(["Positive Comment",]).numpy()
embeddings_neg_numpy = embed(["Negative Comment",]).numpy()
embedding_msg1_numpy = embed([msg1]).numpy()
embedding_msg2_numpy = embed([msg2]).numpy()
embedding_msg3_numpy = embed([msg3]).numpy()
embedding_msg4_numpy = embed([msg4]).numpy()
embedding_msg5_numpy = embed([msg5]).numpy()

embeddings_pos = embeddings_pos_numpy.flatten()
embeddings_neg = embeddings_neg_numpy.flatten()
embedding_msg1 = embedding_msg1_numpy.flatten()
embedding_msg2 = embedding_msg2_numpy.flatten()
embedding_msg3 = embedding_msg3_numpy.flatten()
embedding_msg4 = embedding_msg4_numpy.flatten()
embedding_msg5 = embedding_msg5_numpy.flatten()

for i, a in enumerate([embedding_msg1,embedding_msg2,embedding_msg3,embedding_msg4,embedding_msg5]):

# Determination of Cosine Similarity based on Cosine Distance Computation

 cosine_pos = cosine(embeddings_pos,a)
 cosine_neg = cosine(embeddings_neg,a)

 if (cosine_pos < cosine_neg):
  print("Message "+str(i)+" Cosine Similarity - Positve :"+str(cosine_pos)+"Positive Review Comment\n")
 else:
  print("Message "+str(i)+" Cosine Similarity - Negative :"+str(cosine_neg)+"Negative Review Comment\n")

# Manhattan Distance Computation

 manhattan_distance_pos = cityblock(embeddings_pos,a)
 manhattan_distance_neg = cityblock(embeddings_neg,a)

 if(manhattan_distance_pos < manhattan_distance_neg):
  print("Message "+str(i)+" Manhattan Distance-Positive :"+str(manhattan_distance_pos)+"Positive Review Comment\n")
 else:
  print("Message "+str(i)+" Manhattan Distance-Negative :"+str(manhattan_distance_neg)+"Negative Review Comment\n")


# Euclidean Distance Computation

 euclidean_distance_pos =  euclidean(embeddings_pos,a)
 euclidean_distance_neg =  euclidean(embeddings_neg,a)

 if(euclidean_distance_pos < euclidean_distance_neg):
  print("Message "+str(i)+" Euclidean Distance - Positve :"+str(euclidean_distance_pos)+"Positive Review Comment\n")
 else:
  print("Message "+str(i)+" Euclidean Distance - Negative :"+str(euclidean_distance_neg)+"Negative Review Comment\n")


# Cosine Similariy Computation - whichever is closer to 1 is similar - so comparing greater values for similarity unlike distance in other cases


 manual_cosine_similarity_pos = cosine_similarity(embeddings_pos,a) 
 manual_cosine_similarity_neg = cosine_similarity(embeddings_neg,a)
 
 print("+ve cosine similarity value is", manual_cosine_similarity_pos)
 print("-ve cosine similarity value is", manual_cosine_similarity_neg)
 

 if (manual_cosine_similarity_pos > manual_cosine_similarity_neg):  
  print("Message "+str(i)+" Manual Cosine Similarity - Positve :"+str(manual_cosine_similarity_pos)+"Positive Review Comment\n")
 else:
  print("Message "+str(i)+" Manual Cosine Similarity - Negative :"+str(manual_cosine_similarity_neg)+"Negative Review Comment\n")


