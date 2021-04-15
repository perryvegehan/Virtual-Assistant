# regular expressions allow us to search for patterens in text

# used when we don't know the exact text but we know the pattern
# for eg: (+91)8210013208:  this is a number (+91) is sure but after that any 10 digits can be there
# the regular expression for this would be
# r"(+91)\d\d\d\d\d\d\d\d\d\d"  OR r"(+91)\d{10}  ---->> (+91) followed by 10 digits

# let us create a sample text
text="Agent Sam's phone number is (+91)8210013208 and the phone number of his dad is (+91)7033890684"
# for simple words, we can use the in operator
res="phone" in text
print(res) # true
res="pratyush" in text
print(res) # false
# now let us use re

import re
pattern="phone"
print(re.search(pattern,text)) # it will tell us if there is a match and also the starting and end index of the match
new_pattern="Not in text"
print(re.search(new_pattern,text)) # gives answer none

# we can store the match results in a variable
match=re.search(pattern,text)
print(match.span())
# But if we have multiple matches it still gives back only one match. for multiple matches, we will use findAll()
match=re.findall(pattern,text) # findall() gives a list of all the matches.
print(match)
# if we want we can iterate through the match objects. for that use the finditer method
for match in re.finditer(pattern,text):
    print(match.span())

# to match using regular expressions, we have to lookup this table
#  Character       Description       Pattern Code                 Example
#    \d            digits            fixed_text\d\d\d             fixed_text123
#    \w      (letters or numbers)     \w-\w\w\w                    A-b_1
#
#    \s            whitespace         A\sB\sC                     A B C
#    \D            Non-Digit          \D\D\D                      ABC
#    \W            Special characters  \W\W\W\W                   *=+)

text="My phone number is 408-5555-908"
# notice the phone number pattern
phone_search=re.search(r'\d\d\d-\d\d\d\d-\d\d\d',text) # it will give the match
print(phone_search)
# now notice that even when the phone number is anything the match will give the results. it only checks for the pattern
# and not for any particular string
# we can grab the matched phone number by the group method
print(phone_search.group())
text="My phone number is 455-6676-900 and my father phone number is 234-4444-567 and my mother phone number is 456-3333-897"
for phone_search in re.finditer(r'\d{3}-\d{4}-\d{3}',text):
    print(phone_search.group()) # lists out all the phone numbers

# ths {3} that we used is a QUANTFIER. It is same as toc regular expressions.

#   Quantifier         Description
#     +                 once or more
#     *                 zero or more
#     {3}               exactly three times
#     {2,5}             occurs 2 to 5 times
#     {3,}              occurs 3 times or more
#     ?                 either occurs once or none (singular only)

text="The sample string contains either 111 or 1111 or 11111."
for i in re.finditer(r'\d{3,5}',text):
    print(i.group())

text="My phone number is 455-6676-900 and my father phone number is 234-4444-567 and my mother phone number is 456-3333-897"

# we want to match the phone numbers and also extract the first 3 digits of all the phone numbers.
# here we can use the compile function. what it does is divide a regular expression into many groups.
phone_pattern=re.compile(r'(\d{3})-(\d{4})-(\d{3})')
for i in re.finditer(phone_pattern,text):
    print(i.group(1)) # prints the matches of first regular expression
    print(i.group(2)) # prints the matches of second regular expression
