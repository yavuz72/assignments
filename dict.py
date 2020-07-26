dict1={}
sentence = input('please enter a sentence:')
for i in sentence:
    keys = dict1.keys()
    if i in keys:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)