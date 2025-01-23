# THis program matches a given input string with the regex pattern

# A Function Defintion - to match the pattern with the given input text

# Function to determine if given pattern matches with a string or not

def match_pattern(str, pat, dict, i=0, j=0):

 str_length_n = len(str)
 pattern_length_m = len(pat)


# basic condition

 if str_length_n < pattern_length_m:
  return False

# if both pattern and the string reaches end

 if i == str_length_n and j == pattern_length_m:
  return True

# if either string or pattern reaches end

 if i == str_length_n or j == pattern_length_m:
  return False

# consider next character from the pattern
 curr = pat[j]

# if the character is already present or available
 if curr in dict:

  s = dict[curr]
  print("The value of curr and s are:",curr,s)
  k = len(s)

# sub_str stores next k characters of the given string

  if i + k < len(str):
   sub_str = str[i:i + k]
  else:
   sub_str = str[i:]

# return false if next k characters doesn't match with s value

  if sub_str != s:
   return False

# call recursively for remaining characters if next k characters matches

  return match_pattern(str, pat, dict, i + k, j + 1)

# process all remaining characters in the string if current character was not present earlier

 for k in range(1, str_length_n - i + 1):

# insert substring formed by next k characters of the string into the dictionary

  dict[curr] = str[i:i + k]

# check if it yields the solution by making a recursive call

  if match_pattern(str, pat, dict, i + k, j + 1):
   return True

#  otherwise, current character is deleted from the dictionary

  dict.pop(curr)

 return False






# A function definition for executing test cases

def testing_func(testcases):
 dict = {}
 for test_case in testcases:
  arr,expected = test_case
#  actual = match_pattern(arr[0],arr[1])
  actual = match_pattern(arr[1],arr[0],dict)
  print("Pattern is",arr[0],"Text is",arr[1])
  if(actual==expected):
   print("Result is Successful")
  else:
   print(f"\tFailed: Expected Result should be {expected} but got {actual}\t\n")

# Main Program Starts

testcases= [
 	    (("a...*","abcde"),True),
	    (("abc","abc"),True),
 	    (("a*","abcde."),True),
            (("a.","a1"),True),
	    (("a.","a"),False),
            (("a?","a "),True)
            ]


pattern="*?"
input_text="abc123"

print(len(pattern),len(input_text))


#if __name__ == '__main__':

# input string and pattern

str = "God is Good"

pat= "G.G*"

# create a dictionary to store mappings between the pattern and string

dict = {}

# check for solution

if match_pattern(str, pat, dict):
 print(dict)
else:
 print("Solution doesn't exist")

'''

if(bool==True):
 print("The given input text matches with the pattern:\n")
else:
 print("The given input text does not match with the pattern:\n")

'''

testing_func(testcases)



