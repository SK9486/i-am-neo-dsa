from collections import deque
def main():
    n = int(input())
    inps = input().split()
    arr = []
    for a in inps:
        arr.append(int(a))
    divide(arr)

def divide(arr):
    if(len(arr) <= 1):
        return arr
    d = (int) (len(arr)/2)
    print("d : ",d)
    arr1 = arr[0:d]
    print("arr1 : ",arr1)
    arr2 = arr[d:len(arr)]
    print("arr2 : ",arr2)
    left = divide(arr1)
    righ = divide(arr2)
    return merge(left,righ)

def merge(arr1,arr2):
    arr = []
    i =0
    j = 0
    print("merge : ")
    print("arr1 : ",arr1)
    print("arr2 : ",arr2)
    while(i<len(arr1) and j<len(arr2)):
        if(arr1[i]>arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        arr.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        arr.append(arr2[j])
        j+=1
    print("arr : ",arr)
    return arr
main()
