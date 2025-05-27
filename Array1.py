#given an array of integers, and target sum, find the continuous sub array that adds up to the target. 
#if such a subarray exists, return it's indices otherwise return -1
# inputArray = [1, 2, 3, 7, 5], Target = 12, Ouput subarray = 2 to 4


x = int(input("enter the numbers" ))
target = int(input("Enter the target"))


listx = []
for i in range(0, x):
    y = int(input("enter the the number" ))
    listx.append(y)

for i in listx:
    print(i, end = " ")
    i = i+1

for i in listx:
    for j in listx:
        if listx[i]+listx[y] == target:
            print(listx[i], "and", listx[j])
        
        else:
            print("There are no such elements")






