def longestSubarray(arr):
    size=len(arr)
    cMax=cMin=arr[0]
    current=total=0

    for i in range(1,size):
        if(abs(arr[i] - arr[i-1]) <= 1):
            if(arr[i] == cMax or arr[i] == cMin):
                current += 1
            else:
                if(current > total):
                    total = current
                current = 1
                cMax = max(arr[i-1],arr[i])
                cMin = min(arr[i-1],arr[i])
        else:
            if(current > total):
                total = current
            cMin = cMax = arr[i]
    return total+1


print(longestSubarray([3,2,2,1]))