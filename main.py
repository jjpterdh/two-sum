from typing import List 

def twoSum(nums: List[int], target: int) -> List[int]:
    index=[]
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j]==target:
                return [i, j]
        
        

if __name__=='__main__':
    
    
    print("Output: ", twoSum(nums=[3,2,4], target = 6))

    