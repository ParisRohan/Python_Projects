#Given an array of ints, return true if one of the first 4 elements in the array is 9

def array_front(num_array):
    for i in range(5):
        if num_array[i] == 9:
            return True
    else:
        return False


num_array=[1,2,9,5,8]

if len(num_array)<4:
    print("Insufficient array size :( ")
else:
    ans=array_front(num_array)
    if ans:
        print("Number 9 is present in first four elements :)")
    else:
        print("Number 9 is absent in first four elements :(")

