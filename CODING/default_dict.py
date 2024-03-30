from collections import defaultdict


# def anagram_check1_dict(x,y):
#     cx = defaultdict(lambda: 0)
#     cy = defaultdict(lambda: 0)

#     for c in x:
#         cx[c] += 1

#     for c in y:
#         cx[c] += 1

#     return cx

# print(anagram_check1_dict([1,2,3,4],[1,1,2,3]))


# def DefDectCheck(x):
#     cx = defaultdict(lambda:0)  
#     for i in x:
#         cx[i]+=1


#     print(cx)

# DefDectCheck([1, 2, 3, 8,1,1])


# def map_lists_to_dict(list_keys, list_values):
#     z = {}
#     for key, value in zip(list_values, list_keys):
#         z[key] = value
#     return z

# x = ['a', 'b', 's', 'as', 'q', 'aqw']
# y = [12, 13, 14, 15, 16, 17, 18]

# output = map_lists_to_dict(x, y)
# print(output)

# def map_lists_to_dict(list_keys, list_values):
#     z = {}
#     for key, value in zip(list_values, list_keys):
#         z[key] = value
    
#     # Handle the case where key list is shorter than value list
#     if len(list_keys) < len(list_values):
#         for value in list_values[len(list_keys):]:
#             z[value] = ''
    
#     return z

# x = ['a', 'b', 's', 'as', 'q', 'aqw']
# y = [12, 13, 14, 15, 16, 17, 18]

# output = map_lists_to_dict(x, y)
# print(output)



# x = [1,4213,124,1214,112,312,131]
# y = ['a','ac','aw','cqe','qc','qw']

# z = dict(zip(x,y))
# z.update({key:'' for key in x if key not in z})

# print(z)


# A ={1:"rush",2:"uma",3:"navin"}

# for value in A:
#     print(value)


from collections import defaultdict

x = defaultdict(list)

for i in range(3):
    for j in range(5):
        x[i] = j

print(x)