import math
'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(arr[j]) < abs(arr[i]):
                temp_variable = arr[j]
                arr[j] = arr[i]
                arr[i] = temp_variable
    
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")