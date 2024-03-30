# def productExceptSelf(nums):
#     z = [1]*len(nums)     ##[1,1,1,1]
#     x = [1]*len(nums)     ##[1,1,1,1]
#     y = [1]*len(nums)     ##[1,1,1,1]

#     for i in range(0,len(nums)-1):
#         x[i+1]=x[i]*nums[i]
#     print(x)
        
#     for j in range(len(nums)-1,-1,-1):
#         y[j-1]=y[j]*nums[j]
#         z[j]=y[j]*x[j]
             
#     return z


# print(productExceptSelf([1,2,3,4]))


def productExceptSelf_1(nums):
    x = [1]*len(nums)     # [1,1,1,1]

    pre = 1
    for i in range(len(nums)):
        x[i]=pre
        pre *= nums[i]      
    
    post = 1
    for j in range(len(nums)-1,-1,-1):
        x[j] *= post
        post *= nums[j]

    return x


print(productExceptSelf_1([1,2,3,4]))


# y = [24,12,4,1]