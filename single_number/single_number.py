'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    counter1=0
    counter2=1

    temp1=arr[counter1]
    temp2=arr[counter2]

    empty_list = []
    
    while arr[counter1] == arr[counter2]:
        counter1=counter1+2
        counter2=counter2+2

        if arr[counter1] != arr[counter2]:
           if arr[counter2+1] == arr[counter1]:
               return arr[counter2]
           elif arr[counter1+1] == arr[counter2]:
               return arr[counter1]
           else:
               return arr[counter1]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 0, 9, 0]

    print(f"The odd-number-out is {single_number(arr)}")