nums =[]   
for i in range(4): 
    num = int(input('enter a number: ')) 
    nums.append(num)   
for i in range(0,4): 
    for l in range(0,4):
        for n in range(0,4):
            for g in range(0,4):
                print(nums[i],nums[l],nums[n],nums[g])
