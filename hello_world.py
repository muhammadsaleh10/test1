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
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr