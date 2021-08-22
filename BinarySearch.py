pos=-1

def binarySearch(listA,searchE):
    lower=0
    upper=len(listA)-1
    while lower<=upper:
        mid=(lower+upper)//2        #'//' is used for integer division
        if listA[mid]==searchE:
            #globals()["pos"]=mid
            global pos
            pos=mid
            return True
        elif listA[mid]<searchE:
            lower=mid+1
        elif listA[mid]>searchE:
            upper=mid-1
    else:
        return False


# Take multiple inputs within a list in a single line  
n = int(input("Enter number of elements : ")) 

# Below line read inputs from user using map() function 
listA = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 

searchE=int(input("Enter the number to be searched : "))

listA.sort() 

if binarySearch(listA,searchE):
    print("Number found at position",pos+1)
else:
    print("Number not found")

