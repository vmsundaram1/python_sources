# This program is used to extract the information from a file

import re

pattern1 = "^http[:][/][/]|https[:][/][/](www|[^*/+_;(% )]+)([.][a-z0-9][^*/+;_(% )])+([/][a-zA-Z0-9])*([.][a-zA-Z0-9])*"
pattern2 = "http://[\S]+|https://[\S]+"

# Function Definition to check 

def url_pattern_check(input_file):


 with open(input_file) as inp_fh:
  handle = inp_fh.readlines()   
  count=0
  if(handle!='' or handle!=None or handle!=[]):
   for line in handle:
    count=count+1
# Using re.findall method

    print("************Results of URL matches based on FINDALL METHOD PATTERN-1*****************\n")  

    url1 = re.findall(pattern1,line)

    if(url1!=[]):
     print("The input file data does HAS entry matching URL pattern\n")
     print("Using FINDALL METHOD Pattern 1 Check for LINE NUMBER:",count,":",url1,line)
     print("**********************************************************************\n")
    else:
     print("The input file data DOES NOT HAVE an entry matching URL pattern for LINE NUMBER:",count,"\n")
     print("**********************************************************************\n")


    print("************Results of URL matches based on FINDALL METHOD PATTERN-2*****************\n")  

    url2 = re.findall(pattern2,line)
    if(url2!=[]):
     print("The input file data does HAS entry matching URL pattern\n")
     print("Using FINDALL METHOD Pattern 2 Check for LINE NUMBER:",count,":",url2,line)
     print("**********************************************************************\n")
    else:
     print("The input file data DOES NOT HAVE an entry matching URL pattern for LINE NUMBER:",count,"\n")
     print("**********************************************************************\n")



# Using re.search method

    print("************Results of URL matches based on SEARCH METHOD PATTERN-1*****************\n")

    url1 = re.search(pattern1,line)
    if(url1!=None):
     print("The input file data does HAS entry matching URL pattern\n")
     print("Using SEARCH METHOD Pattern 1 Check for LINE NUMBER:",count,":",url1.groups(),line)
     print("Using SEARCH METHOD Pattern 1 Check for LINE NUMBER:",count,":",url1.group(),line)
     print("**********************************************************************\n")
    else:
     print("The input file data DOES NOT HAVE an entry matching URL pattern for LINE NUMBER:",count,"\n")
     print("**********************************************************************\n")

    print("************Results of URL matches based on SEARCH METHOD PATTERN-2*****************\n")
  
    url2 = re.search(pattern2,line)
    if(url2!=None):
     print("The input file data does HAS entry matching URL pattern\n")
     print("Using SEARCH METHOD Pattern 2 Check for LINE NUMBER:",count,":",url2.groups(),line)
     print("Using SEARCH METHOD Pattern 2 Check for LINE NUMBER:",count,":",url2.group(),line)
     print("**********************************************************************\n")
    else:
     print("The input file data DOES NOT HAVE an entry matching URL pattern for LINE NUMBER:",count,"\n")
     print("**********************************************************************\n")


# Main Program Starts

done=False

while(not done):
 input_text = input("Enter the name of the input file containing the URLs:\n")
 input_split_text=input_text.split(".")

 if(input_text!="" and len(input_split_text)>1):
  url_pattern_check(input_text)
  done=True
 else:
  print("Please check and re-enter the input file name correctly:\n")
  done=False
