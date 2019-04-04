"""
    File: exercise_2.3.py
    Author: William Gatharia
    This code demonstrates more string methods.
"""
s = "Hello World"

s.lower() #returns lowercase version of string

s.upper() #returns uppercase version of string


s.isalpha() #tests if all the string chars are alphanumeric
s.isdigit() #tests if all the string chars are digits
s.isspace() #tests if all the string chars are space

s.startswith('other') #tests if the string starts with the given other string

s.endswith('other') #tests if the string ends with the given other string

s.find('other') #searches for the given other string (not a regular expression) within s,
                #and returns the first index where it begins or -1 if not found

s.replace('old', 'new') #returns a string where all occurrences of 'old' have been replaced by 'new'

s.split('delim') #returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text.
                #e.g. 'aa,bb,cc'.split(',') produces ['aa', 'bb', 'cc']

s.split() # (no arguments) splits on all whitespace chars.

s.join(list) # opposite of split(), joins the elements in the given list together using the string as the delimiter.
             #e.g '--'.join(['aa', 'bb', 'cc']) produces aa--bb--cc

s = "Hello"
s[1:4] #produces 'ell'

s[1:] #produces 'ello'

s[:] #produces 'Hello'

#negative indexing
s[-1] #produces 'o'
s[-4] #produces 'e'

s[:-3] #produces 'He'

s[-3:] #produces 'llo'


