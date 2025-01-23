#This program evaluates a valid URL pattern to see if it is a valid URL using regex pattern match

import re


# URL pattern match

txt="https://www.domain_name.com/intro.html"
txt1="http://www.yahoo.com"
txt2="http://www.gmail.com/"
txt3="http://data.ai/"
txt4="https://www.indigo.co.in/get_one.txt"
txt5="www.traveltrip.co.in"
txt6="http://iitm.ac.in/"
txt7="http://www.sprint.co.in/sprint1/sprint/star.py"
txt8="http:/www.sprint.com"  # one slash is missing. so, it does not match
txt8a="https://127.0.0.1/sprint1/python.html"
txt8b="http://127.89.331.23/"
txt9="https:/www.sprint.com"
txt10="http//www.sprint.com"
txt11="https//www.sprcint.com"
txt12="http/www.india.com"
txt13="https/www.india.com"



#pattern = "^http|https[:]{1}[/]{2}([www|^*/+_;(% )]+)([.][a-z0-9][^*/+;_(% )])+([/][a-zA-Z0-9])*([.][a-zA-Z0-9])*"

#pattern = "^http[:][/]{2}|https[:][/]{2}([www|^*/+_;(% )]+)([.][a-z0-9][^*/+;_(% )])+([/][a-zA-Z0-9])*([.][a-zA-Z0-9])*"

pattern = "^http[:][/][/]|https[:][/][/](www|[^*/+_;(% )]+)([.][a-z0-9][^*/+;_(% )])+([/][a-zA-Z0-9])*([.][a-zA-Z0-9])*"


pattern2 = "https://[\S]+https://[\S]+"

#input_url_txt = input("Enter the URL that needs to be checked with regex pattern:\n")


result = re.search(pattern,txt)

#result = re.search(pattern,input_url_txt)

if(result!=None):
 print("The input URL matches the URL Pattern")
 print(result.groups())
else:
  print("The input URL does not match with URL pattern")



result = re.findall(pattern,txt)


if(result!=[]):
 print("The input URL matches the URL Pattern")
 print(result)
else:
  print("The input URL does not match with URL pattern")