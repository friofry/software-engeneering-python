# A regular expression (or RE) specifies a set of strings that matches it

# Online tools:
#   https://rubular.com/
#   https://regexr.com/

# API: https://docs.python.org/3/library/re.html

import re

# Syntax
# Special characters . ^ $ * + ? { } [ ] \ | ( )

# [] - set (one of)
# (h[aoe])+ : haha, hoho, hehe

# \ - escape special characters
# a[\\\]]b : a\b, a]b

# character classes \w, \s, \d
#
# \s - white space (\S not white space)
# \d - digit (\D not digit)
# \x - hex digit
# \w - word (\W not word)

# anchors ^, $, \b,\Z
#
# ^ - start of the string (\A)
# $ - end of the string (\Z)
# \b - word boundary (\B not word boundary)
# \< - start of word
# \> - end of word

# Groups
# (a|b)    - a or b
# .        - any character
# [abc]    - range from a to c (a or b or c)
# [^abc]   - not a and not b and not c
# [0-7]    - range from 0 to 7
# [a-zA-Z] - range from a to z and A-Z

# Quantifiers
#
# *        - 0 or more
# +        - 1 or more
# ?        - 0 or 1
# {3}      - 3 times
# {3,4}    - 3 or 4 times
# {3,}     - 3 and more
# {,4}     - up to 4 times


# Typical usages:
# 1. check phone,IP or email format
def match_test():
    email_regex = "^([\w\.\-]+)@([\w\-]+)((\.(\w){2,3})+)$"
    email_pattern = re.compile(email_regex)
    m = email_pattern.match("some.email@gmail.com")
    if m:
        print('Match found: ', m.group())
    else:
        print('No match')


# 2. Split to substrings
def split_substrings():
    result = re.split(r'[,;\. ]+', 'word1, word2, word3; word4; word5. word6')
    print(result)

    result = re.split(r'[,;. ]+', 'word1, word2, word3; word4; word5. word6')
    print(result)


# 3. Find patterns
def findall_test():
    result = re.findall(r'\d+', 'ball 10$, horse 20$, train 30$')
    print(result)


# 4.
def search_test():
    s = 'ball 10$, horse 20$, train 30$'
    expenses = {}
    for line in s.split(","):
        result = re.match(r'([a-z]+)\s+(\d+)', line.strip())
        if result:
            expenses[result.group(1)] = result.group(2)

    print(expenses)


# 5. Find & Replace
def find_replace():
    result = re.sub(r'\w+', 'bla', 'Hello ; World')
    print(result)


# 6. Compile (reuse regular expression object, better performance)
def compile_test():
    ip_regex = re.compile('^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')

    ips = [
        # good IPs
        "127.0.0.1",
        "192.168.1.1",
        "192.168.1.255",
        "255.255.255.255",
        "0.0.0.0",
        "1.1.1.01",
        # bad IPs
        "30.168.1.255.1",
        "127.1",
        "192.168.1.256",
        "-1.2.3.4",
        "1.1.1.1.",
        "3...3"
    ]
    for ip in ips:
        m = ip_regex.match(ip)
        if m:
            print('Valid IP: ', m.group())
        else:
            print('Invalid IP: ', ip)


# Find words starting with vowel
def vowel_test():
    words = 'cat, dog, horse, owl, hawk, oak, elk, Orange'
    result = re.findall(r'\b[aeiou]\w+', words, flags=re.IGNORECASE)
    print(result)

