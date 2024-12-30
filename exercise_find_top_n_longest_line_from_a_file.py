# This program determines the top 3 longest lines in a given input file and has a separate function to determine just the longest line in given input file.

# A function that determines the top 3 longest lines, returns them in a list

def find_top_n_longest_lines_func(inFile,cnt):
 done=False
# longest_3_lines = []
 temp_list=[]
 with open(inFile) as inp_fh:
  for line in inp_fh:
   line_length = len(line)
   temp_list.append((line_length,line))   
  temp_list.sort(reverse=True)
 
 return temp_list[0:cnt]


# A Function to determine the longest line in a given input file

def determine_longest_line(inFile):
 maximum=0
 t=(0,'')
 with open(inFile) as in_fh:
  for line in in_fh:
   length=int(len(line))
   if (length > maximum):
    maximum=length
    t=maximum,line

 return t       

# User Input Data Collection - File Name with extension and the last 'n' number of lines to be read/printed are collected

inputFileName=input("Enter the Input file name with extension such as .txt etc to READ the contents:\n")

count=input("Enter the number of longest lines that needs to be determined (top 'N' longest lines):\n")


# Invoking the Function Call for determining last n number of lines from a file

count=int(count)
final_result=find_top_n_longest_lines_func(inputFileName,count)


for i in final_result:
 print(i)


long_line=determine_longest_line(inputFileName)
print(long_line)
print("**********************************************************************************************\n")
print("The length of the longest line in the given input file '",inputFileName,"' is:", long_line[0],"\n\n")
print("The actual longest line in",inputFileName,"is the following line:\n")
print(long_line[1])
print("\n")
print("**********************************************************************************************\n")

