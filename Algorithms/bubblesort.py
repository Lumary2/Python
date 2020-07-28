def bubbleSort(arr): 
    length = len(arr)

    for i in range(length-1):
        print("Round "+str(i+1))

        for j in range(length-1,i,-1):

            for i in range(len(arr)):
                print(arr[i], end=" ")
            print()
            print("comparing "+ str(arr[j]) +" and "+ str(arr[j-1]))
            print("----------------------")

            if arr[j] < arr[j-1] :
                arr[j], arr[j-1] = arr[j-1], arr[j]

arr = [5, 4, 7, 3, 2, 1, 9]
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print (arr[i], end=" ")