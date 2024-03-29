
##### for 1 word #####

def alphacovert(word):
    x = list(word)
    y = []
    for i in x:
        z = ord(i)
        y.append(z)
    
    print(y)

alphacovert("rushabh")

##### MULTI WORDS #####

def approach2(words):
    a =[]
    for word in words :
        z=0
        for j in range (len(word)):
            z += ord(word[j])
        a.append(z)
        z=0
    
    return min(a)

print(approach2(["rushabh", "navin", "uma"]))




## for multi-words list ##

# approach 1 useless
# from collections import defaultdict

# def multiword(listwords):
#     names_dict = defaultdict()
#     z= []

#     # Assign the list as the value for each key in the dictionary
#     for index1,name in enumerate(listwords,864):
#         names_dict[index1] = (name)

#     for value in names_dict.values():
#         x = list(value)
#         y = 0
#         for i in range(len(x)):
#             y+=ord(x[i])
#         z.append(y)
#         y=0
    
#     return z
        

# print(multiword(["rushabh", "navin", "uma"]))




        