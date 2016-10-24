# 6_password_strength 
  This script calculates **the strength of your password**. The result estimates from __1__ to __10__ points. 
1 - weak password
10 - very strong password

`password_strength.py` was analized  five properties of the pass. Each of them can give the strength +2 to 0 points.

They are: 

* password length
* prohibition of words found in a password blacklist
* inclusion of one or more numerical digits
* inclusion of special characters, such as @, #, $
* inclusion of both upper-case and lower-case letters (case sensitivity)

___

Also you can change the blacklist.  To do this: 
  change the url in `get_password_strength` function:
  `base = upload_pass_base('**https://yoururl.txt**')`
   
