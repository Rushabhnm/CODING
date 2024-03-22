


# def palindrome(x):
#     y = str(x)[::-1]
#     if str(x)==y:
#         print(True)
#         return True
#     else:
#         print(False)
#rahul prohanjain
# palindrome(121)




# x = int(input("enter number"))
# y = 0
# while x>0:
#     for i in range(len(str(x))):
#         y = y*10+x%10
#         x = x//10
# print(y)
    



# def romanToInt(s):
#     x = list(s)
#     y = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
#     z = 0
#     for i in x:
#         z+=y[f"{i}"]

#     print(z)

# romanToInt("MCMXCIV")


# def inpp(x):

#     def list_len(a):
#         return len(a)
    
#     x.sort(key=list_len)

#     ans = ""
#     for i in range(len(x[0])):
#         for s in x:
#             print(s)
#             print(s[i])
#             if s[i] != x[0][i]:
#                 return ans
#         ans += x[0][i]

#     return ans

# print(inpp(["rushabh","rushab","ruspqk"]))


print("rushabh"[1])