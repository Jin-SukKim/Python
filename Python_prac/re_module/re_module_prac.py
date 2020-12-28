import re # 정규표현식

# a.b : . = all words except \t
# a*b : * = repeate including 0
# a+b : + = repeate but not include 0
# a{n}b : {n} = n number
# a{n,m}b : {n,m} b/w n and m
# a?b : ? = 0 or 1

# repeate one or more times from a to z.
p = re.compile('[a-z]+') # - : from ~ to, + : repeate
# p = re.compile('a.b', re.DOTALL) # . : any word, DOTALL option : include all
# p = re.compile('[a-z]', re.I) # I option : ignore uppercase, and lowercase
# p = re.compile('^python\s\w+') # ^ : first word. \s : space. \w : alphabet, num, _. + : repeate.
# p = re.compile('^python\s\w+', re.M) # M : multiline, return all same words.
# sample = '''python one
# python two
# life is too short
# last python'''

# p = re.compile(r'&[#](0[0`7]+|[0-9]+|x[0-9a-fA-F]+);')

# p = re.compile(r'''
# &[#]                    # Start of a numeric entity reference
# (
#       0[0`7]+           # Octal form
#     | [0-9]+            # Decimal Form
#     | x[0-9a-fA-F]+     # Hexadecimal Form
# )
# ;                       # Trailing semicolon
# ''', re.VERBOSE) # VERBOSE : able to compile even though using newline

# \d = [0-9], \D = [^0-9], \s = whitespace([\t\n\r\f\v]), 
# \S = not whitespace([^\t\n\r\f\v]), \w = [a-zA-Z0-9_], \W =[^a-zA-Z0-9_]

# p = re.compile('\section') # whitespcae + ection
# p = re.compile('\\section') # section
# p = re.compile(r'\\section') # \section, r : raw string

# | : or
# ^ : at the beginning, first word should be ^'word'
# $ : at last
# \b : space
# ect, a lot of meta words

# grouping : ().
# re.compile('(abc)+') : find abc repeate
# print(m.group()) or m.group(n)
# ('(abc)\s+\1') # \1 : find when abc group repeate one more time(ex: abc abc)

# ?P<name> : naming grouped words
# (?=w) : find until w
# (?!w) : find not include w
# p.sub(o1, o2) # switching 02 word with 01 that match with patterns

m1 = p.match('python')
m2 = p.match('3 python')
print(m1)
print(m2)

print(m1.group())
print(m1.start())
print(m1.end())
print(m1.span())

s = p.search('3 python')
# print(re.search('python', '3 python'))
print(s)

f = p.findall('life is too short.')
print(f)

f2 =  p.finditer('life is too short.')
print(f2)

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group()) # Greedy
print(re.match('<.*?>', s).group()) # Non-Greedy


