'''
We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
The array can have duplicates,
which means some numbers will be missing. Find all those missing numbers.
'''

#please keep in mind that the array is starting form 1 to n or 0 to n.

def find_missing_numbers(nums):
    ans=[]
    i=0
    n=len(nums)
    while i<n:
        j=nums[i]-1 #since the array starts from 0 and the numbers in the range are 1 to n
        if nums[i]!=nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
        else:
            i+=1
    for i in range(n):
        if nums[i]!=i+1:
            ans.append(i+1)
    return ans
        
if __name__ == '__main__':
    ans=find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1])    
    print(ans)
    print(find_missing_numbers([2, 4, 1, 2]))
    print(find_missing_numbers([2, 3, 2, 1]))