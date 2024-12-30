# This program determines counts the number of words from a given file and prints the same. A couple of functions are used to de-couple the functionality
# for processing purposes

# A function that counts the words and collects, returns them in a list


def find_keyword_and_file_write_func(inFile, keyword, outFile):
 done=False
 inp_fh =  open(inFile, "r")
 out_fh =  open(outFile,"w")
 keyword=keyword.lower()
 for line in inp_fh:
  x = line.split()
  for word in x:
   word=word.lower()
   if(word==keyword):
    out_fh.write(line)
    break
 done=True
 out_fh.close()
 inp_fh.close()

 return done 



# User Input Data Collection - File Name with extension and the last 'n' number of lines to be read/printed are collected

inputFileName=input("Enter the Input file name with extension such as .txt etc to READ the contents:\n")

outputFileName=input("Enter the Output file name with extension such as .txt etc to WRITE:\n")
00
key_word=input("Enter the KEYWORD that needs to be searched and written to the Output File:\n")


# Invoking the Function Call for determining last n number of lines from a file

done_boolean=find_keyword_and_file_write_func(inputFileName, key_word, outputFileName)
print(done_boolean)

# Final text output is printed i.e. the last 'n' number of lines from the file, after sorting the entries.

if(done_boolean==True):
 outF = open(outputFileName,"r")
 print("*******************************************Printing the Output Written to the File***************************************************\n")
 for line in outF:
  line=line.rstrip()
  print(line)
 print("*******************************************Printing the Output Written to the File***************************************************\n") 
 outF.close()