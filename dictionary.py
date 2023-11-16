"""
sentence = input("Enter a sentance: ")
chars = {}
for char in sentence:
        chars[char] = chars.get(char, 0) + 1
print(chars)
"""
# a)
#The program puts all the characters of user input sentance in a dictionary with the value being how many times the letter appears

# b)
#char seperates every character in the string

# c)
#string

# d)
#The char keys are: the character
#The char values are: how many times it appears

# e)

# f)
#This call returns the value in the dictionary that corresponds to key. If the key does not exist the call returns None (unless a default value has been specified for the key). Therefore, this command never results in a KeyError
 
# g)
"""
sentence = input("Enter a sentance: ")
chars = {}
vowel = ["a","e","i","o","u"]
for char in sentence:
    if char in vowel:
        chars[char] = chars.get(char, 0) + 1
        #chars[char] = 1
print(chars)
"""
# h)
sentence = input("Enter a sentance: ")
chars = {"vowels": 0, "consonants": 0}
vowel = ["a","e","i","o","u"]

for char in sentence:
    if char in vowel:
        chars[vowels] + 1
    else:
        chars[consonants] + 1
print(char)

