'''
We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. 
Find both these numbers.
'''

def find_corrupt_numbers(arr):
    i=0
    n=len(arr)
    while i<n:
        j=arr[i]-1
        if arr[i]!=arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
        else:
            i+=1
    for i in range(n):
        if i+1!=arr[i]:
            return([arr[i],i+1])
    return [-1,1]

if __name__ == '__main__':
    print(find_corrupt_numbers([3, 1, 2, 5, 2]))
    print(find_corrupt_numbers([3, 1, 2, 3, 6, 4]))