# Program to compute Gross Pay by taking Working Hours and Hourly Rate as Input, Hourly Rate is increased for working hours greater than 40

# Collecting Input Data - Total Working Hours, Hourly Rate

str_hours_worked = input("Enter the Total Work Hours: ")
str_hourly_rate = input("Enter the Charging Rate per Hour: ")


# Convert the Input Data for Computation, Checking the conformance of Input and throwing Error Message for incorrect input

try:
    working_hours = int(str_hours_worked)
    rate_per_hour = float(str_hourly_rate)

    print(type(working_hours))
    print(type(rate_per_hour))

    print("Total Hours Worked :", working_hours)
    print("Charging Rate per Hour:", rate_per_hour)

except:

	print("Type cast Error, Check the data type of Inputs and Provide Numeric Data in Integer format!") 
	exit()

# Computing Gross Pay and Printing the Value, Throwing Error Message if numeric computation yields error

try:

   if(working_hours > 40):
   	modified_rate_per_hour = 1.5*rate_per_hour
   	str_gross_pay = working_hours*modified_rate_per_hour
   	print("working Hours is Greater than 40: ", working_hours,"\nHourly Rate is Revised: ",modified_rate_per_hour)
   else:
   	str_gross_pay = working_hours*rate_per_hour
   	print("working Hours is Less than 40: ", working_hours,"\nHourly Rate is Same: ",rate_per_hour)


   print("Gross Pay = ", str_gross_pay)

except:

	print("There is an Error; Check the Input data :")





  
