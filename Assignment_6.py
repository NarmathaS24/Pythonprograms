list_var=['eat','tea',"tan","ate","nat",'bat']
list_res=[]
dict_res={}
print("Input:",list_var)
for word in list_var:
    sorted_word="".join(sorted(word))

    if sorted_word not in dict_res:
        dict_res[sorted_word]=[word]

    else:
        dict_res[sorted_word] += [word]
#print(dict_res)
print("Output:",list(dict_res.values()))
