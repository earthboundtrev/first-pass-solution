'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here

    empty_list = []
    counter = 0

    for i in range(0, len(arr)):
        if empty_list==[]:
            empty_list.append(arr[i])
        else:
            for j in range (0, len(empty_list)):
                if empty_list[j] == arr[i]:
                    counter=counter+1
                    if counter==2:
                        return arr[i]
                else:
                    empty_list.append(arr[i])
                    counter=counter+1



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")