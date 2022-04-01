
def checksum(self, nums,target):
    nums = []
    target = 0
    for num in nums:
        for x in range(num+1,len(nums)):
            
            if(nums[num] + nums[x] == target):
                print(nums[num])
                print(nums[x])
 