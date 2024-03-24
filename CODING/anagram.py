# ANAGRAM CHECK 1

# def anagram_check(x,y):
#     ans =  sorted(x) == sorted(y)
#     print(ans)
# anagram_check("rushabh","saumitra")

# ANAGRAM CHECK 2

from collections import defaultdict

def anagram_check1(x,y):
    for i in set(x):
        if x.count(i) != y.count(i):
            print(False)
            return False
    print(True)
    return True

# anagram_check1("rushabh","rushhba") 





def anagram_check1_dict(x,y):
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


def group_anagrams(low):
    anagram_group = defaultdict(list)

    for word in low:
        anagagramFound = False
        for repr, loa in anagram_group.items():
            if anagram_check1_dict(word, repr):
                anagram_group[repr].append(word)
                anagagramFound = True
                break
        
        if not anagagramFound:
            anagram_group[word].append(word)
    
    return anagram_group


low = ["POT","TOP","CAT","OTP","MAP","TAC"]

print(group_anagrams(low=low).values())
                



l = [1,1,1,1,1,3,3,4,4,5,5,6,6,6,6,6,6,7,7,8,9]

target = 1


def binSearch(arr, l,r, target):
    if r < l:
        return -1
    
    mid = (l+r)//2

    if arr[mid] == target:
        return mid
    
    if arr[mid] > target:
        return binSearch(arr, l,mid-1, target)
    else:
        