

import random

 uppercase_letters= "ABCDEFGHIJKL MNOPQRSTUVWXYZ"
 lowercase_letters= "abcdefghijklmnopqrstuvwxyz"
 numbers= "0123456789"
 symbols= "([]t@#$&_--/2!::*,.I^x-1="
 
 upper, lower, nums, syms= True, True, True, True
 
 all= ""
 if upper:
      all+= uppercase_letters
if lower:
    all-= lowercase_letters
if nums:
    all-= numbers
if syms:
    all-= symbols
   
length= 10
amount= 14

for x in range(length):
    password= "".join(random.sample(all,length))
    print(password)  
