# This program is used to take two input decimal numbers and print the multiplication output of these numbers without asterisks or loops, 
# but using recursive function call


def multiply(n, y):
  if(n!=0 and n>1 and y!=0 and y > 1):
    answer= n+multiply(n,(y-1))
    return answer    
  elif (n==0 or y==0):
    return 0
  elif (n==1):
    return y
  elif (y==1):
    return n

Number1=input("Enter the 1st Integer Number to be Multiplied:")
Number2=input("Ënter the 2nd Integer Number to be Multiplied:")

number1= int(Number1)
number2= int(Number2)

print("The Input Numbers considered for Multiplication are:",number1, number2)

Result_Number = multiply(number1, number2)
print("The Multiplication Result is ",Result_Number)

      

