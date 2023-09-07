import re
pattern = r'a+b*'
strings = ['ab', 'aab', 'abb', 'aaab', 'abbbb', 'bc']
for s in strings:
    if re.match(pattern, s):
        print(f"{s} matches the pattern")
    else:
        print(f"{s} does not match the pattern")
