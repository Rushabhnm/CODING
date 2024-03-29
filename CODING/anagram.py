##### ANAGRAM CHECK 1 #####

def anagram_check(x,y):
    ans =  sorted(x) == sorted(y)
    print(ans)
anagram_check("rushabh","saumitra")

##### ANAGRAM CHECK 2 #####

def anagram_check1(x,y):
    for i in set(x):
        if x.count(i) != y.count(i):
            print(False)
            return False
    print(True)
    return True

anagram_check1("rushabh","rushhba") 



##### ANAGRAM CHECK 3 #####

from collections import defaultdict

def anagram_check3(x,y):
    cx = defaultdict(lambda: 0)
    cy = defaultdict(lambda: 0)

    for c in x:
        cx[c] += 1

    for c in y:
        cy[c] += 1

    for c in cx.keys():
        if cx[c] != cy[c]:
            return False
        
    return True

print(anagram_check3("google","logoge"))



##### ANAGRAM CHECK 4 #####

from collections import defaultdict

def anagram_check4(word1,word2):
    x = defaultdict(lambda:1)

    for i in word1:
        x[i]+=1

    for j in word2:
        if j not in x:
            return "Not an anagram"
        else:
            x[j]-=1
    
    return "Anagram found"

print(anagram_check4("google",'logoge'))
