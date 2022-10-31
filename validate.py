
import re
welcome_msg = """
========================================
==== Welcome to Password Validator! ====
========================================
"""
print(welcome_msg)
#2
while True:
  #3 Enter User Password
  user_input = input("Enter a password : ")

  is_valid = False

  if (len(user_input)>9 and len(user_input)<12):
    #4 Check the length of the password
    print('''The password should meet the following rules:
        1) Password must be between 9 and 12 characters
        2) Password must contain 5 letters [a-z A-Z]
        3) Password must contain at least 3 special characters ['&', '#'. '$', '!', '?', '"', '(', ')', '.']''')
    print("Your Password is: ", user_input)
    print("Validation Failed: You need to have a minimum of 9 and a maximum of 12 characters")
    
    continue
  elif not re.search("[A-Z]",user_input):
    #5 Check every character if it contains Capital Letters
    print(''' The password should meet the following rules:
        1) Password must be between 9 and 12 characters
        2) Password must contain 5 letters [a-z A-Z]
        3) Password must contain at least 3 special characters ['&', '#'. '$', '!', '?', '"', '(', ')', '.']''')
    print("Your Password is: ", user_input)    
    print("Validation Failed: The Password should contain one letter between [A-Z]")
    
    continue
  elif not re.search("[a-z]",user_input):
    #6 Check every character if it contains small Letters
    print(''' The password should meet the following rules:
        1) Password must be between 9 and 12 characters
        2) Password must contain 5 letters [a-z A-Z]
        3) Password must contain at least 3 special characters ['&', '#'. '$', '!', '?', '"', '(', ')', '.']''')
    print("Your Password is: ", user_input)
    print("Validation Failed: The Password should contain one letter between [a-z]")
    
    continue
  elif not re.search("[1-9]",user_input):
    #7 Check every character if it contains values from 0 - 9
    print(''' The password should meet the following rules:
        1) Password must be between 9 and 12 characters
        2) Password must contain 5 letters [a-z A-Z]
        3) Password must contain at least 3 special characters ['&', '#'. '$', '!', '?', '"', '(', ')', '.']''')
    print("Your Password is: ", user_input)
    print("Validation Failed: The Password should contain one letter between [1-9]")
    continue
  elif not re.search("""[~!@#$%^"&*]""",user_input):
    #8 #7 Check every character if it contains character given
    print(''' The password should meet the following rules:
        1) Password must be between 9 and 12 characters
        2) Password must contain 5 letters [a-z A-Z]
        3) Password must contain at least 3 special characters ['&', '#'. '$', '!', '?', '"', '(', ')', '.']''')
    print("Your Password is: ", user_input)
    print("Not valid ! It should contain at least 3 special character in [~!@#$%^&*]")
    continue
  
  else:
    #10
    is_valid = True
    break

#11
if(is_valid):
    print(''' The password should meet the following rules:
        1) Password must be between 9 and 12 characters
        2) Password must contain 5 letters [a-z A-Z]
        3) Password must contain at least 3 special characters ['&', '#'. '$', '!', '?', '"', '(', ')', '.']''')
    print("Your Password is: ", user_input)
    print("Validation Succeeded!")
