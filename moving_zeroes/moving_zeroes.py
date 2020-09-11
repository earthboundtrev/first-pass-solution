import math
'''
Input: a List of integers
Returns: a List of integers
'''
def first_pass_moving_zeroes(arr):
    # Your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if abs(arr[j]) < abs(arr[i]):
                temp_variable = arr[j]
                arr[j] = arr[i]
                arr[i] = temp_variable
    
    return arr

def moving_zeroes(arr):
    counter = len(arr) - 1
    for i in range(0, len(arr)):
        if arr[i] == 0 and arr[counter] != 0:
            temp_variable = arr[counter]
            arr[counter] = arr[i]
            arr[i] = arr[counter]
            counter=counter-1
    
    for j in range(0, len(arr)):
        if j+1 == len(arr):
            print("This is the end of the list")
        print(arr[j])

    return arr



if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")