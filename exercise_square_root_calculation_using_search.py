# This program uses search based algorithm to compute square root of an Integer Number


# This function is used to calculate the square root of the number without using the math function, The floor value is computed in case of floating point values of
# square root value


def compute_square_root(lower,number1):

 start = lower
 end = number1
 temp_sqr_root=number1 

 sqr_mid_val=0.0

 if(number1==0 or number1==1): 
   return number1
 elif(number1 > 1):

  while(start<=end):

   print(start,end)

   mid_val = (start+end)//2

   print("The middle value is ",str(mid_val))

   sqr_mid_val=mid_val*mid_val

   print(sqr_mid_val)

   if sqr_mid_val == number1:

    print("I am equal")
    return mid_val

   elif sqr_mid_val < number1:

    print("I am less")
    temp_sqr_root = float(mid_val)
    start=mid_val+1

   else:
    print("I am greater")
    end=mid_val-1
   print(start)


#     end=number1
    
 return temp_sqr_root          
      
   
# Input Data Collection   


input_number=input('Enter the Integer Number for which square root needs to be found \n')

number = int(input_number)


# Invoking the Function to Compute Cubic Root of an Integer Number


result  = compute_square_root(1, number)

print("The square root of ",number,"is :", round(result,4))