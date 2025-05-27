
# def pivot(arr, si, li):
#     index = si
#     i = si

#     while i<li:
#         if arr[i]>arr[li]:
#             i = i +1
#         else:
#             arr[index], arr[i] = arr[i], arr[index]
#             i = i+1
#             index = index +1

#     arr[index], arr[li] = arr[li], arr[index]

#     return index

# def sorting(arr, si, li):
#     if si>=li:
#         return
    
#     PI = pivot(arr, si, li)
#     sorting(arr, si, PI-1)
#     sorting(arr, PI+1, li)

#     return arr

# listx = [1, 65, 4, 2, 9, 99, 77]
# sorting(listx, 0, len(listx)-1)

# print(listx[len(listx)-2])

### But this isn't the most efficient way, the most efficient way is this ###

# def findsecondmax(arr):
#     max = float("-inf")
#     secondmax = float("-inf")

#     for i in range(len(arr)):
#         if arr[i]>max:
#             secondmax = max
#             max = arr[i]
        
#         elif arr[i]<max and arr[i]>secondmax:
#             secondmax = arr[i]

#     return secondmax 

# listx = [1, 2, 8, 6, 99, 77]
# print(findsecondmax(listx))

### let's try finding the smallest element ###

def findsecondmax(arr):
    min = float("inf")
    secondmin = float("inf")

    for i in range(len(arr)):
        if arr[i]<min:
            secondmin = min
            min = arr[i]
        
        elif arr[i]>min and arr[i]<secondmin:
            secondmin = arr[i]

    return secondmin

listx = [1, 2, 8, 6, 99, 77]
print(findsecondmax(listx))


### GREAT ! ###


## 22/01/2025 ( I have forgotten how to find the secondmin/ secondmax element)

def findsecondmin(arr):
    min = float("inf")
    secondmin = float("inf")

    for i in range(len(arr)):
        if arr[i]<min:
            secondmin = min
            min = arr[i]

        elif arr[i]>min and arr[i]<secondmin:
            secondmin = arr[i]

    return [min, secondmin]

print(findsecondmin([1, 9, 8, 7, 4, 99]))



