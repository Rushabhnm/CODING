# x={819:"Rushabh",820:"Uma",821:"Navin"}

# for value in x.values():
#     x = list(value)


############ random2 ############

# from collections import defaultdict

# x =["rushabh","uma","navin"]

# y = defaultdict()

# for index,i in enumerate(x):
#     y[index]=i

# print(dict(y))


############ random3 ############

# x = [(1,"rushabh"),(2,"navin"),(3,"uma")]

# print(dict(x))

from collections import defaultdict

def anagram_group(words):
    x = defaultdict(list)
    for index, word in enumerate(words,1):
        x[index]=word
        
    return x
    

print(anagram_group(["tap","pat","cat","bat","tac"]))