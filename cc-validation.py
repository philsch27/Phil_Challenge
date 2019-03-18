#!/usr/local/bin/python3
#

import re 

def checkdup(num):
    clean=re.sub('[\-]','',num)
    chars=re.findall(r'.',clean)
    count=1
    card="Valid"
    for i in range(len(chars)-1):
        if chars[i] == chars[i+1]:
           count += 1
           if count == 4:
              card="Invalid"
              break
        else:
           count = 1
    return card

pattern='^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'

card_count=int(input(''))
for i in range(card_count):
    cardno=input('')
    if re.match(pattern,cardno):
       valid=checkdup(cardno)
       print(valid)
    else:
       print ('Invalid')


