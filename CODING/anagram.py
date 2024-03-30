# ##### ANAGRAM CHECK 1 #####

# def anagram_check(x,y):
#     ans =  sorted(x) == sorted(y)
#     print(ans)
# anagram_check("rushabh","saumitra")

# ##### ANAGRAM CHECK 2 #####

# def anagram_check1(x,y):
#     for i in set(x):
#         if x.count(i) != y.count(i):
#             print(False)
#             return False
#     print(True)
#     return True

# anagram_check1("rushabh","rushhba") 



# ##### ANAGRAM CHECK 3 #####

# from collections import defaultdict

# def anagram_check3(x,y):
#     cx = defaultdict(lambda: 0)
#     cy = defaultdict(lambda: 0)

#     for c in x:
#         cx[c] += 1

#     for c in y:
#         cy[c] += 1

#     for c in cx.keys():
#         if cx[c] != cy[c]:
#             return False
        
#     return True

# print(anagram_check3("google","logoge"))


# ##### ANAGRAM CHECK 4 #####

# from collections import defaultdict

# def anagram_check4(word1,word2):
#     x = defaultdict(lambda:0)

#     for i in word1:
#         x[i]+=1
#     print(x)

#     for j in word2:
#         if j not in x:
#             return "Not an anagram"
#         else:
#             x[j]-=1
    
#     return "Anagram found"

# print(anagram_check4("google",'logoge'))


##### ANAGRAM CHECK FOR GROUP OF WORDS #####

##################################  APPROACH 1  ##################################

from collections import defaultdict

def anagram_group(words):
    x = defaultdict(list)
    y = defaultdict(lambda :0)
    for word in words:
        for i in word:
            y[i]+=1
        
        y = tuple(sorted(y))
        
        x[y].append(word)
        y= defaultdict(lambda :0)
            
    return x.values()
    

print(anagram_group(["tap","pat","cat","bat","tac"]))


##################################  APPROACH 2  ##################################

from collections import defaultdict

def grp_anagram(words):
    x = defaultdict(list)

    for word in words:
        key = [0]*26
        for i in word:
            key[ord(i)-ord('a')]+=1
        key = tuple(key)
        x[key].append(word)

    return x.values()

print(grp_anagram(["tap","pat","cat","bat","tac"]))



##################################  APPROACH 3  ##################################

from collections import defaultdict

def anagram_group_gpt(words):
    # Define a defaultdict to store groups of anagrams
    groups = defaultdict(list)

    # Iterate through each word in the list
    for word in words:
        # Sort the characters of the word to create a key for grouping anagrams
        sorted_word = ''.join(sorted(word))
        
        # Append the word to its corresponding group in the defaultdict
        groups[sorted_word].append(word)
    
    # Return the values of the defaultdict, which are lists of anagram groups
    return groups

# Test the function with a list of words
print(anagram_group_gpt(["tap", "pat", "cat", "bat", "tac"]))
