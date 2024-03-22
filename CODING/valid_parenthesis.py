# def is_valid(s):
#     while True:
#         if "()" in s:
#             s = s.replace("()", "")
#         elif "{}" in s:
#             s = s.replace("{}", "")
#         elif "[]" in s:
#             s = s.replace("[]", "")
#         else:
#             # If the string becomes empty, it indicates all brackets are matched.
#             return len(s) == 0

# print(is_valid("({[})"))


def isValid(s):
    open_brackets = []
    for element in s:
        if element in "{[(":
            open_brackets.append(element)
            print(open_brackets)
        else:
            if not open_brackets or \
                (element == "}" and open_brackets[-1] != "{") or \
                (element == "]" and open_brackets[-1] != "[") or \
                (element == ")" and open_brackets[-1] != "(" ):
                    return False
            open_brackets.pop()
            
    return not open_brackets

print(isValid("({})"))