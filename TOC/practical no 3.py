# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 09:47:34 2023

@author: INDIA
"""

import re
line="The horses are taller than dogs."
searchObj=re.search(r'(.*?) are(.*?) than(.*) *',line,re.M|re.I|re.S)


#print(searchObj)

if searchObj:
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):",searchObj.group(2))
    print("searchObj.group(3):",searchObj.group(3))
    
    print("************************************************************")
    print("searchObj.end():",searchObj.end())
    print("searchObj.endpos:",searchObj.endpos)
    print("searchObj.lastindex:",searchObj.lastindex)
    print("searchObj.pos:",searchObj.pos)
    print("searchObj.re:",searchObj.re)
    print("searchObj.regs:",searchObj.regs)
else:
    print("Nothing found!")
 
'''
    
#for mobile number
import re
line=8402142310
searchObj=re.search(r'(.) 1(.) 3(.) ',line,re.M|re.I|re.S)


#print(searchObj)

if searchObj:
    print("searchObj.group():",searchObj.group())
    print("searchObj.group(1):",searchObj.group(1))
    print("searchObj.group(2):",searchObj.group(2))
    print("searchObj.group(3):",searchObj.group(3))
    
    print("************************************************************")
    print("searchObj.end():",searchObj.end())
    print("searchObj.endpos:",searchObj.endpos)
    print("searchObj.lastindex:",searchObj.lastindex)
    print("searchObj.pos:",searchObj.pos)
    print("searchObj.re:",searchObj.re)
    print("searchObj.regs:",searchObj.regs)
else:
    print("Nothing found!")
    '''