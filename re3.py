import re
string = "Love the life you live123."
pattern = r'\w+'
matches = re.findall(pattern, string)
print("Find all matches:")
print(matches)
pattern = r'\bq\w+'
match = re.search(pattern, string)
if match:
    print("First match for search:")
    print(match.group())
else:
    print("No match found for search")
pattern = r'\W+'
split = re.split(pattern, string)
print("Split string into words:")
print(split)
pattern = r'\d'
sub = re.sub(pattern, '#', string)
print("Substitute digits with '#':")
print(sub)
