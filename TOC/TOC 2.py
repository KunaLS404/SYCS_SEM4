# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 09:32:00 2022

@author: INDIA
"""
import re

'''
#Email
x="ABC-1055"
if re.search("\d{3}-\d{3}-\d{4}",x):
    print("It is a phone number")
    
    
x="8959674518"
if re.search("[89] [0-9]{9}",x):
    
    print("It is a phone number")
else:
    print("It is not a phone number")
    '''
    
#Email
x="asbsd123@gmail.com"
if re.search("[a-zA-Z-0-9_\-\]+@[a-z]+[\.][a-z{2,3}]",x):
    
    print("It is a EMAIL Id")
    
else:
    print("It is not a EMAIL Id")