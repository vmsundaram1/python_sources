# This program uses search based algorithm to compute fourth root of an Integer Number


# This function is used to calculate the fourth root of an Integr number without using the math function, The floor value is computed in case of floating point values 
# of cubic root value

def compute_fourth_root(lower,number1):

 start = lower
 end = number1
 temp_fourth_root=number1 

 fourth_mid_val=0.0

 if(number1==0 or number1==1): 
   return number1
 elif(number1 > 1):

  while(start<=end):

   print(start,end)

   mid_val = (start+end)//2

   print("The middle value is ",str(mid_val))

   fourth_mid_val=mid_val*mid_val*mid_val*mid_val

   print(fourth_mid_val)

   if fourth_mid_val == number1:

    print("I am equal")
    return mid_val

   elif fourth_mid_val < number1:

    print("I am less")
    temp_fourth_root = float(mid_val)
    start=mid_val+1

   else:
    print("I am greater")
    end=mid_val-1
   print(start)


    
 return temp_fourth_root          
      

# Input Data Collection   

input_number=input('Enter the Integer Number for which Fourth root needs to be found \n')

number = int(input_number)


# Invoking the Function to Compute Fourth Root of an Integer Number

result  = compute_fourth_root(1, number)

print("The Fourth root of the Integer",number,"is :", round(result,4))