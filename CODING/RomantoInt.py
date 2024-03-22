
def romanToInt(s):
    x = list(s)
    y = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    z = 0
    for i in range(len(x)-1):
        if y[x[i]]<y[x[i+1]]:
            z-=y[x[i]]
            print(f"minus z, {x[i]}",z)
        else:
            z+=y[x[i]]
            print(f"plus z, {x[i]}",z)
    z +=y[x[len(x)-1]]
    return z



print(romanToInt("MCMLXII"))
