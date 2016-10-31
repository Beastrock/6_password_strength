# 6_password_strength 
## about
This script calculates **the strength of your password**.   
The result counts from __1 to 10 points__:  
1/10 - weak password, 10/10 - very strong password   
`password_strength.py` analizes  five properties of the password. Each of them can add to strength  __+2 to 0 points__. 

They are: 
* password length
* prohibition of words found in a password blacklist
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $
* inclusion of both upper-case and lower-case letters (case sensitivity)  

## lunching
You can launch it by typing following commands in console:    
First `pip install -r requirements.txt` then `python password_strength.py <your_password>`
## changing bad passwords base  
Also you can change the blacklist.  To do this: 
  change the url to new txt file in function `get_password_strength`:  
*line 21*: `base = upload_pass_base('https://yoururl.txt')`
