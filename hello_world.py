#write a fuction for printing hello world
def hello_world():
    print("Hello World")    

#write a function for printing hello world n times
def hello_world_n_times(n):
    for i in range(n):
        print("Hello World")


# create a function for bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-1-i):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

# create a function for selection sort algorithm
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if(arr[j]<arr[min_index]):
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr
