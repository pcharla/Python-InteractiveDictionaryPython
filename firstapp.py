import difflib
import json

data= json.load(open('data.json','r'))
check=''
def mydict(word):
  if word.upper() in data:
    return data[word.upper()]
    
  elif word[0] in ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
    new_word= word[0]+word[1:].lower()
    #print new_word
    if new_word in data:
      return data[new_word]
    else:
      return data[word.lower()]
  
  else:
    word= word.lower()
    if word in data:
      return data[word]
    else:
      isit= difflib.get_close_matches(word,data.keys(),3,0.8)
      isit1= ','.join(isit)
      if isit==[]:
        return ' word not found'
      else:
        check=raw_input('did you mean any of these ('+ isit1+') ' + '(y/n)')
        if check=='y':
          check2= raw_input('enter  precise word from the list')
          #check2= check2.lower()
          if check2 in isit:
            return data[check2]
          else:
            return 'are you blind ?'
        else:
          return 'word not in my lead'

test= raw_input('enter a word: ')
result= mydict(test)
#print result
if type(result) is list:
  for i in result:
    print i
else:
  print result

   
