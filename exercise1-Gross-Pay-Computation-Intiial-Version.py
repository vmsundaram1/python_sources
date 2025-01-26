# Program to compute Gross Pay by taking Working Hours and Hourly Rate as Input


# Collecting Input Data - Total Working Hours, Hourly Rate

str_hours_worked = input("Enter the Total Work Hours: ")

str_hourly_rate = input("Enter the Charging Rate per Hour: ")


# Convert the Input Data for Computation

working_hours = int(str_hours_worked)

rate_per_hour = float(str_hourly_rate)

print(type(working_hours))

print(type(rate_per_hour))

print("Total Hours Worked :", working_hours)

print("Charging Rate per Hour:", rate_per_hour)


# Computing Gross Pay and Printing the Value

str_gross_pay = working_hours*rate_per_hour

print("Gross Pay = ", str_gross_pay)



