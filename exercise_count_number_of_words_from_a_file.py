# This program determines counts the number of words from a given file and prints the same. A couple of functions are used to de-couple the functionality
# for processing purposes

# A function that counts the words and collects, returns them in a list


def count_words_func(fileName):
 d={ }
 with open(fileName) as fh:
  words = fh.read().split()
  for word in words:
   word=word.lower()
   if word in d:
    d[word]+=1
   else:
    d[word]=1
 return d


def order_by_value(myDict):
 final_list = []
 for key,val in myDict.items():
  print(key,val)
  final_list.append((key,val))
 final_list.sort()
 return final_list 

# User Input Data Collection - File Name with extension and the last 'n' number of lines to be read/printed are collected

fileName=input("Enter the file name with extension such as .txt etc:\n")


# Invoking the Function Call for determining last n number of lines from a file

result_txt=count_words_func(fileName)


# Final text output is printed i.e. the last 'n' number of lines from the file, after sorting the entries.

length = int(len(result_txt))

result = order_by_value(result_txt)

print("*******************************************After Sorting Dictionary Items and populating in a list***************************************************\n")
#for i,val in enumerate(result):
# print(val[0],val[1])

myiter=iter(result)
i=0
while i < length:
 temp = next(myiter)
 print("Word-",temp[0],"Count=",temp[1])
 i+=1

print("*******************************************After Sorting Dictionary Items and populating in a list***************************************************\n")