'''
def product(num):
    res = []
    for i in range(len(num)):
        mul = 1
        for j in range(len(num)):
            if i != j:
                mul = mul*j
        res.append(mul)
num = [1,2,3,4,5]
product(num)
print(res)
'''
'''
num = [1,2,3,1,1,2,3,3,3]
max_num = 0#1
value = -1
for i in num:
    count = 0#1
    for j in num:
        if i == j:
            count +=1
    if count > max_num:
        max_num = count    
        value = i    
print(max_num)
print(value)    
'''
'''
def subset(num,t):
    for i in range(0,len(num)):#0,5
        for j in range(i+1,len(num)):
            if num[i] + num[j] == t:
                return num[i],num[j]
            
num = [1,2,3,4,5,6]
t = 4 #0 1 2
print(subset(num,t))
'''
'''
def sum(num,t):
    i = 0 
    j = len(num)-1
    while i< j:
        sum = num[i] + num[j]
        if sum == t:
            return num[i] , num[j]
        elif sum < t:
            i = i + 1
        else:
            j = j -1
num = [1,2,3,4,5,6,7,8]
t = 15
print(sum(num,t))   
'''             