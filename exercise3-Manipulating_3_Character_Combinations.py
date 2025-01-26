# This program is used to take the input string of three characters and print the output by considering all combinations of characters

# Checking the Input Data and Validating the correct combination of 3 unique characters
# Lowercase and Uppercase Characters are treated differently

done = False
while(not done): 
 char_list = input("Enter the value of 3 character string (lowercase/uppercase/numbers/special characters): ")
 length = len(char_list)
 print(length)
 print("************\n") 
 print(char_list[0])
 print(char_list[1])
 print(char_list[2])
 print("************\n")
 try:
     if(length!=3):
         print("Please Enter ONLY 3 characters next time!\n")
         done=False
     else:
         Z1=char_list[0]
         Z2=char_list[1]
         Z3=char_list[2]
         if(Z1==Z2 or Z2==Z3 or Z3==Z1 or Z1==Z2==Z3):
	         print("Do not Enter duplicate characters:")
	         done=False
         else:
           print("The input data validation is correct and complete!\n")
           print(Z1, Z2, Z3)
           done=True
 except:
     print("ERROR MESSAGE: There is problem with the data and processing cannot proceed further!\n")
       

# Arriving at the combination of characters by traversing through the list and building another list for holding combination of characters

final_list=[]


for chars in char_list:
    if(chars == Z1):
      tempA1=chars+Z2+Z3
      tempA2 = chars+Z3+Z2
      print(tempA1)
      print(tempA2)
      final_list.append(tempA1)
      final_list.append(tempA2)
    elif(chars == Z2):
      tempB1=chars+Z1+Z3
      tempB2=chars+Z3+Z1
      print(tempB1)
      print(tempB2)
      final_list.append(tempB1)
      final_list.append(tempB2)
    elif(chars == Z3):
      tempC1=chars+Z1+Z2
      tempC2=chars+Z2+Z1
      print(tempC1)
      print(tempC2)
      final_list.append(tempC1)
      final_list.append(tempC2)        




# Checking the List for the combination of characters and printing each element in the list

print("Printing Final List: ")

for words in final_list:
	print(words)