
#translates user input into pig latin

pyg = 'ay'

print("Enter a word")
original = raw_input('*alphabetic characters only: ')

if len(original) > 0 and original.isalpha():
  print "Original: "+original
  #convert to lower case
  word= original.lower()
  
  #get first char and append to end of
  #original string, then append 'ay'
  first = word[0]
  new_word = word + first + pyg
  
  #slice the word after the first char
  new_word = word[1:len(word)]
  
  #put it all back together
  new_word = new_word +first + pyg
  print "Translation: " + new_word
 
else:
  print 'empty or non-alpha characters entered'
