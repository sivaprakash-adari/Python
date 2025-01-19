#
#  Given an array nums containing n distinct numbers in the range [0, n], 
#  return the only number in the range that is missing from the array.
#

def find_missing_number(nums):
     result = 0
     
     for i,n in enumerate(nums):
          print(nums[i])    
     return result

nums = [1,2,3,5]
find_missing_number(nums)k