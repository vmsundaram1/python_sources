# This program uses search based algorithm to compute fifth root of an Integer Number


# This function is used to calculate the fifth root of an Integr number without using the math function, The floor value is computed in case of floating point values 
# of fifth root value

def compute_fifth_root(lower,number1):

 start = lower
 end = number1
 temp_fifth_root=number1 

 fifth_mid_val=0.0

 if(number1==0 or number1==1): 
   return number1
 elif(number1 > 1):

  while(start<=end):

   print(start,end)

   mid_val = (start+end)//2

   print("The middle value is ",str(mid_val))

   fifth_mid_val=mid_val**5

   print(fifth_mid_val)

   if fifth_mid_val == number1:

    print("I am equal")
    return mid_val

   elif fifth_mid_val < number1:

    print("I am less")
    temp_fifth_root = float(mid_val)
    start=mid_val+1

   else:
    print("I am greater")
    end=mid_val-1
   print(start)


    
 return temp_fifth_root          
      

# Input Data Collection   

input_number=input('Enter the Integer Number for which fifth root needs to be found \n')

number = int(input_number)


# Invoking the Function to Compute Fourth Root of an Integer Number

result  = compute_fifth_root(1, number)

print("The Fifth root of the Integer",number,"is :", round(result,4))