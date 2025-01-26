# Program to compute Compound Interest

# Collecting Input Data - Principal, Rate of Interest, Number of Years

str_principal = input("Enter the Principal: ")
str_interest_rate = input("Enter the Rate: ")
str_years = input("Enter the Number of Years: ")


# Convert the Input Data for Computation

p=int(str_principal)
r=float(str_interest_rate)
n=int(str_years)

print(type(p))
print(type(r))
print(type(n))

print("Prinicpal :", p)
print("Rate of Interest :", r)
print("Number of Years: ", n)

# Computing Compound Interest using Formula and Printing the Output

str_compound_interest = p*((1+r/100)**n)
print("Data Type of Compound Interest: ", type(str_compound_interest))
print("Compound Interest = ", str_compound_interest)
