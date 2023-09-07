def ends_with_number(s):
    if s[-1].isdigit():
        return True
    else:
        return False
strings = ['hello', 'world1', 'example123', 'abc123xyz', 'Narmu']
for s in strings:
    if ends_with_number(s):
        print(f"{s} ends with a number")
    else:
        print(f"{s} does not end with a number")
