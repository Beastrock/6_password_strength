# 6_password_strength 
  This script calculates **the strength of your password**.   
  The result estimates from __1 to 10 points__:  
1/10 - weak password  
|  
|  
10/10 - very strong password

`password_strength.py` was analizes  five properties of the password. Each of them can give the strength __+2 to 0 points__.

They are: 

* password length
* prohibition of words found in a password blacklist
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $
* inclusion of both upper-case and lower-case letters (case sensitivity)

## how it works##  
To lunch the script first `pip install -r requirements.txt` then `python password_strength.py` and input your password.  

Also you can change the blacklist.  To do this: 
  change the url in `get_password_strength` function:  
  `base = upload_pass_base('https://yoururl.txt')`
   
