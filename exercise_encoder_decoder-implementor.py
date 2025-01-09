'''
THis program is used to take input details of customer data from an input file, encodes the email_id and maintains the encoded emails in an output file.
Later, the encoded set of emails are fetched from the file and decoded using a function. The final result is written to a separate output file based on the 
recommendations.

'''

# FUnction to Encode each element in a given array and return the encoded array/list

def encode_func(inp_array):

 length = len(inp_array)
 encoded_text = []

 for i,val in enumerate(inp_array):
  text=[]
  for char in val:
   text.append(ord(char))
#   text.append(ord("-"))

  encoded_text.append(text) 
 
 return encoded_text


# FUnction to Decode each element in an encoded array/list and return the decoded array/list

def decode_func(encoded_str_arr):

 length = len(encoded_str_arr)
 decoded_text=[]
 
 for i, val in enumerate(encoded_str_arr):
  decoded_val=""
  for num in val: 
#   if chr(num)!="-":
   decoded_val+=chr(num)
  decoded_text.append(decoded_val) 
 
  
 return decoded_text

# Encode a given input string and return output as string

def encode_string(val):
 encoded_text=[]
 for char in val:
  encoded_text.append(ord(char))

 return encoded_text


# Decode a given input encoded string and return output as normal string

def decode_string(val):
 decoded_text=""
 print("I am inside 1 decode string function",val)

 desired_array = [int(n) for n in val] 

 for num in desired_array:
  decoded_text+=chr(num)
 
 return decoded_text


# Main Program Starts


# Sample Data for Testing encoding and decoding of data

input_list = []

input_list = ["sandeep@gmail.com", "msundar.ms@gmail.com", "ssmahe@hotmail.com", "vmsundaram1@yahoo.com", "ms679107@gmail.com"]


encoded_result_arr = encode_func(input_list)

print("The encoded result is ", encoded_result_arr)

decoded_result_arr = decode_func(encoded_result_arr)

print("The decoded result is ",decoded_result_arr)


# Actual Data is read from an input file, encoding is done using a function call.
# The encoded email is written to a separate output file

input_file="input_parameters.txt"

encoded_file="encoded_emails.txt"

customer_info=[]

with open(input_file) as inp_fh,open(encoded_file,"w") as out_fh:
 lines=inp_fh.readlines()
 for line in lines:
  words = line.strip('').split()
  if(len(words)==3):
   if("email_id" in words):
    print("I am skipping the 1st line")
    continue 
   else:
    print("I am reading after 1st line")
    temp = encode_string(words[0])
    member = (temp,words[1],words[2])
    customer_info.append(member)       
          

 my_it = iter(customer_info)
 out_fh.write("		email_id	\n")
 for i in range(len(customer_info)):

# print("The details of encoded record ",str(i+1),"is",next(my_it)) - We need to write only email id, so product_code and score are skipped
  out_fh.write(str(next(my_it)[0]))
  out_fh.write("\n")


print("Now, the decoding part will execute through file handling")

# Decoding the data and writing to a file

final_out_data_file = "final_out1.txt"

with open(encoded_file) as mapping_fh, open(final_out_data_file,"w") as final_out_fh:

 length_of_words=0
 decoded_arr=[] 
 arr_list=[]
 for line in mapping_fh:
  temp_val=''
  if(str(customer_info[0][0])==str(line)):
   print("The check is complete")
  words = line.split()
  if("email_id" in words):
   continue
  arr_list=line
  print("The value of the encoded email in a list is",line)
  txt1=line.strip()
  txt1=txt1.replace("[","")
  txt1=txt1.replace("]","")
  txt1=txt1.split(",")
  temp_val=decode_string(txt1)
  decoded_arr.append(temp_val)
    


# Parsing the decoded array and writing data to the output file

 final_it = iter(decoded_arr)
 i=0
 j=0
 final_out_fh.write("	email_id	"+"		product_code	"+"	score	"+"\n")
 while(i<len(decoded_arr) and j<len(customer_info)):
  final_out_fh.write(next(final_it))
  final_out_fh.write("			") 
  final_out_fh.write(customer_info[i][1])
  final_out_fh.write("			")
  final_out_fh.write(customer_info[i][2])
  final_out_fh.write("\n")
  i+=1
  j+=1
  