x = [0,1,2,3,4]
y = []
z = 1
b = 0
for i in x:
    if i !=0:
        for j in range(len(x)):
            z= z*x[j] 
        z = z/i
        y.append(z)
        z = 1
    else:
        x.remove(0)
        for j in range(len(x)):
            z= z*x[j]
        y.append(z)
        z=1
        x.append(0)  
        b+=1       


print(y[:len(y)-b+1])


