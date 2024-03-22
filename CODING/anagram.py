# ANAGRAM CHECK 1

# def anagram_check(x,y):
#     ans =  sorted(x) == sorted(y)
#     print(ans)
# anagram_check("rushabh","saumitra")

# ANAGRAM CHECK 2

def anagram_check1(x,y):
    for i in set(x):
        if x.count(i) != y.count(i):
            print(False)
            return False
    print(True)
    return True

anagram_check1("rushabh","rushhba")   



