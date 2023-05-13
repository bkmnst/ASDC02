import time


def bubble_sort(data):
    start_time = time.time_ns()
    n = len(data)
    comparisons = 0
    swaps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if data[j][3] > data[j+1][3]:
                data[j], data[j+1] = data[j+1], data[j]
                swaps += 1
    end_time = time.time_ns()
    return (comparisons, swaps, end_time - start_time)


def quick_sort(data):
    start_time = time.time_ns()
    comparisons = 0
    swaps = 0

    def partition(arr, low, high):
        nonlocal comparisons
        nonlocal swaps
        i = (low-1)
        pivot = arr[high][3]
        for j in range(low, high):
            comparisons += 1
            if arr[j][3] <= pivot:
                i = i+1
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
        arr[i+1], arr[high] = arr[high], arr[i+1]
        swaps += 1
        return (i+1)

    def quickSort(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quickSort(arr, low, pi-1)
            quickSort(arr, pi+1, high)
    n = len(data)
    quickSort(data, 0, n-1)
    end_time = time.time_ns()
    return (comparisons, swaps, end_time - start_time)


def insertion_sort(data):
    start_time = time.time_ns()
    n = len(data)
    comparisons = 0
    swaps = 0
    for i in range(1, n):
        key = data[i]
        j = i-1
        while j >= 0 and key[3] < data[j][3]:
            comparisons += 1
            data[j+1] = data[j]
            j -= 1
            swaps += 1
        data[j+1] = key
    end_time = time.time_ns()
    return (comparisons, swaps, end_time - start_time)


with open('bank_accounts.txt', 'r') as file:
    data = [line.strip().split(';') for line in file]

print("Bubble sort:")
comparisons, swaps, time_ns = bubble_sort(data)
print(f"Comparisons: {comparisons}")
print(f"Swaps: {swaps}")
print(f"Time (ns): {time_ns}")

with open('bank_accounts.txt', 'r') as file:
    data = [line.strip().split(';') for line in file]

print("Quick sort:")
comparisons, swaps, time_ns = quick_sort(data)
print(f"Comparisons: {comparisons}")
print(f"Swaps: {swaps}")
print(f"Time (ns): {time_ns}")

with open('bank_accounts.txt', 'r') as file:
    data = [line.strip().split(';') for line in file]

print("Insertion sort:")
comparisons, swaps, time_ns = insertion_sort(data)
print(f"Comparisons: {comparisons}")
print(f"Swaps: {swaps}")
print(f"Time (ns): {time_ns}")
