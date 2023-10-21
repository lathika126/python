def miniMaxSum(arr):
    arr.sort()
    min=sum(arr[:-1])
    max=sum(arr[1:])
    print(min,max)
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
