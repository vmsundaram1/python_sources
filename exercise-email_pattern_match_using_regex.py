#This program evaluates and matches a valid email address using regex pattern match

import re


email_txt1 = "sandeepgiri@cloudxlab.com"
email_txt2="msundar.ms@gmail.com"
email_txt3="_youremail @hotmail . com"
email_txt4="$#@!*&%()"
email_txt5="Common$123@gmail.com1"
email_txt6="vmsundar_1@yahoo.org.in"
email_txt7="msundaram@aero.iitm.ernet.in"
email_txt8="vmsundaram12@alumni.iitm.ac.in"



email_txt_input= input("Enter the email address to check whether it complies with a valid format (using Regex):\n")

print(email_txt_input)

#pattern = "(^[a-zA-Z][^*/+(% )]+)([@])([a-zA-Z][^*/+(% )_]+[.][a-zA-Z][^*/+(% )_]*[^0-9]$)"

#pattern = "(^[a-zA-Z][^*\\/+(% )]+)([@])([a-zA-Z][^*\\/+(% )_]+[.][a-zA-Z][^*\\/+(% )_]*[^0-9]$)"

pattern="(^[a-zA-Z][a-zA-z.0-9_-]+)([@])([a-zA-Z0-9]+[.][a-zA-Z.0-9]+[^0-9]$)"

result= re.search(pattern,email_txt_input)
#result= re.search(pattern,email_txt7)

if(result!=None):
 print("The given Email Matches the Pattern")
 x = result.groups()
 print(x, x[0]+x[1]+x[2])
else:
 print("No email Match with pattern")